> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

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

**Effort for this skill.** Thinking is always on and effort defaults to `medium`; in Anthropic's testing Opus 5.5 at `medium` matched or beat Opus 5 at `high` on coding and knowledge work, so the default is a reasonable start for a disproof pass. If you or your harness have seen a real gain from a higher level on this kind of review, set it for that request before step 3 — effort is fixed by the caller per request, not raised mid-turn. Response length won't reliably shrink at lower effort either (carried over from Opus 5 guidance), so if you want a terse three-line verdict rather than an exhaustive one, say so explicitly — don't count on effort level alone to control that.

## Core principles

**Framing decides the answer.** Ask "is this a problem?" and the easy answer is no. Ask "find the problem in this" and one actually gets found. The wording of the review request determines the quality of the review.

**Only stripped context makes it a real review.** Hand over the reasoning that led to the conclusion and you get a review that's been talked into that reasoning. Hand over only the output and its contract.

**Decisions with wide blast radius need reviewers who don't share your stake in them.** A choice other teams will build interfaces on top of, or copy as precedent, deserves a reviewer who isn't invested in your original reasoning being right — self-review from inside the same context tends to confirm rather than disprove. Opus 5 guidance (carried over to 5.5) says the model verifies its own work unprompted without being told to; the value of an adversarial pass here isn't extra double-checking, it's the independent, stake-free framing — don't stack redundant "are you sure?" instructions on top of the Disprove step, they cost tokens and latency without buying more correctness. Step 3's adversarial framing already does the work generic re-verification would try to do.

**Watch the delegation reflex.** This model reaches for a subagent more readily than earlier ones, including for legs of this procedure a direct read would settle faster — extracting the claim (step 1) or checking one specific counterexample (step 4) is often faster done directly than dispatched. Delegate the disproof pass itself if the review genuinely needs distance from your own reasoning; don't delegate mechanical sub-steps that don't need it.

**A refusal isn't always a real block.** This model runs safety classifiers (biology, cybersecurity, reasoning extraction), and a decline arrives as `stop_reason: "refusal"`. Finding vulnerabilities in source code is explicitly allowed — only high-risk dual-use cyber activity is not — so a refusal on a legitimate review of an auth check or endpoint is worth a second, more explicitly scoped attempt before assuming the review itself is out of bounds.

**Don't over-build the review artifact.** Opus 5 guidance (which Anthropic says still applies to Opus 5.5) notes a tendency to expand a task's scope and to write longer deliverables than needed — here that looks like a full report template, extra categorization, a scoring rubric nobody requested. The output of a disproof pass is a short list of real defects sorted by the Reconcile step, not a deliverable to polish.
