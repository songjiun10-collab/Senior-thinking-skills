---
name: search-first
description: Check current documentation and prior art before writing code against any external API, library, or framework. Use whenever the task touches a third-party library, SDK, API, CLI flag, config format, or language/framework version behavior. Especially when writing code from memory about how something works, when a version number is involved, or when an API "should" work a certain way but hasn't been verified.
---

# Search First (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the verification order and cost-sense judgment are the same everywhere, but how much narration to expect and how eagerly to delegate a lookup differs by tier.

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
