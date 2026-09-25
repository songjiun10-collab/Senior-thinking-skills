---
name: security-review
description: Review security-sensitive code changes before they ship — injection, broken auth, access control, secrets, data exposure — for diffs touching auth, user input, APIs, databases, or credentials. Use before a PR or merge when the change touches security-relevant paths, when adding an endpoint or auth flow, or when handling user input or credentials. Skip for diffs with no security surface (UI-only, docs, refactors with no input or trust-boundary change).
---

# Security Review (router)

This skill is tuned per model. The OWASP checklist itself doesn't change; the process guidance around it does — pick the file that matches the model actually running.

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
