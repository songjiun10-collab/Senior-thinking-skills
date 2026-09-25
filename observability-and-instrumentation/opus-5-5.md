> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

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
- Propagate trace context across every async boundary. Add manual spans only around meaningful work, not every function — resist the pull to instrument everything just because it's easy to add a span; a span with no diagnostic question behind it is noise, not coverage.
- Alert on symptoms users feel, not merely causes. Every page must be actionable, have a threshold/duration rationale, and link to a short runbook.
- Telemetry export must not block the user path; bound queues and timeouts, and define what happens when the collector is unavailable.

## Verify the telemetry

Instrumentation is code and can be wrong. Before calling it complete, work through this once, directly:

1. Induce a representative failure in a safe environment and locate it using telemetry alone.
2. Confirm structured fields, correlation IDs, redaction, and entry-point attribution in actual output.
3. Send test traffic and inspect metric series, bounded labels, and sane values.
4. Follow one request end-to-end and check for broken spans.
5. Fire each new alert once and verify the destination and runbook link.
6. Compare event rate, series count, payload size, and request overhead before and after the change.
7. Exercise retry, timeout, cancellation, malformed-input, and high-cardinality paths; confirm they do not create misleading duplicates or overload the exporter.

Run this yourself — grep the actual log output, read the metric series directly — rather than dispatching it to a subagent by default. It's a bounded, mechanical check against a live system, and doing it in-session is usually faster than briefing and waiting on a delegate.

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

- **Effort for tracing a hard-to-explain incident.** Effort defaults to `medium`, which in Anthropic's testing matched or beat Opus 5 at `high`; thinking stays on regardless, and effort is the knob that actually changes depth. For a genuinely tangled cross-service trace, if a higher level has shown a gain, the caller sets it for that request — it can't be raised mid-turn.
- **Run the verification gate once, thoroughly, and stop.** Opus 5 guidance (still applicable to 5.5) says added verification instructions cause over-verification; re-confirming "yes the redaction really worked" three separate times past the checklist above is wasted latency, not extra safety.
- **Watch for scope expansion in the instrumentation itself** (documented for Opus 5, carried over to 5.5) — a generic telemetry abstraction layer, a configurable exporter framework, or schema flexibility nobody asked for. The rules above already specify what's needed; add only that.
- **A refusal on this skill's territory may be a false positive.** Instrumenting for security incidents, auth failures, or abuse detection is legitimate engineering work; this model runs cybersecurity classifiers that target high-risk dual-use activity, and a decline arrives as `stop_reason: "refusal"`. If a request in this space gets refused, check whether it's actually a defensive/operational task before assuming it's blocked for cause.
