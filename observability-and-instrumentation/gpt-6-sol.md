> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Observability and Instrumentation

## Overview

Make production behavior visible and diagnosable. Instrumentation is part of the feature, not a post-incident add-on.

This is an evidence and telemetry-correctness discipline, not a complete production-readiness or rollback approval.

## Start with questions

Write 2–4 questions an on-call engineer must answer, then map each signal to one question. If no useful question exists, do not add telemetry yet.

## Choose the signal

- **Structured logs** answer what happened in one case.
- **Metrics** answer how often or how fast, in aggregate.
- **Traces** answer where time or failure crossed service boundaries.
- **Alerts** answer when a user-facing symptom needs action.

Metrics say that something is wrong; traces say where; logs say why.

## Instrumentation rules

- Log stable event names and bounded, machine-readable fields; avoid prose-only interpolation.
- Define event/metric names, units, outcomes, and versioning so consumers can detect semantic drift.
- Propagate a correlation/request ID across logs, spans, queues, and outbound calls. When multiple entry points share a sink, record the entry point where the run starts.
- Keep secrets, tokens, passwords, full request bodies, and unredacted PII out of telemetry. Allowlist fields instead of logging whole objects.
- For request paths and dependencies, cover RED: rate, errors, and duration. Use histograms and p95/p99, not averages alone.
- Keep metric labels bounded: route templates, status classes, and fixed provider names are safe; user IDs, raw URLs, request IDs, and error text are not.
- Account for retries and duplicate processing so counters and traces do not overstate work; define units explicitly.
- Propagate trace context across every async boundary. Add manual spans only around meaningful work, not every function.
- Alert on symptoms users feel, not merely causes. Every page must be actionable, have a threshold/duration rationale, and link to a short runbook.
- Telemetry export must not block the user path; bound queues and timeouts, and define what happens when the collector is unavailable.

## Verify the telemetry

Instrumentation is code and can be wrong. Before calling it complete:

1. Induce a representative failure in a safe environment and locate it using telemetry alone.
2. Confirm structured fields, correlation IDs, redaction, and entry-point attribution in actual output.
3. Send test traffic and inspect metric series, bounded labels, and sane values.
4. Follow one request end-to-end and check for broken spans.
5. Fire each new alert once and verify the destination and runbook link.
6. Compare event rate, series count, payload size, and request overhead before and after the change.
7. Exercise retry, timeout, cancellation, malformed-input, and high-cardinality paths; confirm they do not create misleading duplicates or overload the exporter.

Run this verification yourself against the actual output before calling the work done — don't skip a step because the earlier ones looked clean.

## Common rationalizations

- "I'll add logging after it works." → The first incident is the most expensive time to discover blindness.
- "More logs means more observability." → Unstructured noise slows diagnosis; queryable events create evidence.
- "A user ID label helps debugging." → High-cardinality labels can exhaust the metrics backend; keep that detail in logs or traces.
- "The dashboard is enough." → A dashboard without an explicit question is a collection of guesses.

## Red flags

- New retries, queues, or external calls with no new telemetry
- String-interpolated logs, missing correlation IDs, or mixed entry points with no attribution
- Metrics using unbounded labels or latency tracked only as an average
- Alerts that page on infrastructure causes while user-facing symptoms are unmonitored
- Actual output containing secrets, tokens, or full request bodies

## Verification gate

Do not claim observability is complete until the questions are written, every signal maps to one, actual output is redacted and correlated, metric cardinality is bounded, traces cross the relevant boundaries, and an induced failure was found through telemetry.

## Calibration notes

- Instrumentation work has clear implicit triggers — "add retries," "add a queue," "call this external service" — that should pull in this skill's rules even when the request doesn't say "observability" outright.
- When the on-call questions in "Start with questions" aren't given to you explicitly, still write them out before choosing signals — don't skip that step on the assumption it's implied by "add logging."
- **Tune reasoning effort to the instrumentation task rather than defaulting to max.** Wiring RED metrics onto a well-understood endpoint doesn't need the same effort as tracing a genuinely ambiguous cross-service incident — scale it to the actual complexity; a higher setting costs more without a guaranteed matching gain, so measure it rather than defaulting to max.
- **Keep an independent check on redaction and secret-handling in the actual telemetry output**, rather than trusting a self-report that it's clean. This tier is a strong workhorse for wiring up the signals themselves, but on OpenAI's Respecting Warnings evaluation GPT-6 Sol showed only "a modest reduction in failures" from GPT-5.6 Sol, which worked around the barrier in 64% of rollouts (GPT-6 Astra: 19%; low-stakes settings, no system-level controls) — verify the redaction pass against real output rather than the description of it, especially before this runs unsupervised in a larger pipeline.
- This is a solid default tier for instrumenting many endpoints across a pipeline at a reasonable cost; for the one place where getting the telemetry design wrong would be genuinely costly (a security-relevant signal, a compliance-relevant field), treat this tier's design as a draft to double-check rather than the final call.
