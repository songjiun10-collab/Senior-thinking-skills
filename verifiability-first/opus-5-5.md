> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Verifiability First

## Pin the success criterion first

If you set the bar after seeing the result, anything can be made to look like success. So **before starting**, decide "what has to be true for this to count as done."

- "Make it work" → what counts as working? Turn it into something verifiable.
- "Add validation" → write a test for invalid input **first**, then make it pass.
- "Fix the bug" → write a failing **reproduction** first, then make it pass.
- "Is A better than B" → decide what threshold counts as a win before comparing (X% or better, N out of M cases).
- When measurement or an experiment is involved: if the difference could plausibly be explained by chance, **"inconclusive" is the correct answer**, no matter how good the mean looks. Admitting you can't conclude is itself a result.
- Principal angle: for any threshold or benchmark other teams will later cite as ground truth, the criterion itself becomes precedent — get it agreed before the numbers exist, not after.
- **Distinguished/Fellow angle:** if this benchmark could end up cited in a conference talk, a blog post competitors read, or an industry comparison, the criterion has to survive scrutiny from people with no memory of why it was chosen, years from now.
- **Executive angle (CTO/VP-Eng):** if the criterion will justify a budget, headcount, or vendor decision to the board, pin it before the numbers exist — otherwise the spend gets approved on a threshold picked to match the result.

A strong criterion lets you run to completion alone; "make it good" needs constant check-ins at every step. This is the highest-leverage habit for you specifically: you already self-verify well once work is underway, so the value isn't in adding more re-checks after the fact — it's in pinning the criterion *before* results exist, so there's nothing to rationalize around later. Thinking is always on and effort defaults to `medium`; when the criterion itself needs real deliberation — a benchmark threshold, a "better" that has to be defined precisely — set effort explicitly higher for that step, since a low effort setting won't shrink your output but will shrink how carefully the bar gets chosen.

## Design for testability

Thinking about how you'll verify something up front naturally improves the design. Code that's hard to test is usually code with tangled responsibilities.

- How will you confirm this logic runs correctly?
- Does verifying it really require a DB, network, time, or randomness? **Can that piece be isolated?**
- Think of one failing case first — that's effectively your first test.
- Multi-step work becomes **a plan with a verification step attached to each item**.
- When a verification step is a quick, concrete check — run the failing test, grep for the actual call site, read the output — do it directly instead of delegating it to a subagent. Confirming the criterion is the whole point here; a delegation round-trip is usually slower than checking it yourself, and you still need to look at the real result either way.
