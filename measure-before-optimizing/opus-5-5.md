> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Measure First

Don't optimize without evidence. "This seems slow" is a guess, not a problem — and optimization that starts from a guess usually just adds complexity with no felt improvement.

## Order: measure → pinpoint → fix → re-measure

- Start with a **reproducible measurement** (profiler, timing logs, Lighthouse, real-user metrics) — don't point at "this is the problem" from a hunch. Run the profiler or read the timing logs directly yourself when the codebase and tooling are already in front of you; that's usually faster than spinning up a subagent to do it, even though delegating a research-shaped side-task can feel like the natural move.
- Pinpoint **exactly one** bottleneck: an N+1 query, a cache miss, bundle size. Fix several things at once and you can't tell what actually helped
- After fixing, **re-measure the same way**. The improvement has to beat measurement noise to count as real
- Don't say "it's faster now" without a re-measurement

## Common traps

- Reaching for memoization or a cache before profiling — a cache buys you a new cost: invalidation bugs
- Bundling several optimizations into one commit, so nobody can tell what worked
- "It's a neutral change, leave it in for now" — if it didn't help, revert it; don't accumulate code with no justification
- Declaring "it's fast now" with no guardrail (monitoring, a benchmark test) against regression
- Turning the fix step into more than the measurement justified — a single N+1 query or a single cache miss doesn't need a new abstraction layer or a generalized caching framework, it needs the one targeted fix

## Is it even worth optimizing

If you measured and the bottleneck is negligible against the overall path, it's not something to optimize — it's something to **skip**. Performance is a budget: spend it only where you have evidence it's actually felt.

- If the hot path sits inside a shared library or service other teams call, weigh the fix against **their** traffic profile too, not just your one call site — a change that helps your caller can quietly regress someone else's.
- **Distinguished/Fellow angle:** A technique that earns its place here and could become the org's default (or get open-sourced, blogged about, or presented externally) needs evidence that holds beyond this one workload — a multi-year bet on a benchmark from a single call site is how false optimizations become doctrine.
- **Executive angle (CTO/VP-Eng):** Before a fix that adds infrastructure (bigger instances, a caching layer, a new managed service) ships as the default, weigh its recurring bill against the engineer-hours it saves — that's the number a CFO asks for before approving the spend increase.

## Calibration notes

- **Set effort explicitly when the measurement or diagnosis is non-trivial** — profiling a genuinely elusive bottleneck (intermittent latency, a cross-service slowdown) deserves more depth than your medium default gives it unmet.
- **Don't add a second round of "let me double-check this measurement is real"** beyond the re-measure step already in the order above — you already verify your own reasoning well; a redundant confirmation pass here is wasted latency, not extra rigor.
- **Resist the pull to over-build the fix.** Once you've pinpointed the one bottleneck, ship the one targeted fix. Don't add a generic caching layer, a configurable strategy pattern, or unrequested flexibility around it — that's scope the measurement never asked for.
