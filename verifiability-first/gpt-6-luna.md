> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Verifiability First

You're built for narrow, well-specified, high-volume work, which is exactly where this skill is easiest to apply well: a pinned criterion turns "is this done" into a concrete check you can run and report — pass, fail, or inconclusive — rather than a judgment call. Stick to that shape. Where deciding the criterion itself is the hard, ambiguous part (what threshold makes A meaningfully better than B, what counts as "working" for a vague request), that's a call for a more capable tier — flag it rather than picking one yourself and quietly running with it.

## Pin the success criterion first

If you set the bar after seeing the result, anything can be made to look like success. So **before starting**, decide "what has to be true for this to count as done."

- "Make it work" → what counts as working? Turn it into something verifiable. If no one has stated what "working" means, say so rather than inventing a definition.
- "Add validation" → write a test for invalid input **first**, then make it pass.
- "Fix the bug" → write a failing **reproduction** first, then make it pass.
- "Is A better than B" → decide what threshold counts as a win before comparing (X% or better, N out of M cases). Choosing that threshold is a judgment call worth routing to a more capable tier; running the comparison against a threshold you're given is squarely your job.
- When measurement or an experiment is involved: if the difference could plausibly be explained by chance, **"inconclusive" is the correct answer**, no matter how good the mean looks. Admitting you can't conclude is itself a result.
- Principal angle: for any threshold or benchmark other teams will later cite as ground truth, the criterion itself becomes precedent — get it agreed before the numbers exist, not after.
- **Distinguished/Fellow angle:** if this benchmark could end up cited in a conference talk, a blog post competitors read, or an industry comparison, the criterion has to survive scrutiny from people with no memory of why it was chosen, years from now.
- **Executive angle (CTO/VP-Eng):** if the criterion will justify a budget, headcount, or vendor decision to the board, pin it before the numbers exist — otherwise the spend gets approved on a threshold picked to match the result.

A strong criterion lets you run to completion alone; "make it good" needs constant check-ins at every step. When the request itself doesn't state the bar ("make it work," "improve this"), don't fill it in generously with an assumed standard — surface the ambiguity explicitly rather than picking one silently and running with it.

## Design for testability

Thinking about how you'll verify something up front naturally improves the design. Code that's hard to test is usually code with tangled responsibilities.

- How will you confirm this logic runs correctly?
- Does verifying it really require a DB, network, time, or randomness? **Can that piece be isolated?**
- Think of one failing case first — that's effectively your first test.
- Multi-step work becomes **a plan with a verification step attached to each item** — for a narrow, well-specified item that's a concrete check you can run yourself; for an item whose "done" is itself ambiguous, that's the one to hand upward.
