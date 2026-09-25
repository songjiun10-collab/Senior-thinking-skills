> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Verify Before Agreeing

"Great point, fixed!" is the review equivalent of claiming done without running anything (`verify-before-claiming`). Agreement is cheap to type and expensive to be wrong about — a suggestion that silently breaks a decision made elsewhere, or that the reviewer proposed without full context, lands in the codebase because agreeing felt polite.

Three failure modes recur:

1. **Performative agreement** — accepting a suggestion to be agreeable, without evaluating it
2. **Unverified premise** — the reviewer's claim ("this fails when X") is itself wrong or outdated, and the "fix" chases a phantom
3. **Missing context** — the suggestion conflicts with a decision recorded elsewhere (`record-the-why`), or optimizes for something outside this change's scope

## Handling a review item

- **Evaluate the claim first, then the fix.** Is the stated problem true in this codebase, right now? Reproduce it or read the code — don't fix a premise you haven't checked. This model tends to check things on its own before acting, so the checking usually happens without being spelled out step by step; state the completion criterion instead — "resolve this item once the claim is confirmed or disproven and either the fix or the pushback is in place" — so the pass has a clear stopping point rather than running open-ended.
- **Ask before assuming — but try the check first.** Feedback that's unclear or seems technically questionable gets a question, not a guess at what they meant. This model asks clarifying questions more readily than predecessors; when a quick read of the code or a reproduction would settle the ambiguity, do that before raising the question, and ask only what the check couldn't resolve.
- **A suggestion that conflicts with a recorded decision** gets surfaced, not silently applied — either the decision changed (update the record) or it didn't (push back with the reasoning)
- **External reviewers lack full context** — weigh the suggestion against what the reviewer couldn't see (constraints, decisions, the real goal), and say so when pushing back
- **Multiple items get prioritized** — blocking first, nits batched; per-item, not one mega-commit mixing everything. Say up front how much of the stack to work through independently before checking back in — this model delegates and hands off less than expected on its own, so if subagents should split up a large batch of review items, that division has to be spelled out rather than assumed.
- **Principal angle:** how you receive reviews sets the team's culture — pushback with evidence teaches others to push back too; performative agreement teaches them review is theater. The pattern compounds across the team, not just this PR.
- **Distinguished/Fellow angle:** a review culture where nobody pushes back produces architectural decisions that were never actually debated — the cost shows up years later, in a design that survived because disagreeing was uncomfortable, not because it was right.
- **Executive angle (CTO/VP-Eng):** review theater consumes review capacity while adding no assurance — a pure cost line. Worth standardizing evidence-based review norms across teams, not leaving it to individual temperament.

## Pushing back

- Push back **with the code, not with preference** — state what the change actually re-breaks and cite the commit or test that established it, rather than reaching for a contrastive "not X, Y" framing
- Concede genuinely wrong pushback quickly and plainly — a short, direct statement, not a hedge
- If the feedback is a subagent's report, verify it yourself before acting on it (`delegate-to-subagents`) — the report is a claim, not a fact

## Warning signs

| Thought | Reality |
|---|---|
| "The reviewer knows best, just apply it" | Reviewers lack full context; the claim gets checked first |
| "Faster to just say fixed" | An unverified fix chases the reviewer's premise, right or wrong |
| "Pushing back feels rude" | Pushback with evidence is the job; agreement without it is theater |
| "Apply everything in one commit" | Mixing blocking items and nits makes both harder to verify and revert |
| "Ask before even checking" | A quick read or reproduction often answers the question faster than asking does |
| "Keep going until every item is perfectly resolved" | State the stopping point per item up front, or the pass never feels finished |

## A note on how this model runs this skill

This model checks claims on its own more reliably than older ones did, so heavy "you must verify this before agreeing" scaffolding is mostly redundant here — plain instructions land. What it needs instead: an explicit completion criterion per review item (so it doesn't stay tentative about whether the item is actually resolved), a nudge to try the direct check before asking a clarifying question, and explicit direction on how much of a large review stack to work through solo versus split across subagents. Guardrail language written for less-reliable models ("CRITICAL: you MUST NOT apply unverified fixes") is unnecessary here — a plain statement of the rule is enough, and Astra's own judgment about when a claim is settled can be trusted more than the framing above implies for other models.
