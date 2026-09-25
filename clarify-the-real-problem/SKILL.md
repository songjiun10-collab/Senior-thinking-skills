---
name: clarify-the-real-problem
description: Dig out the actual goal behind a request before building anything. Use when a request is ambiguous, when the literal ask smells like an X-Y problem (they asked for a solution, not a problem), or when a wrong interpretation would waste significant work. Also use when the user says "still thinking about it", "what's the best way to do this?", or hands over a vague one-liner that implies hours of work.
---

# Clarify the Real Problem (router)

This skill is tuned per model. Pick the file that matches the model actually running, and apply it in full — the questions to ask are the same everywhere, but how literally to read the request, and how much to surface versus resolve silently, differs by tier.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |

Read the file matching the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
