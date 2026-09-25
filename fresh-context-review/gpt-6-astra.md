> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Review With Fresh Eyes

> **Difference from `adversarial-review`**: this is a post-hoc pass over **finished work**. `adversarial-review` interrogates an **in-flight decision** with a disproving bias, while reversing it is still cheap. If an irreversible decision is on the line, reach for `adversarial-review` before the work is done, not after.

Review code with the same context you wrote it in, and you carry the same blind spots into the review. You know why you wrote it that way, so the odd part doesn't look odd. Most of a review's value comes from **looking at it without that knowledge.**

## Fix the scope before you start, so you know when the review is done

You're more likely than earlier models to stay tentative about calling a review finished, and to check in mid-review rather than carrying it to a conclusion on your own. Head that off by stating up front what this review covers (which files, which diff, which of the two axes below) and what "done" looks like — every changed file walked once, tests actually run, findings written down. Then run it to that stated end without re-confirming along the way, unless something you find genuinely changes the scope (a file you didn't know was touched, a test that doesn't exist).

## How to shed the context

- **Look only at the result.** Set aside why it turned out this way; read only the diff and the final code.
- Ask the questions a first-time reader would ask: when is this variable null? What does this function return? Why is this condition here?
- **Go back to the original requirement and check against it.** Is what you built what was asked for? Did it drift along the way? Reread the original requirement's exact wording here rather than your paraphrase of it — an underspecified original ask tends to get built to its literal words, and a drift is easiest to miss if the review also works from a loosened paraphrase instead of the actual text.

## Two separate axes

Mix two kinds of judgment into one pass and you miss both. Keep them separate.

1. **Spec compliance** — did you actually do what was asked? What requirements are missing? What did you do that wasn't asked for?
2. **Code quality** — naming, structure, duplication, error handling, boundary conditions

On a change to a shared interface, add a third lens: **who else calls this, and does the review still hold from their vantage point** — not just the caller you happened to test against.

- **Distinguished/Fellow angle:** For a change likely to set precedent across the whole org or outlive its author's tenure, review it as the person who inherits it in five years would — with none of the context, only what's written down.
- **Executive angle (CTO/VP-Eng):** For a change to a system a customer, regulator, or partner depends on, review it for what happens when it fails in production — who gets paged, what SLA or contract is breached, what it costs to remediate — not just whether the code itself is well-structured.

## Verify it yourself — this is already your instinct, trust it

You test and check your own work without being told to more than earlier models did. Don't add a redundant explicit "now go verify this" instruction on top of the checklist below — it's already what this checklist is. What matters is doing it once, thoroughly:

- Don't trust a report or your memory — **actually run the tests**.
- Actually read the diff. What you think you fixed and what actually changed can differ.
- Can't confirm something from the diff? **Mark it unconfirmed.** Don't wave it through — and don't round "probably fine" up to "confirmed" in the write-up; state exactly what was and wasn't checked.

## No self-censoring

Don't pre-filter findings before the review with "this is probably fine." Even something you think is a false positive goes on the list — judge it later. Pre-grading buries the real problems along with the noise. This isn't in tension with your own good judgment about what's actually safe — it's specifically about not letting that judgment run *before* the findings are on paper, only after.

## Watch your own budget on a large diff

You track your remaining context budget as you go. On a review that touches many files, use that awareness to decide early whether to review the whole diff in one pass or split it — better to notice you're running short with half the diff still unread and adjust than to have the back half of the review get thinner without deciding to let it.

## Write the findings plainly

State each finding directly — what's wrong and where — rather than through a hedge or a contrastive frame. Skip a bulleted list for findings that aren't actually parallel to each other; a short paragraph per finding is often clearer than forcing dissimilar issues into one list format. Avoid "it's worth noting," "delve into," or manufacturing a label for an issue that doesn't need one — name the concrete problem.
