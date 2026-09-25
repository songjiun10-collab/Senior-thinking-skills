---
name: verify-before-agreeing
description: Evaluate review feedback technically instead of performatively agreeing — before implementing a review comment, when feedback seems unclear or technically wrong, when multiple items need prioritization, or when a suggestion conflicts with an existing decision. Use when receiving code review comments from any source — human reviewer, PR comments, or a subagent's review report. Skip for feedback that's unambiguously correct and trivial (typos, style nits matching the repo's conventions).
---

# Verify Before Agreeing

This skill's full instructions are split per model, since the same guidance needs different emphasis depending on what's running it.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 / Claude Mythos 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read the file matching the model actually running before applying this skill.

**Running a model not listed above** (Claude Haiku 4.5, Claude Opus 5, an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure — read that one rather than skipping this skill.
