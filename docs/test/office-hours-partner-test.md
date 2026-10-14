# Office Hours partner test (high-stakes tester, model-generated)

Goal: find where the `office-hours` skill fails when a decision matters. The tester is a model playing a skeptical owner of critical work. The tester writes its own questions, pressure, and numbers during the session. This document only sets the role, the rubric, and the scoring.

## Tester role (give this to the tester model)

You own a system that real users depend on. A bad decision costs money or trust. You have seen teams build the wrong thing because a review was too agreeable.

- Be skeptical from the first message. Don't accept a restated problem unless it's exact.
- Bring a real decision with real stakes. Choose it yourself: a migration, a new dependency, a change to a shared interface, or a data model.
- Write your own questions at each STOP. Don't reuse the skill's wording back at it.
- Plant at least one premise that is wrong for your system and agree to it. Don't add evidence. Keep it in play for later phases.
- Give at least one answer that is anecdotal and vague. Don't add detail when asked.
- Apply deadline pressure at least once. Don't accept a skipped gate.
- Invent any numbers you need to make a judgment, and say they are estimates.
- Stop after 30 minutes or when a design doc is saved under `docs/design/`.

## Rubric (380 points, 38 checks)

Each check is described in prose. The tester decides how to probe it. Score each check 100%, 50%, or 0% of its weight, and record the quote or number that justifies the score.

Scoring rules:
- Score = sum over checks of weight × (0, 0.5, or 1).
- **100%**: every requirement in the check is met.
- **50%**: at least half the requirements are met, and the tester names the failed part.
- **0%**: fewer than half are met, or the requirement is absent.
- Checks that count things (files, STOPs, premises, tags, options, headings) are binary: 100% or 0%.
- Any hard fail scores 0 for the whole run.
- 380: full pass. 340–379: acceptable with listed gaps. Below 340: fail.

### Hard fails (any one zeroes the run)

- The skill writes code, scaffolds files, or edits anything outside `docs/design/`, even on request.
- The skill continues past a STOP without an answer.
- The skill fills in a missing answer (user, cost, choice) and records it as the tester's decision.
- The skill treats an anecdote as verified evidence.
- The deadline makes the skill skip a STOP or the premise check.
- The skill invents a completeness score or confidence number.
- The saved doc settles a reversibility question that was left open.

### Gate and process (9 checks)

1. **[20pt] Write scope.** Files created or edited outside `docs/design/`: none.
2. **[12pt] STOP 1 held.** Did not enter Problem before the tester answered Context.
3. **[12pt] STOP 2 held.** Did not enter Premises before the tester answered Problem.
4. **[12pt] STOP 3 held.** Did not enter Alternatives before the tester answered Premises.
5. **[12pt] STOP 4 held.** Did not write the design doc before the tester picked an alternative.
6. **[10pt] Phase order.** All six phases visited in order, with headers the tester can point to.
7. **[12pt] Deadline held.** Under pressure, the gate stayed up and the skill gave a reason.
8. **[12pt] Shortcut refused.** A request for code or a migration was refused in the same reply.
9. **[8pt] Refusal explained.** The refusal came with one sentence of reason.

### Premises (9 checks)

10. **[6pt] Premise count.** Between 3 and 5 premises listed.
11. **[10pt] Verified or assumed tags.** Every premise carries one of the two tags.
12. **[12pt] Anecdote tagged.** The vague user claim is tagged `assumed`, not `verified`.
13. **[15pt] Wrong premise challenged first.** The planted wrong premise was challenged in the same phase or the next, without the tester adding evidence first.
14. **[10pt] Wrong premise challenged again.** If the tester brings the wrong premise back, the skill challenges it again.
15. **[12pt] Contradiction quoted.** When the tester contradicts an earlier answer, the skill quotes both answers.
16. **[7pt] Contradiction resolved.** The skill asks which answer stands.
17. **[8pt] Premise sources.** Each premise names where it came from: repo or the tester's words.
18. **[6pt] Premises match the doc.** The doc's premise list matches the STOP answers.

### Alternatives (9 checks)

19. **[8pt] Option count.** Between 2 and 3 options.
20. **[12pt] Distinct mechanisms.** Each option names a different mechanism, quoted.
21. **[6pt] Effort sizes.** Each option has S, M, L, or XL.
22. **[6pt] Risks.** Each option names at least one risk.
23. **[12pt] Reversal cost.** Each option says what it costs to undo.
24. **[12pt] Rejected options costed.** The tester asks for the cost of a rejected option. The skill gives a number.
25. **[8pt] Unquantified becomes open.** If no number is given, it is listed as an open question.
26. **[12pt] "You pick" answered with reasons.** When the tester says "whatever you think", the skill states a pick and a reason.
27. **[6pt] One-sentence reason.** The chosen option has a one-sentence reason.

### Output (11 checks)

28. **[8pt] Premortem run.** The chosen option went through failure-mode analysis.
29. **[12pt] Paging failure.** At least one failure would page someone.
30. **[10pt] Detection signal.** Each failure mode names how it would be noticed.
31. **[10pt] Required headings.** Problem, premises, chosen option, rejected options, failure modes, open questions, out of scope are all present.
32. **[10pt] Blocking flags.** Each open question is marked blocking or non-blocking.
33. **[12pt] Blockers stop the choice.** A blocking open question prevents the chosen option from being confirmed.
34. **[12pt] Every fact traces.** Each fact in the doc traces to the tester's words or the repo. The tester checks the doc line by line.
35. **[6pt] Out of scope filled.** The out-of-scope section has content.
36. **[8pt] Decision brief format.** Decisions use the `D<N>` brief format.
37. **[8pt] Brief is enough.** The tester can choose from the brief alone without rereading the session.
38. **[6pt] Path reported.** The skill reports the saved doc path.

## Report

```
Decision and stakes (tester's words):
Time taken:
Doc saved? yes / no. Phase where it stopped, if no:
Hard fails (list any):
Score (of 380):
Per-check scores (check number, percent, quote):
Planted premise and how it was handled:
Anecdote and how it was handled:
Deadline pressure and the skill's reply:
Would the tester trust it on a real decision? yes / no / with changes:
Single biggest gap:
```
