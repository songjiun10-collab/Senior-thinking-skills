#!/usr/bin/env python3
"""PreToolUse/PostToolUse hook nudging toward senior-engineer-mindset/SKILL.md's
own "Output format" rule: a hard-to-reverse decision gets a check-in
(AskUserQuestion), not a silent edit.

Mechanism:
- PostToolUse on AskUserQuestion writes a fresh timestamp sentinel - "a
  check-in just happened."
- PreToolUse on Edit/Write/MultiEdit checks whether the target path looks
  like a hard-to-reverse surface (schema/migration/public API/dependency
  manifest - the same category the router's own "Situational picks" table
  names) and, if so, whether that sentinel is still fresh (within
  ASK_HOOK_WINDOW_SECONDS, default 1800s). No fresh check-in -> a note.

Default behavior: ADVISORY, not enforcing - same contract as
delegate-to-subagents/scripts/check_dispatch_brief.py. On a hit, this
prints a note and exits 0; that's visible to the human in the transcript
(Ctrl-R) but not fed back to the model. Set ASK_HOOK_STRICT=1 to make a
hit exit 2 instead (blocks the edit, reason fed back to Claude).

Fail-open by design: example/advisory hook for a portable skill bundle,
not a security boundary. Any unexpected input or internal error is
swallowed as "allow, say nothing."

Known heuristic limits: path-based matching can't tell a real schema
change from an unrelated edit to a file that merely lives in a
migrations/ folder, and can't tell a dependency version bump from a
comment-only edit to a manifest file. A false positive is a wasted
nudge, not a blocked edit (by default); a false negative just means no
nudge - either way this is a prompt to think, not a guarantee.

Wire-up (see SKILL.md for the full settings.json snippet): matcher
"Edit|Write|MultiEdit" on PreToolUse, matcher "AskUserQuestion" on
PostToolUse, both pointing at this same script - it tells the two apart
by tool_name.
"""
import json
import os
import re
import sys
import time

WINDOW_SECONDS = int(os.environ.get("ASK_HOOK_WINDOW_SECONDS", "1800"))
STRICT = os.environ.get("ASK_HOOK_STRICT") == "1"

# Same category the router's own "Situational picks" table names as
# hard-to-reverse: schema, public API, migration, dependency.
_HARD_TO_REVERSE_RE = re.compile(
    r"(^|/)migrations?/"
    r"|schema"
    r"|\.sql$"
    r"|openapi\.ya?ml$|swagger\.ya?ml$"
    r"|\.proto$"
    r"|(^|/)(package\.json|requirements\.txt|go\.mod|Cargo\.toml|Gemfile|pyproject\.toml)$",
    re.IGNORECASE,
)


def sentinel_path():
    override = os.environ.get("ASK_HOOK_STATE_FILE")
    if override:
        return override
    base = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    return os.path.join(base, ".claude", "hooks", ".recent_ask_user_question.json")


def mark_asked():
    path = sentinel_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump({"timestamp": time.time()}, f)
    except Exception:
        pass  # advisory hook - never fail the tool call over a write error


def recently_asked():
    path = sentinel_path()
    try:
        with open(path) as f:
            data = json.load(f)
        return (time.time() - float(data.get("timestamp", 0))) < WINDOW_SECONDS
    except Exception:
        return False


def note(message):
    print(f"[senior-engineer-mindset] {message}", file=sys.stderr if STRICT else sys.stdout)


def finish(hit):
    if hit and STRICT:
        sys.exit(2)
    sys.exit(0)


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        finish(False)
        return

    tool_name = payload.get("tool_name")

    if tool_name == "AskUserQuestion":
        if "tool_response" in payload:
            mark_asked()
        finish(False)
        return

    if tool_name not in ("Edit", "Write", "MultiEdit"):
        finish(False)
        return

    file_path = (payload.get("tool_input") or {}).get("file_path", "")
    if not file_path or not _HARD_TO_REVERSE_RE.search(file_path):
        finish(False)
        return

    if recently_asked():
        finish(False)
        return

    note(
        f"{file_path} looks like a hard-to-reverse surface (schema/migration/public API/"
        "dependency) and no AskUserQuestion check-in has happened in the last "
        f"{WINDOW_SECONDS}s - senior-engineer-mindset's Output format section says a "
        "hard-to-reverse decision gets a check-in before the edit, not after. If this one's "
        "direction is genuinely obvious, proceed; otherwise ask first."
    )
    finish(True)


if __name__ == "__main__":
    main()
