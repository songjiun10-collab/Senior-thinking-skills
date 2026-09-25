> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

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

- If a request only implies a performance concern ("this feels sluggish," "can we speed this up") without explicitly asking for profiling, still apply the measure-first order — state the plan (measure → pinpoint → fix → re-measure) up front so it's explicit rather than left to infer.
- **Tune reasoning effort to the diagnosis, and don't default to the top setting.** A one-line N+1 fix doesn't need the same effort as chasing an intermittent cross-service slowdown — raise it for the genuinely tangled cases and keep it lower for routine ones; a higher setting costs more without a guaranteed matching gain, so measure it rather than defaulting to max.
- This tier is well-suited as the default for a repeated or pipelined profiling pass (checking the same class of bottleneck across many services) given its cost profile — but for a single ambiguous, high-stakes performance regression, treat its diagnosis as a first pass rather than the final word, and keep a second check in place before a costly infra change (a new cache layer, bigger instances) ships on its recommendation alone.
