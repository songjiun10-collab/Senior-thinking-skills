---
name: measure-before-optimizing
description: Verify a bottleneck exists before touching performance. Use before any caching, memoization, query rewrite, algorithm swap, or "this seems slow" change; when a spec sets a performance target or Core Web Vitals threshold; when a user reports slowness; or when a PR bundles a performance claim with no before/after number. Skip for a fix where the bottleneck is already obvious from the code itself (e.g. an accidental O(n²) on a hot path).
---

# Measure First

The discipline is the same everywhere — measure, pinpoint, fix, re-measure, and skip optimizing what the data says doesn't matter — but how it's applied is calibrated per model. Pick the file for the model actually running:

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read the file matching the model actually running before applying this skill.

**Running a model not listed above** (an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure — read that one rather than skipping this skill.
