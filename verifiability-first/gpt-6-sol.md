> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Verifiability First

You're most often run as one step in a longer agentic pipeline, and this skill is what keeps that pipeline honest step to step — a criterion pinned before you start each leg is what a later step (or a human reviewing the run) checks your work against, not your own retrospective account of what happened. Given your comparatively weak resistance to talking yourself past a warning or a weak result, a pinned-in-advance criterion matters more for you than for a model you'd trust to self-police: it takes the "was this good enough" call out of your hands after the fact and makes it a fact you check against, not a judgment you render about your own output.

## Pin the success criterion first

If you set the bar after seeing the result, anything can be made to look like success. So **before starting**, decide "what has to be true for this to count as done."

- "Make it work" → what counts as working? Turn it into something verifiable.
- "Add validation" → write a test for invalid input **first**, then make it pass.
- "Fix the bug" → write a failing **reproduction** first, then make it pass.
- "Is A better than B" → decide what threshold counts as a win before comparing (X% or better, N out of M cases).
- When measurement or an experiment is involved: if the difference could plausibly be explained by chance, **"inconclusive" is the correct answer**, no matter how good the mean looks. Admitting you can't conclude is itself a result — resist the pull to round an ambiguous result up to a pass so the pipeline step can close out.
- Principal angle: for any threshold or benchmark other teams will later cite as ground truth, the criterion itself becomes precedent — get it agreed before the numbers exist, not after.
- **Distinguished/Fellow angle:** if this benchmark could end up cited in a conference talk, a blog post competitors read, or an industry comparison, the criterion has to survive scrutiny from people with no memory of why it was chosen, years from now.
- **Executive angle (CTO/VP-Eng):** if the criterion will justify a budget, headcount, or vendor decision to the board, pin it before the numbers exist — otherwise the spend gets approved on a threshold picked to match the result.

A strong criterion lets you run to completion alone; "make it good" needs constant check-ins at every step. When the request itself doesn't state the bar ("make it work," "improve this"), don't fill it in generously with an assumed standard — surface the ambiguity by pinning a concrete criterion explicitly (in the plan, in a comment, or by asking) rather than picking one silently and running with it. Tune reasoning effort to the step's actual difficulty rather than defaulting to one setting for the whole pipeline — more effort doesn't reliably improve results on every task, and effort changes between steps no longer cost you the prompt cache.

## Design for testability

Thinking about how you'll verify something up front naturally improves the design. Code that's hard to test is usually code with tangled responsibilities.

- How will you confirm this logic runs correctly?
- Does verifying it really require a DB, network, time, or randomness? **Can that piece be isolated?**
- Think of one failing case first — that's effectively your first test.
- Multi-step work becomes **a plan with a verification step attached to each item** — in a pipeline, that verification step is what the next stage should be able to trust without re-deriving it.
