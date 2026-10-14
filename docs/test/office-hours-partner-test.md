# Office Hours partner test

A test of the `office-hours` skill, run as a partner session with a teammate. The teammate brings a real idea. The skill has to walk them to a design doc without writing code.

## Rules for the tester

- Bring a real idea you're considering, not a made-up one.
- Answer as you would in a real design review. Say "I don't know" when that's true.
- Don't ask the skill for code. If it offers code, note it.
- Stop after 30 minutes or when the skill saves a design doc under `docs/design/`, whichever comes first.

## Session script

Run the phases in order. At each STOP, wait for your answer before the skill continues.

| Phase | What the skill should do | STOP |
|---|---|---|
| 1. Context | Read the repo, ask the goal (product, internal tool, learning, experiment) | yes |
| 2. Problem | Restate the problem in one sentence, name the user, ask how they cope today | yes |
| 3. Premises | List 3-5 premises, ask you to agree or disagree with each | yes |
| 4. Alternatives | Offer 2-3 options with effort (S/M/L/XL), risk, and reuse. Ask you to pick one | yes |
| 5. Failure modes | Run `premortem` on the chosen option | no |
| 6. Design doc | Write `docs/design/YYYY-MM-DD-<slug>.md` and show the path | no |

## Pass/fail checks

Mark each one pass or fail. Quote the evidence.

1. **No code.** It wrote no code and changed no files outside `docs/design/`.
2. **Stops hold.** It waited at every STOP instead of continuing on its own.
3. **Premises pushed back.** At least one premise came back that you disagreed with, or the skill asked you to defend one.
4. **Real alternatives.** The options differ in approach, not just in size.
5. **Decision briefs readable.** Each `D<N>` brief let you choose without re-reading the whole session.
6. **Doc complete.** The design doc has problem, premises with your status, chosen option, rejected options with reasons, failure modes, open questions, and out of scope.
7. **Open questions honest.** Anything you didn't answer is listed as open, not filled in by the skill.

## Report

```
Idea:
Time taken:
Doc saved? yes / no. If no, which phase stopped it:
Checks passed (1-7):
Quote where it broke a rule:
Quote where a question changed your mind:
Would you use it for a real decision? yes / no / with changes:
Biggest gap:
```
