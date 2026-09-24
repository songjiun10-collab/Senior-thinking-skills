> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

# Disprove-Biased Review

A confident answer isn't the same as a correct one. The longer a session runs, the more quietly assumptions harden into "facts." This skill pulls out a review posture **biased to disprove, not approve** — **before** the finished result exists.

**This isn't a verdict on finished work.** It's interrogating a decision while it's still in flight, while course-correction is still cheap.

## When it applies — the bar for "non-trivial"

Any one of these makes it non-trivial: it introduces or changes branching logic, crosses a module or service boundary, claims a property the type system or compiler can't verify (thread-safety, idempotency, ordering, invariants), correctness depends on context a future reader can't see, it's irreversible (production deploy, data migration, public API change), or it crosses a team/service ownership boundary or sets a pattern other teams are likely to copy — the review then has to ask what happens elsewhere if this spreads, not just whether it's correct here.

- **Distinguished/Fellow angle:** if it could become company-wide doctrine, get open-sourced, or get cited in a conference talk competitors watch, the disproof has to hold up for years and outside the building — would it still survive review from someone joining in five years with none of the institutional memory behind it?
- **Executive angle (CTO/VP-Eng):** if it changes headcount or team shape, commits to vendor/infra spend, or moves regulatory, competitive, or customer-trust risk (a build-vs-buy call, a data-access grant, killing a team), the disproof needs a reviewer who'd have to defend that budget or that risk to a board, not just someone who'd maintain the resulting code.

**Doesn't apply**: mechanical work (renames, formatting, moving files), following an explicit instruction as given, reading or summarizing existing code, an obviously-correct one-line change. **Suspect every keystroke and nothing ships** — apply this only when the bar above is actually met.

## Procedure

State this as a goal and a constraint rather than a script to execute mechanically: **the goal is a disproof, not a checklist completed.** That said, the shape is:

1. **Claim** — compress it into two or three lines, in the form "X is safe because Y." If you can't phrase it that way, it's a feeling, not a decision.
2. **Extract** — keep only the **output and its contract** needed for review. Strip the reasoning that got you there. Hand over the reasoning too and you just get agreement with that reasoning. Shrink it to something reviewable at a glance — split it first if you can't.
3. **Disprove** — frame the request **adversarially**. Not "does this look OK?" but **"find what's wrong with this."** The question's phrasing decides the answer.
4. **Reconcile** — take what comes back and check each point against the actual output text; sort into: real defect / already handled / out of scope.
5. **Stop condition** — stop once only minor points remain, after three passes, or when the user says it's enough.

This model's own reasoning through a multi-pass adversarial review often exceeds what a rigidly scripted sequence would produce — treat steps 1-5 as the shape of a good disproof, not a rigid script to follow literally step-by-step. If a shorter path to a real defect is obvious, take it.

**Say explicitly if you want progress visibility.** This model writes fewer user-facing updates between passes by default during a multi-pass review — it may go quiet through all three passes and return only the final reconciled list. If you need to see where a claim broke down, or want a status after each pass, ask for that explicitly; it won't volunteer it unprompted.

## Core principles

**Framing decides the answer.** Ask "is this a problem?" and the easy answer is no. Ask "find the problem in this" and one actually gets found. The wording of the review request determines the quality of the review.

**Only stripped context makes it a real review.** Hand over the reasoning that led to the conclusion and you get a review that's been talked into that reasoning. Hand over only the output and its contract.

**Decisions with wide blast radius need reviewers who don't share your stake in them.** A choice other teams will build interfaces on top of, or copy as precedent, deserves a reviewer who isn't invested in your original reasoning being right — self-review from inside the same context tends to confirm rather than disprove.

**This model handles a long multi-pass review well in one continuous turn** — three full disprove/reconcile cycles against a large claim don't need to be split across separate exchanges the way they might for a shorter-horizon model. Let it run the full stop condition in one go rather than checking in after every single pass, unless progress visibility was requested per above.
