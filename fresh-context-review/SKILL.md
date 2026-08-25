---
name: fresh-context-review
description: Review code with the assumptions of the person who wrote it deliberately stripped away. Use after finishing an implementation and before declaring it done, before opening a PR, or when asked to review code that you (or the same session) just wrote. Also use when a change touched more files than expected or when the implementation drifted from the original plan.
---

# Review With Fresh Eyes

> **Difference from `adversarial-review`**: this is a post-hoc pass over **finished work**. `adversarial-review` interrogates an **in-flight decision** with a disproving bias, while reversing it is still cheap. If an irreversible decision is on the line, reach for `adversarial-review` before the work is done, not after.

Review code with the same context you wrote it in, and you carry the same blind spots into the review. You know why you wrote it that way, so the odd part doesn't look odd. Most of a review's value comes from **looking at it without that knowledge.**

## How to shed the context

- **Look only at the result.** Set aside why it turned out this way; read only the diff and the final code
- Ask the questions a first-time reader would ask: when is this variable null? What does this function return? Why is this condition here?
- **Go back to the original requirement and check against it.** Is what you built what was asked for? Did it drift along the way?

## Two separate axes

Mix two kinds of judgment into one pass and you miss both. Keep them separate.

1. **Spec compliance** — did you actually do what was asked? What requirements are missing? What did you do that wasn't asked for?
2. **Code quality** — naming, structure, duplication, error handling, boundary conditions

On a change to a shared interface, add a third lens: **who else calls this, and does the review still hold from their vantage point** — not just the caller you happened to test against.

- **Distinguished/Fellow angle:** For a change likely to set precedent across the whole org or outlive its author's tenure, review it as the person who inherits it in five years would — with none of the context, only what's written down.
- **Executive angle (CTO/VP-Eng):** For a change to a system a customer, regulator, or partner depends on, review it for what happens when it fails in production — who gets paged, what SLA or contract is breached, what it costs to remediate — not just whether the code itself is well-structured.

## Verify it yourself

- Don't trust a report or your memory — **actually run the tests**
- Actually read the diff. What you think you fixed and what actually changed can differ
- Can't confirm something from the diff? **Mark it unconfirmed.** Don't wave it through

## No self-censoring

Don't pre-filter findings before the review with "this is probably fine." Even something you think is a false positive goes on the list — judge it later. Pre-grading buries the real problems along with the noise.
