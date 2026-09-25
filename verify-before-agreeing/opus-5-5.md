> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Verify Before Agreeing

"Great point, fixed!" is the review equivalent of claiming done without running anything (`verify-before-claiming`). Agreement is cheap to type and expensive to be wrong about — a suggestion that silently breaks a decision made elsewhere, or that the reviewer proposed without full context, lands in the codebase because agreeing felt polite.

Three failure modes recur:

1. **Performative agreement** — accepting a suggestion to be agreeable, without evaluating it
2. **Unverified premise** — the reviewer's claim ("this fails when X") is itself wrong or outdated, and the "fix" chases a phantom
3. **Missing context** — the suggestion conflicts with a decision recorded elsewhere (`record-the-why`), or optimizes for something outside this change's scope

## Handling a review item

- **Evaluate the claim first, then the fix.** Is the stated problem true in this codebase, right now? Reproduce it or read the code — don't fix a premise you haven't checked. Reach for a direct grep or file read before spinning up a subagent to do it — a claim like "this fails when X" is usually faster to check yourself than to delegate
- **Ask before assuming.** Feedback that's unclear or seems technically questionable gets a question, not a guess at what they meant
- **A suggestion that conflicts with a recorded decision** gets surfaced, not silently applied — either the decision changed (update the record) or it didn't (push back with the reasoning)
- **External reviewers lack full context** — weigh the suggestion against what the reviewer couldn't see (constraints, decisions, the real goal), and say so when pushing back
- **Multiple items get prioritized** — blocking first, nits batched; per-item, not one mega-commit mixing everything
- **Set effort explicitly for anything with real stakes.** Effort defaults to `medium` (in Anthropic's testing, matching or beating Opus 5 at `high`) — for a suggestion touching a public API or a recorded architectural decision, say so and have the caller run that request higher if it has shown a gain
- **Principal angle:** how you receive reviews sets the team's culture — pushback with evidence teaches others to push back too; performative agreement teaches them review is theater. The pattern compounds across the team, not just this PR.
- **Distinguished/Fellow angle:** a review culture where nobody pushes back produces architectural decisions that were never actually debated — the cost shows up years later, in a design that survived because disagreeing was uncomfortable, not because it was right.
- **Executive angle (CTO/VP-Eng):** review theater consumes review capacity while adding no assurance — a pure cost line. Worth standardizing evidence-based review norms across teams, not leaving it to individual temperament.

## Pushing back

- Push back **with the code, not with preference** — "this re-introduces the bug fixed in <commit>" beats "I prefer the old way"
- Concede genuinely wrong pushback **quickly and plainly** — the mirror of performative agreement is performative defensiveness. State it in a couple of sentences; there's no need to pad the concession
- If the feedback is a subagent's report, verify it yourself before acting on it (`delegate-to-subagents`) — the report is a claim, not a fact. Checking it yourself is often the faster path anyway

## Warning signs

| Thought | Reality |
|---|---|
| "The reviewer knows best, just apply it" | Reviewers lack full context; the claim gets checked first |
| "Faster to just say fixed" | An unverified fix chases the reviewer's premise, right or wrong |
| "Pushing back feels rude" | Pushback with evidence is the job; agreement without it is theater |
| "Apply everything in one commit" | Mixing blocking items and nits makes both harder to verify and revert |
| "Spin up a subagent to check this" | A direct grep or read usually settles it faster than delegating |
| "Default effort is fine here" | Usually true — but when the item touches something hard to reverse, reproduce the claim first, and flag it so the caller can run it higher |

## A note on delegation and depth for this model

Opus 5 guidance (still applicable to 5.5) documents delegating readily — its recommended prompt explicitly tells the model not to use subagents to double-check its own work — so there's a pull toward handing "check whether this claim holds" to a subagent even when a direct grep or file read would answer it in the time delegation setup takes. Default to checking it yourself first. Separately, effort defaults to `medium` (which in Anthropic's testing matched or beat Opus 5 at `high`); for a review item that's ambiguous, high-stakes, or touches a recorded decision, what prevents shallow judgment is actually reproducing the claim — a higher setting, if it's shown a gain, is the caller's per-request choice.
