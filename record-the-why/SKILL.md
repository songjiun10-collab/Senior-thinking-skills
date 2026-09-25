---
name: record-the-why
description: Capture the reasoning behind a decision permanently, not just the decision itself. Use when making an architectural choice, changing a public API or data format, choosing between libraries, or reversing an earlier decision. Also use when a comment would just restate the code instead of explaining a non-obvious constraint. Skip for self-explanatory code or decisions that are trivially reversible.
---

# Record the Why (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the ADR structure and the never-delete-the-record rule are the same everywhere, but how much narration to expect and how eagerly to delegate differs by tier.

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
