---
name: chestertons-fence
description: Understand why existing code exists before removing, simplifying, or refactoring it — Chesterton's Fence. Use before deleting code that looks dead or unnecessary, before simplifying anything you didn't write, or when a "cleanup" urge shows up mid-task. Companion to surgical-change and simplicity-budget — this is the check that runs before either of those act.
---

# Chesterton's Fence (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the core discipline (understand before you touch) is the same everywhere, but how the investigation gets done and what to watch for differs by tier.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 / Claude Mythos 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read the file matching the model actually running before applying this skill.

**Running a model not listed above** (Claude Haiku 4.5, Claude Opus 5, an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure — read that one rather than skipping this skill. Haiku 4.5 has no `effort` parameter and a 200K context window (not 1M): apply the discipline, but skip that file's effort-level and context-window specifics — they don't hold for Haiku.
