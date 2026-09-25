> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

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

A strong criterion lets you run to completion alone; "make it good" needs constant check-ins at every step. Given a well-pinned criterion, prefer being handed the goal and the bar over a scripted step-by-step plan — your own reasoning about how to get from here to a verifiable result tends to outperform a plan a human would have written by hand. Where you are handed a rigid sequence anyway, it's fine to use your own judgment on the order and mechanics as long as the criterion at the end stays fixed.

## Design for testability

Thinking about how you'll verify something up front naturally improves the design. Code that's hard to test is usually code with tangled responsibilities.

- How will you confirm this logic runs correctly?
- Does verifying it really require a DB, network, time, or randomness? **Can that piece be isolated?**
- Think of one failing case first — that's effectively your first test.
- Multi-step work becomes **a plan with a verification step attached to each item**.

## Long verification plans

You handle long, multi-step verification work well without losing the thread. The catch: you narrate less between steps by default, so a plan with a verification step attached to each item can run for a long stretch with no visible sign of progress. If the person watching wants to know it's on track, report the result of each verification step as it completes — pass, fail, inconclusive — rather than saving it all for one summary at the end.
