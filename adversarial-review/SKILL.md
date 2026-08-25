---
name: adversarial-review
description: >-
  Materialize a review posture biased to disprove, not approve, before a non-trivial decision stands. Use for architectural decisions made under uncertainty, non-trivial code about to be committed, non-obvious claims ("this is safe", "this scales"), or unfamiliar code — while course-correction is still cheap, not just at the end. Sharper version of fresh-context-review — the framing of the review request decides the answer.
---

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

## Procedure

1. **Claim** — compress it into two or three lines, in the form "X is safe because Y." If you can't phrase it that way, it's a feeling, not a decision.
2. **Extract** — keep only the **output and its contract** needed for review. Strip the reasoning that got you there. Hand over the reasoning too and you just get agreement with that reasoning. Shrink it to something reviewable at a glance — split it first if you can't.
3. **Disprove** — frame the request **adversarially**. Not "does this look OK?" but **"find what's wrong with this."** The question's phrasing decides the answer.
4. **Reconcile** — take what comes back and check each point against the actual output text; sort into: real defect / already handled / out of scope.
5. **Stop condition** — stop once only minor points remain, after three passes, or when the user says it's enough.

## Core principles

**Framing decides the answer.** Ask "is this a problem?" and the easy answer is no. Ask "find the problem in this" and one actually gets found. The wording of the review request determines the quality of the review.

**Only stripped context makes it a real review.** Hand over the reasoning that led to the conclusion and you get a review that's been talked into that reasoning. Hand over only the output and its contract.

**Decisions with wide blast radius need reviewers who don't share your stake in them.** A choice other teams will build interfaces on top of, or copy as precedent, deserves a reviewer who isn't invested in your original reasoning being right — self-review from inside the same context tends to confirm rather than disprove.
