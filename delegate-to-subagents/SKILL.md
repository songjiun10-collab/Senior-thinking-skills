---
name: delegate-to-subagents
description: >-
  Decide when to hand work to a subagent instead of doing it yourself, how to brief it, how to run the fix/review loop when something comes back wrong, and how to verify what comes back. Use when a task is big enough to delegate (independent research, a parallelizable slice, a second opinion, a review pass), when running more than one agent, when a subagent's report claims something is finished, or when a review comes back with findings that need fixing. Skip for single-step edits or when no subagent tooling is available. Bundles an optional PreToolUse/PostToolUse hook (scripts/check_dispatch_brief.py) that nudges on two of the mistakes this skill warns about, plus an execution-state dashboard CLI (scripts/execution_manager.py) for a coordinator tracking multiple workers.
---

# Delegating to Subagents

This skill's substantive guidance (deciding whether to delegate, briefing, coordinating a hierarchy, verifying results, handling blocked/loop cases, and everything else) is calibrated per model. Read the file matching the model you're running as before applying it.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |

Read whichever file matches the model actually running before applying this skill.

The two pieces below — the dispatch-brief hook and the execution-manager script — are fixed infrastructure tied to specific script paths, not model-dependent guidance, so they live here rather than in the per-model files.

## Optional: enforce with a hook

Two of this skill's principles are mechanically catchable — **pasting a long conversation summary verbatim**, and **too many concurrent open dispatches** (2-3 is normal, more than that trips it) — `scripts/check_dispatch_brief.py` detects both right before an Agent call (PreToolUse). By default it **only warns, it doesn't block** (a default chosen with the assumption this may get installed into projects that aren't your own). To actually block, add the environment variable `DELEGATE_HOOK_STRICT=1` to the hook command — the script's header comment documents the exact behavior.

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/delegate-to-subagents/scripts/check_dispatch_brief.py" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/delegate-to-subagents/scripts/check_dispatch_brief.py" }
        ]
      }
    ]
  }
}
```

`Agent` is the built-in dispatch tool's name (some docs/blogs from older Claude Code versions still say `Task` — if your version predates the rename, use that instead and confirm against your own `tool_name` in a hook payload). Hook the same script into both PreToolUse and PostToolUse — PostToolUse closes out the specific dispatch that finished, keyed by the call's `tool_use_id` (hook only one side and open dispatches never get closed). If your skill is installed at a different path, update the command path to match. By default it only warns quietly (visible only in the human-facing transcript) — to make Claude actually react to it (i.e. actually block), prefix the command with `DELEGATE_HOOK_STRICT=1` (`"command": "DELEGATE_HOOK_STRICT=1 python3 ..."`). This hook is example-level enforcement — not a red-team-tested CRITICAL-tier block like Hncs's `protect_never_touch.py`, just a minimal mechanization of this skill's verbal advice. If you need something stronger, use this script as a starting point and adapt it to your project.

**Limitation:** the hook only counts *how many* dispatches are open, it doesn't know *which files* each one touches — two parallel dispatches editing the same file won't trip anything as long as the total count stays under the threshold. Catching that mechanically would mean parsing each brief for the files it intends to touch and cross-checking against the others' — out of scope for this example script; "never let two dispatches edit the same live file" stays something you enforce by reading the briefs yourself.

## Optional: track execution state with a script

Acting as a coordinator over several workers means tracking whose status is what — `scripts/execution_manager.py` is a small CLI for that, so it doesn't have to live in your head or get re-derived from scratch every time you check in:

```bash
python3 scripts/execution_manager.py start worker-a "exploring the auth bug"
python3 scripts/execution_manager.py update worker-a blocked "waiting on a prod API key"
python3 scripts/execution_manager.py dashboard
python3 scripts/execution_manager.py clear worker-a
```

`dashboard` prints one line per tracked worker — status, elapsed time, and note — and flags any `blocked` entry that's been stuck past `EXECUTION_MANAGER_BLOCKED_WARN_SECONDS` (default 1800s). **Be precise about what this does and doesn't do:** it tracks and displays status; it does not detect that a worker has a problem (something has to call `update ... blocked` — the worker itself, or you noticing), and it does not decide what to do about a stale one — that's still your judgment call, same as everywhere else in this skill. Read "problem detected → automatic decision → automatic fix" nowhere in this script; it stops at "here's what's stale, go look."

Optionally wire it as a `PreToolUse` hook on the `Agent` tool so a stale-blocked warning surfaces automatically right before you dispatch yet another worker, instead of only when you remember to run `dashboard` yourself:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/delegate-to-subagents/scripts/execution_manager.py hook" }
        ]
      }
    ]
  }
}
```

This can sit in the same `PreToolUse`/`Agent` matcher block as `check_dispatch_brief.py` above — Claude Code runs every hook command listed under a matcher, in order. State lives in its own file (`.claude/hooks/.execution_manager_state.json` by default, override with `EXECUTION_MANAGER_STATE_FILE`), separate from `check_dispatch_brief.py`'s marker files, so the two don't interfere with each other. Verified with 13 isolated stdin/CLI cases (empty dashboard, start/update/clear, unknown-status rejection, hook mode silent when nothing's stale, hook mode warning once staleness is simulated, PostToolUse and non-Agent calls both silent, malformed stdin fails open, multiple workers with mixed states).
