> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Measure First

Don't optimize without evidence. "This seems slow" is a guess, not a problem — and optimization that starts from a guess usually just adds complexity with no felt improvement.

## Order: measure → pinpoint → fix → re-measure

- Start with a **reproducible measurement** (profiler, timing logs, Lighthouse, real-user metrics) — don't point at "this is the problem" from a hunch. Run the profiler or read the timing logs directly when the tooling is already available; that's the faster path, and there's no need to hand this off to a subagent by default.
- Pinpoint **exactly one** bottleneck: an N+1 query, a cache miss, bundle size. Fix several things at once and you can't tell what actually helped.
- After fixing, **re-measure the same way**. The improvement has to beat measurement noise to count as real.
- Don't say "it's faster now" without a re-measurement. State up front what "done" means for this pass — the re-measurement showing an improvement past noise — so the loop has a stated end instead of continuing indefinitely or stopping early on a feeling.

## Common traps

- Reaching for memoization or a cache before profiling — a cache buys you a new cost: invalidation bugs.
- Bundling several optimizations into one commit, so nobody can tell what worked.
- "It's a neutral change, leave it in for now" — if it didn't help, revert it; don't accumulate code with no justification.
- Declaring "it's fast now" with no guardrail (monitoring, a benchmark test) against regression.
- Turning the fix step into more than the measurement justified — a single N+1 query or a single cache miss needs the one targeted fix, not a new caching abstraction layer built "while we're in here."

## Is it even worth optimizing

If you measured and the bottleneck is negligible against the overall path, it's not something to optimize — it's something to **skip**. Performance is a budget: spend it only where you have evidence it's actually felt.

- If the hot path sits inside a shared library or service other teams call, weigh the fix against **their** traffic profile too, not just your one call site — a change that helps your caller can quietly regress someone else's.
- **Distinguished/Fellow angle:** A technique that earns its place here and could become the org's default (or get open-sourced, blogged about, or presented externally) needs evidence that holds beyond this one workload — a multi-year bet on a benchmark from a single call site is how false optimizations become doctrine.
- **Executive angle (CTO/VP-Eng):** Before a fix that adds infrastructure (bigger instances, a caching layer, a new managed service) ships as the default, weigh its recurring bill against the engineer-hours it saves — that's the number a CFO asks for before approving the spend increase.

## Calibration notes

- **Set explicit completion criteria and an exploration scope before starting a performance investigation.** State what counts as "found" (a specific, reproducible bottleneck backed by a profile or trace) and what's in bounds to check (which services, which code paths) before diagnosing. Left open-ended, this tier tends to stay tentative about calling a diagnosis finished rather than running further than the task needs — a stated bar and scope fixes both.
- **Act on the measurement rather than asking whether to proceed.** Given a profile or a timing log, move to pinpointing and fixing the one bottleneck it points to rather than pausing to confirm the plan; infer the goal from the reported slowness and the data gathered, and flag only genuine ambiguity (e.g., which of two comparably-sized bottlenecks to fix first).
- **No need for extra "make sure you verify this" instructions.** The re-measure step is already built into the order above and this tier runs it without being separately told to double-check.
- **State explicitly when a wide profiling sweep should be split across subagents** — checking several services or call paths for the same class of bottleneck is parallel work. Left unstated, the default here leans toward doing the whole sweep directly even when splitting it out would finish faster.
- **Write the measurement and the fix up in plain, direct prose** — a before/after number and what changed, not a "not X, but Y" framing. Save bullets for genuinely parallel items (the common-traps and warning-sign lists above); a single measurement result reads better as a sentence.
