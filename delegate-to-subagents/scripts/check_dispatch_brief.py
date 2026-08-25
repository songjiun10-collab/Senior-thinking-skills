#!/usr/bin/env python3
"""PreToolUse/PostToolUse hook for the Agent (subagent dispatch) tool.

Mechanizes two of delegate-to-subagents/SKILL.md's checks:

1. Brief looks like a pasted transcript/summary instead of a task + file
   paths (long text, no path-shaped tokens).
2. A large number of dispatches are open at once in the same working
   directory - tracked via one marker file per open dispatch (named by
   the call's tool_use_id, which Claude Code keeps stable between the
   PreToolUse and PostToolUse events for the same invocation), created
   on PreToolUse and removed on PostToolUse. 2-3 concurrent dispatches
   on independent domains is the normal, encouraged case (see SKILL.md's
   "Parallel is normal across independent domains") - this only fires past
   OPEN_DISPATCH_WARN_THRESHOLD, where a big fan-out is harder to keep
   independent and harder to reconcile than the usual 2-3-way split.

One file per dispatch (rather than one shared JSON list) is deliberate:
concurrent PreToolUse calls creating their own distinctly-named file don't
race each other the way concurrent readers/writers of one shared blob
would, and PostToolUse removes the exact file its own tool_use_id created
instead of guessing which of several open entries just finished.

Default behavior: ADVISORY, not enforcing. On a hit, this prints a note
and exits 0. Per Claude Code's hook contract, exit-0 stdout from a
PreToolUse/PostToolUse hook is visible to the human in the transcript
(Ctrl-R) but is NOT fed back to the model - so by default this is a
signal for whoever is watching the session, not a behavior change for
Claude. Set DELEGATE_HOOK_STRICT=1 in the hook's env to make a hit exit
2 instead: that blocks the PreToolUse call (tool doesn't run) and its
stderr is fed back to Claude as the reason, so it can self-correct.

Fail-open by design: this is an example/advisory hook for a portable
skill bundle, not a security boundary. Any unexpected input, missing
field, or internal error is swallowed and treated as "allow, say
nothing" - never block due to a bug in this script. Contrast with a
project's own CRITICAL hooks (e.g. a deny-by-default guard on files that
must never change without sign-off), which should fail closed. This one
should not.

Known heuristic limits, not bugs to chase further in an advisory script:
the brief-detection regex only needs one path-shaped token anywhere in a
long paste to pass, and "longest string field" as a brief-source guess
can misfire if a future tool schema adds another long string field ahead
of "prompt". Good enough for a nudge; not a substitute for actually
reading the dispatch.

Wire-up (see SKILL.md for the full settings.json snippet): matcher
"Agent" on both PreToolUse and PostToolUse, both pointing at this same
script - it tells PreToolUse from PostToolUse by the presence of
tool_response in the hook payload.
"""
import json
import os
import re
import sys
import time

ORPHAN_MAX_AGE_SECONDS = 24 * 3600  # opportunistic cleanup for a dispatch whose PostToolUse never ran (crash, etc) - not used to hide a live one from the count
LONG_BRIEF_CHARS = 4000
OPEN_DISPATCH_WARN_THRESHOLD = 4  # 2-3 concurrent independent-domain dispatches is normal; flag past this
PATH_LIKE_RE = re.compile(r"[./][\w.\-]+/[\w.\-/]+|\b\w+\.(py|md|js|ts|json|yaml|yml|go|rs|java)\b")

STRICT = os.environ.get("DELEGATE_HOOK_STRICT") == "1"


def state_dir():
    override = os.environ.get("DELEGATE_HOOK_STATE_DIR")
    if override:
        return override
    base = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    return os.path.join(base, ".claude", "hooks", ".subagent_dispatch_state")


def marker_path(tool_use_id):
    safe_id = re.sub(r"[^A-Za-z0-9_.-]", "_", tool_use_id) or "unknown"
    return os.path.join(state_dir(), safe_id)


def count_open_dispatches():
    """Count marker files, opportunistically deleting ones far too old to
    still be a real dispatch (a crashed subagent whose PostToolUse never
    fired). Doesn't hide a merely-long-running dispatch from the count -
    only ORPHAN_MAX_AGE_SECONDS-old entries are treated as dead."""
    d = state_dir()
    try:
        names = os.listdir(d)
    except Exception:
        return 0
    now = time.time()
    count = 0
    for name in names:
        path = os.path.join(d, name)
        try:
            age = now - os.path.getmtime(path)
        except Exception:
            continue
        if age > ORPHAN_MAX_AGE_SECONDS:
            try:
                os.remove(path)
            except Exception:
                pass
            continue
        count += 1
    return count


def open_dispatch(tool_use_id):
    path = marker_path(tool_use_id)
    try:
        os.makedirs(state_dir(), exist_ok=True)
        # O_CREAT|O_EXCL: atomic create, never overwrites/races a concurrent one
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.close(fd)
    except Exception:
        pass  # advisory hook - never fail the tool call over a write error


def close_dispatch(tool_use_id):
    try:
        os.remove(marker_path(tool_use_id))
    except Exception:
        pass  # already gone, or state dir unwritable - fine, this is advisory


def note(message):
    print(f"[delegate-to-subagents] {message}", file=sys.stderr if STRICT else sys.stdout)


def finish(hit):
    if hit and STRICT:
        sys.exit(2)  # blocks the PreToolUse call; stderr already went to Claude via note()
    sys.exit(0)


def extract_brief(tool_input):
    if not isinstance(tool_input, dict):
        return ""
    # The Agent tool's own brief field is "prompt"; prefer it explicitly so a
    # long "description" (meant to be a short 3-5 word label) or another
    # string field can't outrank the real brief. Other subagent-dispatch
    # tools may name it differently, so fall back to the longest string
    # value if "prompt" isn't there or isn't a string.
    prompt = tool_input.get("prompt")
    if isinstance(prompt, str):
        return prompt
    strings = [v for v in tool_input.values() if isinstance(v, str)]
    return max(strings, key=len, default="")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        finish(False)
        return

    if payload.get("tool_name") != "Agent":
        finish(False)
        return

    tool_use_id = payload.get("tool_use_id")
    is_post = "tool_response" in payload

    if is_post:
        if isinstance(tool_use_id, str):
            close_dispatch(tool_use_id)
        finish(False)
        return

    # PreToolUse from here on.
    hit = False
    open_count = count_open_dispatches()

    if open_count >= OPEN_DISPATCH_WARN_THRESHOLD:
        note(
            f"{open_count} other subagent dispatches are already open and this starts another - "
            "2-3 concurrent independent-domain dispatches is normal, but at this count, double-check they're "
            "all actually unrelated files/domains and small enough to review when you merge them back."
        )
        hit = True

    brief = extract_brief(payload.get("tool_input"))
    if len(brief) > LONG_BRIEF_CHARS and not PATH_LIKE_RE.search(brief):
        note(
            f"The brief is {len(brief)} chars with no path-shaped tokens in it - "
            "check whether this is a pasted conversation summary or raw text rather than a scoped task. "
            "Passing file paths and letting the subagent read them itself is usually cheaper."
        )
        hit = True

    if isinstance(tool_use_id, str):
        open_dispatch(tool_use_id)
    finish(hit)


if __name__ == "__main__":
    main()
