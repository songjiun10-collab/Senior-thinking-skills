> Tuned for Claude Fable 5.1 (and Claude Mythos 5.1, which shares its Anthropic prompting guide). See SKILL.md for the model index.

# Measure First

Don't optimize without evidence. "This seems slow" is a guess, not a problem — and optimization that starts from a guess usually just adds complexity with no felt improvement.

## Order: measure → pinpoint → fix → re-measure

- Start with a **reproducible measurement** (profiler, timing logs, Lighthouse, real-user metrics) — don't point at "this is the problem" from a hunch
- Pinpoint **exactly one** bottleneck: an N+1 query, a cache miss, bundle size. Fix several things at once and you can't tell what actually helped
- After fixing, **re-measure the same way**. The improvement has to beat measurement noise to count as real
- Don't say "it's faster now" without a re-measurement
- State this as the goal and the order of operations, not a rigid script to follow line by line — but the order itself (measure, then pinpoint, then fix, then re-measure) is the one place in this skill that's genuinely a sequence, not a plan to improvise around. Skipping straight to a fix defeats the point regardless of how good your reasoning about the fix is.

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

## Calibration notes

- **Narrate as you go during profiling and diagnosis.** A performance investigation is exactly the kind of long, exploratory loop where you tend to go quiet by default — say what you're measuring, what came back, and what you're pinpointing next, especially if someone is waiting on the diagnosis.
- This skill covers long-horizon performance work well without hand-holding — if the investigation spans many profiling rounds, keep applying the same measure → pinpoint → fix → re-measure order rather than needing it re-specified at each step.
