> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Disprove-Biased Review

A confident answer isn't the same as a correct one. The longer a session runs, the more quietly assumptions harden into "facts." This skill pulls out a review posture **biased to disprove, not approve** — **before** the finished result exists.

**This isn't a verdict on finished work.** It's interrogating a decision while it's still in flight, while course-correction is still cheap.

## When it applies — the bar for "non-trivial"

Any one of these makes it non-trivial:

- introduces or changes branching logic
- crosses a module or service boundary
- claims a property the type system or compiler can't verify (thread-safety, idempotency, ordering, invariants)
- correctness depends on context a future reader can't see
- it's irreversible (production deploy, data migration, public API change)
- it crosses a team or service ownership boundary, or sets a pattern other teams are likely to copy — the review then has to ask what happens elsewhere if this spreads, not just whether it's correct here
- **Distinguished/Fellow angle:** if it could become company-wide doctrine, get open-sourced, or get cited in a conference talk competitors watch, the disproof has to hold up for years and outside the building — would it still survive review from someone joining in five years with none of the institutional memory behind it?
- **Executive angle (CTO/VP-Eng):** if it changes headcount or team shape, commits to vendor/infra spend, or moves regulatory, competitive, or customer-trust risk (a build-vs-buy call, a data-access grant, killing a team), the disproof needs a reviewer who'd have to defend that budget or that risk to a board, not just someone who'd maintain the resulting code.

**Doesn't apply**: mechanical work (renames, formatting, moving files), following an explicit instruction as given, reading or summarizing existing code, an obviously-correct one-line change. **Suspect every keystroke and nothing ships** — apply this only when the bar above is actually met.

**Be explicit about the bar, not just the spirit of it.** State plainly when the bar is met, rather than assuming it's understood. And note the fit below: the Distinguished/Fellow and Executive angles, and most "crosses a service boundary" or "sets company-wide precedent" calls, involve exactly the kind of ambiguous, high-context judgment this model is the weakest fit for — for those, this model's role is running the mechanical parts of the procedure (compressing the claim, checking findings against the output text), with a stronger model or a human making the actual disproof judgment.

## Procedure

1. **Claim** — compress it into two or three lines, in the form "X is safe because Y." If you can't phrase it that way, it's a feeling, not a decision.
2. **Extract** — keep only the **output and its contract** needed for review. Strip the reasoning that got you there. Hand over the reasoning too and you just get agreement with that reasoning. Shrink it to something reviewable at a glance — split it first if you can't.
3. **Disprove** — frame the request **adversarially**. Not "does this look OK?" but **"find what's wrong with this."** The question's phrasing decides the answer. State this framing explicitly rather than trusting it to be inferred.
4. **Reconcile** — take what comes back and check each point against the actual output text; sort into: real defect / already handled / out of scope.
5. **Stop condition** — stop once only minor points remain, after three passes, or when the user says it's enough.

## Core principles

**Framing decides the answer.** Ask "is this a problem?" and the easy answer is no. Ask "find the problem in this" and one actually gets found. The wording of the review request determines the quality of the review.

**Only stripped context makes it a real review.** Hand over the reasoning that led to the conclusion and you get a review that's been talked into that reasoning. Hand over only the output and its contract — for this model, extraction matters even more: a smaller, well-bounded review task plays to its strengths, while a sprawling, loosely-scoped one doesn't.

**Decisions with wide blast radius need reviewers who don't share your stake in them.** A choice other teams will build interfaces on top of, or copy as precedent, deserves a reviewer who isn't invested in your original reasoning being right — self-review from inside the same context tends to confirm rather than disprove.

**With a 1.05M-token context window**, the claim and its dependency chain can stay loaded without needing to summarize away detail. Reasoning effort can be switched off for a fast, narrow disproof pass on a well-specified, low-stakes claim; leave it on for anything where the claim itself takes real interpretation to compress correctly.

## Calibration note for this model

This is the fastest, cheapest tier — a good fit for high-volume, narrow disproof passes: checking a well-specified claim against its output for an already-known class of defect, or running the extraction and reconciliation steps mechanically. It is the weakest fit in this family for judgment-heavy adversarial review: identifying a *novel* flaw in an ambiguous, high-context, or high-stakes claim (the irreversible, cross-boundary, Distinguished/Fellow, and Executive categories above) should route to a stronger model or a human reviewer rather than being treated as settled by this model's pass alone.
