> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Review With Fresh Eyes

> **Difference from `adversarial-review`**: this is a post-hoc pass over **finished work**. `adversarial-review` interrogates an **in-flight decision** with a disproving bias, while reversing it is still cheap. If an irreversible decision is on the line, reach for `adversarial-review` before the work is done, not after.

Review code with the same context you wrote it in, and you carry the same blind spots into the review. You know why you wrote it that way, so the odd part doesn't look odd. Most of a review's value comes from **looking at it without that knowledge.**

You're the fastest, cheapest tier here, best fit for narrow, well-specified checks rather than an open-ended judgment-heavy review. A full fresh-eyes pass over a large or ambiguous diff — weighing spec compliance, code quality, and a shared-interface's blast radius all at once — is closer to the demanding, judgment-heavy work this tier isn't the best fit for. Where you're asked to do exactly that, flag that a stronger model or a human should take the full pass; where you're asked to check one narrow, well-defined thing (does this diff touch file X, does this function handle a null return, does this match the stated requirement's literal wording), the guidance below applies directly.

## How to shed the context

- **Look only at the result.** Set aside why it turned out this way; read only the diff and the final code.
- Ask the questions a first-time reader would ask: when is this variable null? What does this function return? Why is this condition here?
- **Go back to the original requirement and check against it.** Is what you built what was asked for? Did it drift along the way? Reread the original requirement's exact wording here rather than your paraphrase of it.

## Two separate axes

Mix two kinds of judgment into one pass and you miss both. Keep them separate.

1. **Spec compliance** — did you actually do what was asked? What requirements are missing? What did you do that wasn't asked for?
2. **Code quality** — naming, structure, duplication, error handling, boundary conditions

On a change to a shared interface, add a third lens: **who else calls this, and does the review still hold from their vantage point.** Enumerating every caller across a large codebase is exactly the kind of open-ended search this tier isn't the strongest fit for — if the caller list is long or unclear, say so explicitly rather than reporting a partial list as complete.

## Verify it yourself

- Don't trust a report or your memory — **actually run the tests**.
- Actually read the diff. What you think you fixed and what actually changed can differ.
- Can't confirm something from the diff? **Mark it unconfirmed.** Don't wave it through — and don't round "probably fine" up to "confirmed" in the write-up; state exactly what was and wasn't checked. At this tier, "unconfirmed" is often the right and complete answer for anything outside the narrow question you were actually given — hand it back rather than stretching to cover ground the request didn't ask you to cover.

## No self-censoring

Don't pre-filter findings before the review with "this is probably fine." Even something you think is a false positive goes on the list — judge it later; whoever reads the report decides what to do with each one.
