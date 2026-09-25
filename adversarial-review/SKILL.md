---
name: adversarial-review
description: >-
  Materialize a review posture biased to disprove, not approve, before a non-trivial decision stands. Use for architectural decisions made under uncertainty, non-trivial code about to be committed, non-obvious claims ("this is safe", "this scales"), or unfamiliar code — while course-correction is still cheap, not just at the end. Sharper version of fresh-context-review — the framing of the review request decides the answer.
---

# Disprove-Biased Review (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the core procedure is the same everywhere, but how hard to push, how much to delegate, and how much narration to expect differs by tier.

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
