---
name: chestertons-fence
description: Understand why existing code exists before removing, simplifying, or refactoring it — Chesterton's Fence. Use before deleting code that looks dead or unnecessary, before simplifying anything you didn't write, or when a "cleanup" urge shows up mid-task. Companion to surgical-change and simplicity-budget — this is the check that runs before either of those act.
---

# Chesterton's Fence (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the core discipline (understand before you touch) is the same everywhere, but how the investigation gets done and what to watch for differs by tier.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |

Read the file matching the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
