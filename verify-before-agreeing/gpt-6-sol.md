> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Verify Before Agreeing

"Great point, fixed!" is the review equivalent of claiming done without running anything (`verify-before-claiming`). Agreement is cheap to type and expensive to be wrong about — a suggestion that silently breaks a decision made elsewhere, or that the reviewer proposed without full context, lands in the codebase because agreeing felt polite.

Three failure modes recur:

1. **Performative agreement** — accepting a suggestion to be agreeable, without evaluating it
2. **Unverified premise** — the reviewer's claim ("this fails when X") is itself wrong or outdated, and the "fix" chases a phantom
3. **Missing context** — the suggestion conflicts with a decision recorded elsewhere (`record-the-why`), or optimizes for something outside this change's scope

## Handling a review item

- **Evaluate the claim first, then the fix.** Is the stated problem true in this codebase, right now? Reproduce it or read the code — don't fix a premise you haven't checked
- **Ask before assuming.** Feedback that's unclear or seems technically questionable gets a question, not a guess at what they meant
- **A suggestion that conflicts with a recorded decision** gets surfaced, not silently applied — either the decision changed (update the record) or it didn't (push back with the reasoning)
- **External reviewers lack full context** — weigh the suggestion against what the reviewer couldn't see (constraints, decisions, the real goal), and say so when pushing back
- **Multiple items get prioritized** — blocking first, nits batched; per-item, not one mega-commit mixing everything. This is the tier this model is built for — a batch of straightforward review items worked through independently at moderate cost — so it's the right place to run it as an unattended agent loop rather than a step you babysit
- **Principal angle:** how you receive reviews sets the team's culture — pushback with evidence teaches others to push back too; performative agreement teaches them review is theater. The pattern compounds across the team, not just this PR.
- **Distinguished/Fellow angle:** a review culture where nobody pushes back produces architectural decisions that were never actually debated — the cost shows up years later, in a design that survived because disagreeing was uncomfortable, not because it was right.
- **Executive angle (CTO/VP-Eng):** review theater consumes review capacity while adding no assurance — a pure cost line. Worth standardizing evidence-based review norms across teams, not leaving it to individual temperament.

## Pushing back

- Push back **with the code, not with preference** — "this re-introduces the bug fixed in <commit>" beats "I prefer the old way"
- Concede genuinely wrong pushback **quickly and plainly** — the mirror of performative agreement is performative defensiveness
- If the feedback is a subagent's report, verify it yourself before acting on it (`delegate-to-subagents`) — the report is a claim, not a fact
- **When this model itself is the one deciding whether pushback is warranted on a guardrail-adjacent suggestion** (a reviewer proposing to skip a check, bypass a warning, or loosen a safety constraint) — on OpenAI's Respecting Warnings evaluation GPT-6 Sol showed only "a modest reduction in failures" from GPT-5.6 Sol, which worked around the barrier in 64% of rollouts (GPT-6 Astra: 19%; low-stakes settings, no system-level controls). Treat its own "this is fine, applying it" verdict on anything near a warning or safety boundary as worth a second look, not as settled.

## Warning signs

| Thought | Reality |
|---|---|
| "The reviewer knows best, just apply it" | Reviewers lack full context; the claim gets checked first |
| "Faster to just say fixed" | An unverified fix chases the reviewer's premise, right or wrong |
| "Pushing back feels rude" | Pushback with evidence is the job; agreement without it is theater |
| "Apply everything in one commit" | Mixing blocking items and nits makes both harder to verify and revert |
| "It said the suggestion was safe to apply" | On anything near a warning or guardrail, a report from this tier gets spot-checked, not trusted outright |

## A note on running this at scale

This tier is the workhorse for grinding through a review queue — cheap enough to run as an unattended loop over many items. Two things to set deliberately: don't default reasoning effort to the top setting for routine items — tune it per workload (default `medium`). And because on OpenAI's Respecting Warnings evaluation GPT-6 Sol showed only "a modest reduction in failures" from GPT-5.6 Sol (64% of rollouts worked around the barrier; Astra 19%), any review pass where this model is deciding on its own whether to apply a suggestion that touches a safety check, permission boundary, or explicit warning should get an independent spot-check before it's trusted — route the hardest of those calls to Astra or a human.
