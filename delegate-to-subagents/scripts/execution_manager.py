#!/usr/bin/env python3
"""Execution-state dashboard for the "execution manager" role in a
coordinator/worker hierarchy (see delegate-to-subagents/SKILL.md's
"Coordinating a hierarchy"). Answers one narrow question honestly: this
tracks and displays status, it does NOT detect problems or decide what
to do about them - "a worker's been blocked for 40 minutes" still needs
a person or an agent to look at the dashboard and judge; this script
can't do that part, and doesn't try to.

CLI (explicit, called by whatever's acting as the execution manager):

    execution_manager.py start <worker> ["<note>"]
    execution_manager.py update <worker> <in_progress|blocked|complete> ["<note>"]
    execution_manager.py dashboard
    execution_manager.py clear <worker>

Optional hook mode (wire to PreToolUse on the Agent tool, see SKILL.md's
settings.json snippet): prints the dashboard, but only when something's
been "blocked" past EXECUTION_MANAGER_BLOCKED_WARN_SECONDS (default
1800s) - a nudge to look before dispatching yet another worker while an
existing one is stuck, not a gate on the dispatch itself.

    execution_manager.py hook

State lives in one JSON file (default
.claude/hooks/.execution_manager_state.json, override with
EXECUTION_MANAGER_STATE_FILE) - a dict keyed by worker name. Advisory
only, same as this bundle's other scripts - never blocks a dispatch,
only prints.
"""
import json
import os
import sys
import time

VALID_STATUSES = ("in_progress", "blocked", "complete")
BLOCKED_WARN_SECONDS = int(os.environ.get("EXECUTION_MANAGER_BLOCKED_WARN_SECONDS", "1800"))


def state_path():
    override = os.environ.get("EXECUTION_MANAGER_STATE_FILE")
    if override:
        return override
    base = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    return os.path.join(base, ".claude", "hooks", ".execution_manager_state.json")


def load_state():
    try:
        with open(state_path()) as f:
            data = json.load(f)
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def save_state(state):
    path = state_path()
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(state, f)
    except Exception:
        pass  # advisory tool - never crash a dispatch over a write error


def fmt_elapsed(seconds):
    seconds = int(seconds)
    if seconds < 60:
        return f"{seconds}s"
    if seconds < 3600:
        return f"{seconds // 60}m"
    return f"{seconds // 3600}h{(seconds % 3600) // 60}m"


def cmd_start(worker, note):
    state = load_state()
    now = time.time()
    state[worker] = {"status": "in_progress", "started_at": now, "updated_at": now, "note": note}
    save_state(state)
    print(f"Tracking '{worker}' as in_progress.")


def cmd_update(worker, status, note):
    if status not in VALID_STATUSES:
        print(f"Unknown status '{status}' - must be one of {', '.join(VALID_STATUSES)}.", file=sys.stderr)
        sys.exit(1)
    state = load_state()
    now = time.time()
    if worker not in state:
        state[worker] = {"status": status, "started_at": now, "updated_at": now, "note": note}
    else:
        state[worker]["status"] = status
        state[worker]["updated_at"] = now
        if note:
            state[worker]["note"] = note
    save_state(state)
    print(f"'{worker}' -> {status}.")


def cmd_clear(worker):
    state = load_state()
    if worker in state:
        del state[worker]
        save_state(state)
        print(f"Cleared '{worker}'.")
    else:
        print(f"No entry for '{worker}'.")


def _dashboard_lines(state, now):
    lines = []
    any_blocked_stale = False
    for worker, info in sorted(state.items()):
        status = info.get("status", "?")
        elapsed = now - info.get("started_at", now)
        since_update = now - info.get("updated_at", now)
        note = info.get("note") or ""
        flag = ""
        if status == "blocked" and since_update >= BLOCKED_WARN_SECONDS:
            flag = f"  *** blocked {fmt_elapsed(since_update)}, past {fmt_elapsed(BLOCKED_WARN_SECONDS)} threshold ***"
            any_blocked_stale = True
        line = f"{worker:<20} {status:<12} {fmt_elapsed(elapsed):>6}  {note}{flag}"
        lines.append(line)
    return lines, any_blocked_stale


def cmd_dashboard():
    state = load_state()
    if not state:
        print("No tracked workers.")
        return
    now = time.time()
    lines, _ = _dashboard_lines(state, now)
    for line in lines:
        print(line)


def cmd_hook():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
        return
    if payload.get("tool_name") != "Agent" or "tool_response" in payload:
        sys.exit(0)
        return
    state = load_state()
    if not state:
        sys.exit(0)
        return
    now = time.time()
    lines, any_blocked_stale = _dashboard_lines(state, now)
    if any_blocked_stale:
        print("[execution-manager] At least one tracked worker has been blocked past the warning "
              "threshold - check before dispatching another:")
        for line in lines:
            print(f"  {line}")
    sys.exit(0)


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(1)

    cmd = args[0]
    if cmd == "start" and len(args) in (2, 3):
        cmd_start(args[1], args[2] if len(args) == 3 else "")
    elif cmd == "update" and len(args) in (3, 4):
        cmd_update(args[1], args[2], args[3] if len(args) == 4 else "")
    elif cmd == "dashboard" and len(args) == 1:
        cmd_dashboard()
    elif cmd == "clear" and len(args) == 2:
        cmd_clear(args[1])
    elif cmd == "hook" and len(args) == 1:
        cmd_hook()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
