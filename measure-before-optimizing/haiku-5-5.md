> Tuned for Claude Haiku 5.5. Source: Anthropic prompting guide (prompting-claude-haiku-5-5). Body carried from the Sonnet file; the calibration section is Haiku-specific. See SKILL.md for the model index.

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

## Calibration notes

- If a request only implies a performance concern ("this feels sluggish," "can we speed this up") without explicitly asking for profiling, still apply the measure-first order — don't take the absence of an explicit "profile it" as license to jump straight to a fix. State the plan (measure → pinpoint → fix → re-measure) up front so it's an explicit part of the instruction you're following, not something left to infer.

## Calibration (Anthropic official prompting guide, Haiku 5.5)

- **Effort**: `low`, `medium` (default), `high`, `xhigh`, `max`. At `low`, long agent prompts see more skipped searches, early stops, and skipped checks. Thinking can be turned off with `{type: "disabled"}` at `low`/`medium`/`high` only; at `xhigh`/`max` it is a 400.
- **Search**: send today's date, and add a nudge that training data may be stale for records, prices, versions and "latest". Avoid blanket "search for everything" instructions; they cause searches on prompts that need none.
- **JSON output with your own tools**: with thinking off, the model can skip a needed tool call. Use adaptive thinking, drop `output_config.format` on tool-calling requests, or force the call with `tool_choice`.
- **Early stopping** (long agent prompts at `low`): add an explicit keep-working line and a no-extra-scope line.
- **Coding verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn.
- **Chatbots**: add an explicit rules-hold-for-the-whole-conversation line to resist pressure from users.
- **Safeguard refusals**: categories `cyber`, `frontier_llm`, `bio`, `general_harms`. No server-side fallback, so handle `stop_reason: "refusal"` in the client.
