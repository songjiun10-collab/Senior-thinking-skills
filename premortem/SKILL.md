---
name: premortem
description: Map the failure scenarios before writing the happy path. Use before implementing any feature that touches I/O, user input, external services, concurrency, or persisted state. Also use when adding error handling, when a bug report suggests an unhandled edge case, or when reviewing whether a design is production-ready. Covers both "what breaks" and "how would we even find out".
---

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

This skill is tuned per model. Pick the file matching the model actually running:

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read the file matching the model currently running before applying this skill.

**Running a model not listed above** (an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure.
