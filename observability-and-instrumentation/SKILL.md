---
name: observability-and-instrumentation
description: Use when shipping production behavior, adding logs, metrics, traces, alerts, retries, queues, or external calls; when an incident is hard to explain from available telemetry; or when a feature needs operational evidence.
---

# Observability and Instrumentation

The discipline is the same everywhere — start with the on-call questions, choose the right signal, follow the instrumentation rules, verify before claiming it's done — but how it's applied is calibrated per model. Pick the file for the model actually running:

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |

Read the file matching the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
