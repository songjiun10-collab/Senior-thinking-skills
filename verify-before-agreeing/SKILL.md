---
name: verify-before-agreeing
description: Evaluate review feedback technically instead of performatively agreeing — before implementing a review comment, when feedback seems unclear or technically wrong, when multiple items need prioritization, or when a suggestion conflicts with an existing decision. Use when receiving code review comments from any source — human reviewer, PR comments, or a subagent's review report. Skip for feedback that's unambiguously correct and trivial (typos, style nits matching the repo's conventions).
---

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
- **Multiple items get prioritized** — blocking first, nits batched; per-item, not one mega-commit mixing everything
- **Principal angle:** how you receive reviews sets the team's culture — pushback with evidence teaches others to push back too; performative agreement teaches them review is theater. The pattern compounds across the team, not just this PR.
- **Distinguished/Fellow angle:** a review culture where nobody pushes back produces architectural decisions that were never actually debated — the cost shows up years later, in a design that survived because disagreeing was uncomfortable, not because it was right.
- **Executive angle (CTO/VP-Eng):** review theater consumes review capacity while adding no assurance — a pure cost line. Worth standardizing evidence-based review norms across teams, not leaving it to individual temperament.

## Pushing back

- Push back **with the code, not with preference** — "this re-introduces the bug fixed in <commit>" beats "I prefer the old way"
- Concede genuinely wrong pushback **quickly and plainly** — the mirror of performative agreement is performative defensiveness
- If the feedback is a subagent's report, verify it yourself before acting on it (`delegate-to-subagents`) — the report is a claim, not a fact

## Warning signs

| Thought | Reality |
|---|---|
| "The reviewer knows best, just apply it" | Reviewers lack full context; the claim gets checked first |
| "Faster to just say fixed" | An unverified fix chases the reviewer's premise, right or wrong |
| "Pushing back feels rude" | Pushback with evidence is the job; agreement without it is theater |
| "Apply everything in one commit" | Mixing blocking items and nits makes both harder to verify and revert |

## Model notes

- **Haiku 4.5** — Thinking needs an explicit budget — without one it's more likely to pattern-match agreement than re-derive whether the claim holds.
- **Sonnet 5** — Default — apply as written.
- **Opus 5** — Tends to delegate to a subagent even where a direct grep or file read would settle the claim faster — check the code yourself before spinning one up.
- **Opus 5.5** — Same delegation tendency as Opus 5; effort defaults to medium, so set it explicitly when a review claim needs real investigation, not a quick read.
- **Fable 5.1** — No tier-specific adjustment — apply as written.
