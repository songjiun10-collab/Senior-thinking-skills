---
name: root-cause-discipline
description: Find the actual cause instead of suppressing the symptom. Use when fixing any bug whose cause isn't immediately obvious, investigating a performance regression, or about to add a defensive check (null guard, retry, try/except) to make an error go away. Starts by checking whether the problem is already solved somewhere before digging.
---

# Root Cause Discipline (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the core procedure (the four phases, the "is this already solved" check, the iron rule) is the same everywhere, but how literally to state the process, how much to delegate, and how much narration to expect differs by tier.

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
