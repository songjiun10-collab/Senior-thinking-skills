---
name: fresh-context-review
description: Review code with the assumptions of the person who wrote it deliberately stripped away. Use after finishing an implementation and before declaring it done, before opening a PR, or when asked to review code that you (or the same session) just wrote. Also use when a change touched more files than expected or when the implementation drifted from the original plan.
---

# Review With Fresh Eyes

This skill's guidance is calibrated per model. Read the file matching the model you're running as before applying it.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 / Claude Mythos 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read whichever file matches the model actually running before applying this skill.

**Running a model not listed above** (Claude Haiku 4.5, Claude Opus 5, an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure. Haiku 4.5 has no `effort` parameter and a 200K context window (not 1M): apply the discipline, but skip that file's effort-level and context-window specifics — they don't hold for Haiku.
