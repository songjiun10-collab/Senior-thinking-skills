---
name: measure-before-optimizing
description: Verify a bottleneck exists before touching performance. Use before any caching, memoization, query rewrite, algorithm swap, or "this seems slow" change; when a spec sets a performance target or Core Web Vitals threshold; when a user reports slowness; or when a PR bundles a performance claim with no before/after number. Skip for a fix where the bottleneck is already obvious from the code itself (e.g. an accidental O(n²) on a hot path).
---

# Measure First

Don't optimize without evidence. "This seems slow" is a guess, not a problem — and optimization that starts from a guess usually just adds complexity with no felt improvement.

## Order: measure → pinpoint → fix → re-measure

- Start with a **reproducible measurement** (profiler, timing logs, Lighthouse, real-user metrics) — don't point at "this is the problem" from a hunch
- Pinpoint **exactly one** bottleneck: an N+1 query, a cache miss, bundle size. Fix several things at once and you can't tell what actually helped
- After fixing, **re-measure the same way**. The improvement has to beat measurement noise to count as real
- Don't say "it's faster now" without a re-measurement

## Common traps

- Reaching for memoization or a cache before profiling — a cache buys you a new cost: invalidation bugs
- Bundling several optimizations into one commit, so nobody can tell what worked
- "It's a neutral change, leave it in for now" — if it didn't help, revert it; don't accumulate code with no justification
- Declaring "it's fast now" with no guardrail (monitoring, a benchmark test) against regression

## Is it even worth optimizing

If you measured and the bottleneck is negligible against the overall path, it's not something to optimize — it's something to **skip**. Performance is a budget: spend it only where you have evidence it's actually felt.

- If the hot path sits inside a shared library or service other teams call, weigh the fix against **their** traffic profile too, not just your one call site — a change that helps your caller can quietly regress someone else's.
- **Distinguished/Fellow angle:** A technique that earns its place here and could become the org's default (or get open-sourced, blogged about, or presented externally) needs evidence that holds beyond this one workload — a multi-year bet on a benchmark from a single call site is how false optimizations become doctrine.
- **Executive angle (CTO/VP-Eng):** Before a fix that adds infrastructure (bigger instances, a caching layer, a new managed service) ships as the default, weigh its recurring bill against the engineer-hours it saves — that's the number a CFO asks for before approving the spend increase.
