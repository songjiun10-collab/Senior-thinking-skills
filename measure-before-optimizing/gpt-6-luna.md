> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Measure First

Don't optimize without evidence. "This seems slow" is a guess, not a problem — and optimization that starts from a guess usually just adds complexity with no felt improvement.

## Order: measure → pinpoint → fix → re-measure

- Start with a **reproducible measurement** (profiler, timing logs, Lighthouse, real-user metrics) — don't point at "this is the problem" from a hunch.
- Pinpoint **exactly one** bottleneck: an N+1 query, a cache miss, bundle size. Fix several things at once and you can't tell what actually helped.
- After fixing, **re-measure the same way**. The improvement has to beat measurement noise to count as real.
- Don't say "it's faster now" without a re-measurement.

## Common traps

- Reaching for memoization or a cache before profiling — a cache buys you a new cost: invalidation bugs.
- Bundling several optimizations into one commit, so nobody can tell what worked.
- "It's a neutral change, leave it in for now" — if it didn't help, revert it; don't accumulate code with no justification.
- Declaring "it's fast now" with no guardrail (monitoring, a benchmark test) against regression.

## Is it even worth optimizing

If you measured and the bottleneck is negligible against the overall path, it's not something to optimize — it's something to **skip**. Performance is a budget: spend it only where you have evidence it's actually felt.

- If the hot path sits inside a shared library or service other teams call, weigh the fix against **their** traffic profile too, not just your one call site — a change that helps your caller can quietly regress someone else's.
- **Distinguished/Fellow angle:** A technique that earns its place here and could become the org's default (or get open-sourced, blogged about, or presented externally) needs evidence that holds beyond this one workload — a multi-year bet on a benchmark from a single call site is how false optimizations become doctrine.
- **Executive angle (CTO/VP-Eng):** Before a fix that adds infrastructure (bigger instances, a caching layer, a new managed service) ships as the default, weigh its recurring bill against the engineer-hours it saves — that's the number a CFO asks for before approving the spend increase.

## Calibration notes

- If a request only implies a performance concern without explicitly asking for profiling, still apply the measure-first order rather than jumping to a fix.
- **This tier fits one bounded leg of a performance investigation, not the whole judgment call.** Use it to run a given profiler command and report the numbers, to check one specific query for an N+1 pattern, or to re-run a fixed benchmark and compare before/after — well-specified, narrow work. Diagnosing an ambiguous or cross-service slowdown from scratch, or deciding whether a bottleneck is worth fixing at all, needs more headroom than this tier is built for; hand that judgment call to a stronger tier and use this one for the mechanical measurement steps around it.
- Keep reasoning effort low for this kind of bounded, well-specified check — there's little to gain from pushing it higher on a task that's already narrow, and it adds latency without improving the parts of the job this tier isn't meant to carry anyway.
