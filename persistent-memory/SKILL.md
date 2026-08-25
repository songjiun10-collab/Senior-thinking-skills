---
name: persistent-memory
description: >-
  Capture a correction or preference into a durable per-topic file instead of re-learning it every session — the explicit workaround for the fact that Claude Code sessions and subagent dispatches don't remember each other. Use when the same kind of correction keeps recurring across sessions, when starting a task type you expect to repeat, or when delegate-to-subagents's reusable-template advice applies but you need the actual mechanism. Skip for a one-off correction that won't recur, and skip for anything project-wide enough to belong in CLAUDE.md instead. Bundles scripts/memory.py, a small CLI for reading, appending to, and listing memory files.
---

# Persistent Memory

Claude Code doesn't remember you between sessions, and a dispatched subagent doesn't remember anything at all — it starts from zero session history every time (see `delegate-to-subagents`). Some other agent platforms build in standing per-agent memory that quietly improves with correction; Claude Code doesn't have that layer. The honest substitute is the same one used for a recurring dispatch brief: write down what was learned, in a file, and load that file before repeating the task.

This isn't a workaround to feel bad about — an explicit file beats implicit memory for exactly the reasons `record-the-why` and `honest-artifacts` already argue: you can read it, diff it, prune it, and know exactly why a decision is still in effect, none of which is true of memory you can't inspect.

## When to make one

- The same kind of correction has come up more than once ("no, always use tabs here," "don't touch the generated files," "this client wants short replies")
- You're starting a task type you expect to repeat (a recurring review, a recurring report format, a recurring delegation brief)
- Don't make one for a correction you're confident won't recur — that's just noise to maintain

## Where it belongs

- **Project-wide and stable** (a convention every contributor should know) → `CLAUDE.md`, not a memory file. `CLAUDE.md` is read every session by design; a memory file isn't unless something loads it.
- **Narrower, more volatile, or still being refined** (this user's phrasing preference, a client's quirks, a not-yet-settled workflow) → a memory file, e.g. `.claude/memory/<topic>.md`. Cheap to create, cheap to throw away, doesn't compete for space in CLAUDE.md.
- Genuinely one-off → neither. Not everything needs to survive the session.

## What goes in it

- Distilled corrections, not transcript — the same "brief, not pasted history" principle as `delegate-to-subagents`'s "How to brief." A raw conversation log makes the next reader re-derive the lesson instead of just applying it.
- One line per correction, dated, in your own words — not the user's exact wording captured verbatim, which drifts out of context without the conversation around it.
- The current, still-true state — not a running log of everything that was ever said. Superseded corrections get replaced, not appended forever (see "Keeping it honest" below).

## Keeping it honest

- **Review it periodically, don't just append.** A memory file that only grows is exactly the kind of unverified, never-re-checked artifact `honest-artifacts` warns about — a correction from six months ago may no longer apply.
- If two entries conflict, that's a signal the situation changed — resolve it, don't leave both standing.
- A memory file that hasn't been touched in a long time and no longer matches how the task is actually done is worse than no file — it actively misleads the next read. Delete it or update it; don't let it fossilize.

## The script

`scripts/memory.py` gives you a plain-text-in, plain-text-out CLI over one memory file per topic — no database, no format to learn:

```bash
python3 scripts/memory.py show <topic>              # print the current file, or say there isn't one
python3 scripts/memory.py append <topic> "<note>"    # add one dated line
python3 scripts/memory.py list                       # list every topic that has a memory file
```

Files live under `.claude/memory/<topic>.md` by default (override with `MEMORY_DIR`). `show` is meant to run before starting a recurring task — read it the same way you'd read a reusable dispatch template before delegating. `append` is meant to run right after a correction, not batched up for later, or it doesn't get captured at all.

This script only reads and appends — it never rewrites or deletes an existing line, so pruning a stale entry (see "Keeping it honest") is a manual edit, not something the script does for you silently.
