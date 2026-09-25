---
name: plan-on-disk
description: Keep the active plan on disk instead of in the context window — task_plan.md, findings.md, progress.md — so it survives /clear, compaction, crashes, and hour ten of a long run. Use when starting multi-step work expected to outlast one sitting or one context window, resuming after a /clear or compaction, when work drifts from the original intent after many tool calls, or when handing a long-running task to an agent or subagent chain. Skip for short tasks that fit in one sitting and never leave the session.
---

# Plan on Disk

The discipline is the same everywhere — three files, recitation over memory, completion as a gate not a feeling — but how it's applied is calibrated per model. Pick the file for the model actually running:

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |

Read the file matching the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
