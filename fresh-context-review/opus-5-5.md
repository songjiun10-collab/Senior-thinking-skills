> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

# Review With Fresh Eyes

> **Difference from `adversarial-review`**: this is a post-hoc pass over **finished work**. `adversarial-review` interrogates an **in-flight decision** with a disproving bias, while reversing it is still cheap. If an irreversible decision is on the line, reach for `adversarial-review` before the work is done, not after.

Review code with the same context you wrote it in, and you carry the same blind spots into the review. You know why you wrote it that way, so the odd part doesn't look odd. Most of a review's value comes from **looking at it without that knowledge.**

## How to shed the context

- **Look only at the result.** Set aside why it turned out this way; read only the diff and the final code.
- Ask the questions a first-time reader would ask: when is this variable null? What does this function return? Why is this condition here?
- **Go back to the original requirement and check against it.** Is what you built what was asked for? Did it drift along the way?
- Do this pass yourself, directly, by reading the diff — don't reach for a subagent to do a plain diff read for you. Delegation has a real pull here, including for legs a direct read would settle just as fast; a fresh-eyes review of your own recent work is exactly the kind of task where reading it yourself is both faster and no less thorough.

## Two separate axes

Mix two kinds of judgment into one pass and you miss both. Keep them separate.

1. **Spec compliance** — did you actually do what was asked? What requirements are missing? What did you do that wasn't asked for? This is also where to catch your own over-engineering instinct: flag anything you added that wasn't in the requirement — an extra config option, an abstraction layer, a file nobody asked for — as a finding, not a bonus.
2. **Code quality** — naming, structure, duplication, error handling, boundary conditions

On a change to a shared interface, add a third lens: **who else calls this, and does the review still hold from their vantage point** — not just the caller you happened to test against.

- **Distinguished/Fellow angle:** For a change likely to set precedent across the whole org or outlive its author's tenure, review it as the person who inherits it in five years would — with none of the context, only what's written down.
- **Executive angle (CTO/VP-Eng):** For a change to a system a customer, regulator, or partner depends on, review it for what happens when it fails in production — who gets paged, what SLA or contract is breached, what it costs to remediate — not just whether the code itself is well-structured.

## Verify it yourself

- Don't trust a report or your memory — **actually run the tests**.
- Actually read the diff. What you think you fixed and what actually changed can differ.
- Can't confirm something from the diff? **Mark it unconfirmed.** Don't wave it through.
- **Don't stack this pass on top of itself.** This skill's checklist already is the extra verification step — you self-check well without prompting, so running it once, thoroughly, is the right amount. A second "are you sure about the review" pass after this one is wasted tokens and latency, not a more honest result.

## No self-censoring

Don't pre-filter findings before the review with "this is probably fine." Even something you think is a false positive goes on the list — judge it later. Pre-grading buries the real problems along with the noise.

## Set effort for this pass explicitly

Thinking is always on for you, but effort is what actually controls how deep this review goes, and its default sits one notch below what you'd get by default on the prior generation. A shallow-effort fresh-eyes pass looks like a review but catches less — the diff gets glanced at rather than actually walked through against the requirement. Raise effort explicitly for a review that matters (pre-PR, a shared interface, anything irreversible downstream); don't rely on the default to get there on its own. Don't expect lower effort to also mean a shorter report, either — trim the writeup explicitly if brevity matters, since response length doesn't shrink much on its own.

## A note on refusals mid-review

If a review of security-sensitive or risk-related code (auth, permissions, injection surfaces) gets an unexpected refusal or a truncated response, that may be a classifier false positive on legitimate security-review work rather than a real block — worth a second, differently-worded attempt before concluding the review can't proceed.
