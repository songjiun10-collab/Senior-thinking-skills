---
name: persistent-memory
description: >-
  Capture a correction or preference into a durable per-topic file instead of re-learning it every session — the explicit workaround for the fact that Claude Code sessions and subagent dispatches don't remember each other. Use when the same kind of correction keeps recurring across sessions, when starting a task type you expect to repeat, or when delegate-to-subagents's reusable-template advice applies but you need the actual mechanism. Skip for a one-off correction that won't recur, and skip for anything project-wide enough to belong in CLAUDE.md instead. Bundles scripts/memory.py, a small CLI for reading, appending to, and listing memory files.
---

# Persistent Memory

The judgment call — when to persist something, what to write, how much — is calibrated per model. Pick the file for the model actually running:

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read the file matching the model actually running before applying this skill.

**Running a model not listed above** (an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure — read that one rather than skipping this skill.

## The script

`scripts/memory.py` gives you a plain-text-in, plain-text-out CLI over one memory file per topic — no database, no format to learn. This mechanism is the same regardless of which model is running:

```bash
python3 scripts/memory.py show <topic>              # print the current file, or say there isn't one
python3 scripts/memory.py append <topic> "<note>"    # add one dated line
python3 scripts/memory.py list                       # list every topic that has a memory file
```

Files live under `.claude/memory/<topic>.md` by default (override with `MEMORY_DIR`). `show` is meant to run before starting a recurring task — read it the same way you'd read a reusable dispatch template before delegating. `append` is meant to run right after a correction, not batched up for later, or it doesn't get captured at all.

This script only reads and appends — it never rewrites or deletes an existing line, so pruning a stale entry (see the model file's "Keeping it honest") is a manual edit, not something the script does for you silently.
