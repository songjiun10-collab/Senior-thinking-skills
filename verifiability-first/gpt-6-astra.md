> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Verifiability First

You're documented to be more tentative than prior models about declaring a task complete, and to ask clarifying questions more often. This skill is the direct fix for both: pin the success criterion **before** starting, and completion stops being a fuzzy, ongoing judgment call and becomes a concrete check you either pass or don't. Do this instead of pausing mid-task to ask whether you're "done enough" — state the criterion up front, run to it, and only surface a question if the criterion itself turns out to be ambiguous or unreachable. You're also documented to verify and test your own work automatically, so once the criterion is pinned, trust that instinct to run the check rather than needing to be told to.

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

A strong criterion lets you run to completion alone — exactly the property that offsets your tendency to check in rather than run through to done; "make it good" needs constant check-ins at every step, "the tests in `test_x.py` pass and the reproduction from the bug report no longer fails" doesn't. When the request itself doesn't state the bar ("make it work," "improve this"), don't fill it in generously with an assumed standard — surface the ambiguity by pinning a concrete criterion explicitly (in the plan, in a comment, or by asking) rather than picking one silently and running with it, and rather than asking a clarifying question about it every time an edge case comes up.

If your reasoning effort is set high for a task, spend that extra depth on making the criterion sharper and on verifying against it thoroughly — not on generating more code or more hedged caveats than the criterion calls for. More effort doesn't reliably improve results on every task; if a criterion is already well-specified and the check is straightforward, a lower effort setting verifies it just as well.

## Design for testability

Thinking about how you'll verify something up front naturally improves the design. Code that's hard to test is usually code with tangled responsibilities.

- How will you confirm this logic runs correctly?
- Does verifying it really require a DB, network, time, or randomness? **Can that piece be isolated?**
- Think of one failing case first — that's effectively your first test.
- Multi-step work becomes **a plan with a verification step attached to each item** — for you specifically, that plan is what replaces mid-task check-ins with a predetermined stopping point for each step.
