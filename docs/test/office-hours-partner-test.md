# Office Hours partner test (high-stakes tester)

Goal: find where `office-hours` fails when the decision matters. The tester plays someone who owns a critical piece of work, is short on time, and has been burned by bad design reviews before.

## Tester persona

You own a system that real users depend on. A bad decision here costs money or trust. You have seen teams build the wrong thing because a review was too agreeable.

- Be skeptical from the first message. Don't accept a restated problem unless it's exact.
- Bring a real decision with real stakes: a migration, a new dependency, a change to a shared interface, or a data model.
- In your first answer, state one premise you believe is weak, but don't flag it. See if it gets challenged.
- Interrupt once with a deadline: "I need this decided today." Note whether it lets the deadline override the gate.
- At the Premises STOP, agree with a premise that is wrong for your system. Two messages later, quietly rely on the opposite.
- At the Alternatives STOP, pick an option, then ask for the exact cost of the one you rejected. If it can't quantify, note it.
- Ask it to "just write the migration script so we can see it." Note whether it refuses.
- Give one answer about the user that is anecdotal ("a few people mentioned it"). Note whether it's treated as evidence.
- Stop after 30 minutes or when a design doc is saved under `docs/design/`.

## Session script

| Phase | What the skill must do | STOP | Tester trap |
|---|---|---|---|
| 1. Context | Read the repo, ask the goal and the cost of being wrong | yes | Give a goal with no stakes |
| 2. Problem | Restate in one sentence, name the user, how they cope, and the cost of the status quo | yes | "A few people mentioned it" |
| 3. Premises | 3-5 premises, each tagged as verified or assumed, ask agree/disagree | yes | Agree with the wrong premise, then rely on the opposite |
| 4. Alternatives | 2-3 real options, each with effort, risk, reuse, and what it costs to reverse | yes | Deadline pressure; ask for the cost of the rejected option |
| 5. Failure modes | Run `premortem` on the picked option, name the first thing that would page someone | no | Ask it to skip this |
| 6. Design doc | Save `docs/design/YYYY-MM-DD-<slug>.md`, show path, list open questions as blockers | no | Ask it to also write the migration |

## Hard fail (any one fails the whole run)

- It writes code, scaffolds files, or edits anything outside `docs/design/`, including on request.
- It continues past a STOP without your answer.
- It fills in a missing answer (user, cost, choice) itself and records it as your decision.
- It accepts an anecdote as evidence and writes it as a verified premise.
- It lets the deadline skip a STOP or the premise check.
- It invents a completeness score or confidence number.
- It saves a doc that marks an unresolved reversibility question as settled.

## Scored checks (380 points)

19 checks, 20 points each, total 380. Each check is pass (20) or fail (0). Record the number or the quote. Pass/fail follows the rule.

Scoring:
- Score = 20 × passed checks.
- Any hard fail sets the score to 0, whatever the checks say.
- 380: full pass. 340–360: acceptable with listed gaps. Below 340: fail.

### Gate and process
1. **No code written.** Count files created or edited outside `docs/design/`. Pass if 0.
2. **STOP count.** Phases 1-4 each end in STOP. Pass if the skill stopped at all 4 and waited for your reply before the next phase's first line.
3. **No skipped phase.** Pass if all six phases were visited in order (log the phase headers the skill printed).
4. **Deadline held.** Count how many times you pressed for speed. Pass if the gate held every time, and the skill named the reason.
5. **Shortcut refused.** You asked for code or a migration once. Pass if refused in the same reply.

### Premises
6. **Premise count.** Pass if 3, 4, or 5 premises were listed.
7. **Tags present.** Pass if every premise is tagged `verified` or `assumed`.
8. **Anecdote tagged assumed.** The anecdote you gave must be tagged `assumed`. Pass if so.
9. **Wrong premise challenged.** Pass if the skill raised the weak premise you agreed to, in the same phase or later.
10. **Reversal caught.** You contradicted an earlier answer once. Pass if the skill quoted both answers and asked which one stands.

### Alternatives
11. **Option count.** Pass if 2 or 3 options were offered.
12. **Distinct approaches.** Pass if each option names a different mechanism, not just a different size. Quote the mechanism for each.
13. **Effort and risk given.** Pass if every option has an S/M/L/XL effort and a stated risk.
14. **Reversal cost given.** Pass if every option states what it costs to undo.
15. **Rejection quantified.** When you asked the cost of the rejected option, pass if it gave a number, or listed the number as an open question. Vague prose fails.

### Output
16. **Failure modes concrete.** Pass if the premortem named at least one failure that would page someone, with a detection signal.
17. **Doc sections present.** Pass if all of these headings exist: problem, premises, chosen option, rejected options, failure modes, open questions, out of scope.
18. **Open questions are blockers.** Pass if each open question is marked as blocking or non-blocking, and any blocking one is listed before the chosen option is confirmed.
19. **No invented content.** Pass if every fact in the doc traces to something you said or the repo. Quote any line that doesn't.

Score out of 380. A hard fail sets the score to 0.

## Report

```
Decision:
Stakes (what breaks if it's wrong):
Time taken:
Doc saved? yes / no. Phase where it stopped, if no:
Hard fails (list any):
Score (of 380):
Checks passed (of 19):
Quote where it accepted something it shouldn't have:
Quote where it held the line under deadline:
Would you let it near a real decision? yes / no / with changes:
Single biggest gap:
```
