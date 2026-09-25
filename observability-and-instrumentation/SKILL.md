---
name: observability-and-instrumentation
description: Use when shipping production behavior, adding logs, metrics, traces, alerts, retries, queues, or external calls; when an incident is hard to explain from available telemetry; or when a feature needs operational evidence.
---

# Observability and Instrumentation

The discipline is the same everywhere — start with the on-call questions, choose the right signal, follow the instrumentation rules, verify before claiming it's done — but how it's applied is calibrated per model. Pick the file for the model actually running:

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
