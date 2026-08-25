#!/usr/bin/env python3
"""PreToolUse/PostToolUse hook for the Task (subagent dispatch) tool.

Mechanizes two of delegate-to-subagents/SKILL.md's checks:

1. Brief looks like a pasted transcript/summary instead of a task + file
   paths (long text, no path-shaped tokens).
2. A large number of dispatches are open at once in the same working
   directory - tracked with a small on-disk counter, incremented on
   PreToolUse and decremented on PostToolUse. 2-3 concurrent dispatches
   on independent domains is the normal, encouraged case (see SKILL.md's
   "Parallel is normal across independent domains") - this only fires past
   OPEN_DISPATCH_WARN_THRESHOLD, where a big fan-out is harder to keep
   independent and harder to reconcile than the usual 2-3-way split.

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

Wire-up (see SKILL.md for the full settings.json snippet): matcher
"Task" on both PreToolUse and PostToolUse, both pointing at this same
script - it tells PreToolUse from PostToolUse by the presence of
tool_response in the hook payload.
"""
import json
import os
import re
import sys
import time

STALE_SECONDS = 3600  # drop a tracked dispatch we never saw close after this long
LONG_BRIEF_CHARS = 4000
OPEN_DISPATCH_WARN_THRESHOLD = 4  # 2-3 concurrent independent-domain dispatches is normal; flag past this
PATH_LIKE_RE = re.compile(r"[./][\w.\-]+/[\w.\-/]+|\b\w+\.(py|md|js|ts|json|yaml|yml|go|rs|java)\b")

STRICT = os.environ.get("DELEGATE_HOOK_STRICT") == "1"


def state_path():
    override = os.environ.get("DELEGATE_HOOK_STATE_FILE")
    if override:
        return override
    base = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    return os.path.join(base, ".claude", "hooks", ".subagent_dispatch_state.json")


def load_state():
    try:
        with open(state_path()) as f:
            data = json.load(f)
        if isinstance(data, list):
            return [t for t in data if isinstance(t, (int, float))]
    except Exception:
        pass
    return []


def save_state(open_dispatches):
    path = state_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(open_dispatches, f)
    except Exception:
        pass  # advisory hook - never fail the tool call over a write error


def note(message):
    print(f"[delegate-to-subagents] {message}", file=sys.stderr if STRICT else sys.stdout)


def finish(hit):
    if hit and STRICT:
        sys.exit(2)  # blocks the PreToolUse call; stderr already went to Claude via note()
    sys.exit(0)


def extract_brief(tool_input):
    if not isinstance(tool_input, dict):
        return ""
    # Task tool's argument names have varied across versions; take the
    # longest string value rather than hard-coding one field name.
    strings = [v for v in tool_input.values() if isinstance(v, str)]
    return max(strings, key=len, default="")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        finish(False)
        return

    if payload.get("tool_name") != "Task":
        finish(False)
        return

    is_post = "tool_response" in payload
    now = time.time()
    open_dispatches = [t for t in load_state() if now - t < STALE_SECONDS]

    if is_post:
        if open_dispatches:
            open_dispatches.pop(0)  # FIFO: closing the oldest still-open dispatch
        save_state(open_dispatches)
        finish(False)
        return

    # PreToolUse from here on.
    hit = False

    if len(open_dispatches) >= OPEN_DISPATCH_WARN_THRESHOLD:
        note(
            f"{len(open_dispatches)} other subagent dispatches are already open and this starts another - "
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

    open_dispatches.append(now)
    save_state(open_dispatches)
    finish(hit)


if __name__ == "__main__":
    main()
