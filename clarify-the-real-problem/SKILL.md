---
name: clarify-the-real-problem
description: Dig out the actual goal behind a request before building anything. Use when a request is ambiguous, when the literal ask smells like an X-Y problem (they asked for a solution, not a problem), or when a wrong interpretation would waste significant work. Also use when the user says "still thinking about it", "what's the best way to do this?", or hands over a vague one-liner that implies hours of work.
---

# Clarify the Real Problem (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the questions to ask are the same everywhere, but how literally to read the request, and how much to surface versus resolve silently, differs by tier.

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
