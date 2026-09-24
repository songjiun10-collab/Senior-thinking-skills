---
name: verifiability-first
description: Turn the task into something verifiable and declare the success criterion before seeing results. Use when the request is vague about "done" ("make it work", "improve this"), when writing tests, when fixing a bug (write the failing reproduction first), or when comparing two approaches. Critical before any measurement or benchmark, where deciding the bar after seeing the numbers guarantees a "success".
---

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

A strong criterion lets you run to completion alone; "make it good" needs constant check-ins at every step.

## Design for testability

Thinking about how you'll verify something up front naturally improves the design. Code that's hard to test is usually code with tangled responsibilities.

- How will you confirm this logic runs correctly?
- Does verifying it really require a DB, network, time, or randomness? **Can that piece be isolated?**
- Think of one failing case first — that's effectively your first test.
- Multi-step work becomes **a plan with a verification step attached to each item**.

## Model notes

- **Haiku 4.5** — Thinking needs an explicit budget — without one it may skip straight to code instead of reasoning out the success criterion first.
- **Sonnet 5** — Default — apply as written.
- **Opus 5** — Already self-verifies well once it's working — the leverage here is pinning the criterion *before* results exist, not adding extra re-checks after.
- **Opus 5.5** — Same self-verification strength as Opus 5; effort defaults to medium, so set it explicitly when the criterion needs real deliberation (e.g. a benchmark threshold).
- **Fable 5.1** — Runs long, low-visibility stretches on multi-step verification plans — ask for a status update per step if you want visibility before it's all done.
