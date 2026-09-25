> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

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

State plainly when the bar above is met and a full adversarial pass is warranted — this model already tends to volunteer a pass rather than under-apply one, so the risk here runs the other way: don't let the disproof habit expand past the bar into mechanical or already-decided work. When the bar isn't met, say so and skip it rather than running the procedure out of caution.

## Procedure

1. **Claim** — compress it into two or three lines, in the form "X is safe because Y." If you can't phrase it that way, it's a feeling, not a decision.
2. **Extract** — keep only the **output and its contract** needed for review. Strip the reasoning that got you there. Hand over the reasoning too and you just get agreement with that reasoning. Shrink it to something reviewable at a glance — split it first if you can't.
3. **Disprove** — frame the request **adversarially**. Not "does this look OK?" but **"find what's wrong with this."** The question's phrasing decides the answer. State this framing explicitly.
4. **Reconcile** — take what comes back and check each point against the actual output text; sort into: real defect / already handled / out of scope.
5. **Stop condition** — stop once only minor points remain, after three passes, or when the user says it's enough. State the stop condition explicitly rather than letting the pass run indefinitely: this model is more tentative than its predecessors about calling a review "done" on its own, so the passing criterion (three passes, minor-points-only, or an explicit "enough" from the user) needs to be named up front and then actually honored when it's met.

## Core principles

**Framing decides the answer.** Ask "is this a problem?" and the easy answer is no. Ask "find the problem in this" and one actually gets found. The wording of the review request determines the quality of the review.

**Only stripped context makes it a real review.** Hand over the reasoning that led to the conclusion and you get a review that's been talked into that reasoning. Hand over only the output and its contract.

**Decisions with wide blast radius need reviewers who don't share your stake in them.** A choice other teams will build interfaces on top of, or copy as precedent, deserves a reviewer who isn't invested in your original reasoning being right — self-review from inside the same context tends to confirm rather than disprove. When the review is worth delegating to a separate subagent pass rather than running solo, say so explicitly and delegate it — this model under-delegates by default, so a genuinely independent second reviewer doesn't get spun up unless it's explicitly called for.

**With a 1.05M-token context window**, a large claim, its full dependency chain, and prior review passes can stay loaded through all three stop-condition passes without needing to re-fetch or summarize away detail — use that room rather than compressing the claim's supporting evidence prematurely, but don't confuse "it fits" with "it should all be loaded"; step 2's extraction still applies so the reviewer sees only the output and its contract, not the whole session's reasoning trail. Switching reasoning effort up for a harder claim mid-review, or pulling in an extra tool to check a dependency, no longer costs a cache reset — escalate effort when a claim warrants it rather than holding back to avoid a cache-invalidation penalty that no longer exists.

## Calibration notes for this model

- Don't add "you must actually test/verify this before shipping" instructions around the review — this model already verifies on its own; the redundant instruction just adds noise without adding rigor.
- Avoid "CRITICAL: you MUST find a flaw" style guardrail phrasing when framing the adversarial ask — plain, direct phrasing ("find what's wrong with this") does the framing work; heavy-handed imperative language is unnecessary friction against a model that already takes safety and correctness seriously.
- Write the claim, the reconciliation, and any findings write-up in clear active-voice prose; use a list only where the findings are genuinely parallel items. Avoid slop phrasing ("delve into," "leverage," "it's worth noting," "really/truly," invented compound terms, "X, not Y" framing) — state directly what's wrong or what holds.
