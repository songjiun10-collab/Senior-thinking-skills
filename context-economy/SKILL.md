---
name: context-economy
description: Decide what information goes where — in context, in a file, or dropped. Use when handing work off (to another session, agent, or person), when a task involves large files or long outputs, when writing a plan or spec that must outlive the conversation, or when the conversation is getting long enough that earlier details are at risk. Also use when deciding whether an answer should be chat text or a durable artifact.
---

# Context Economy

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
