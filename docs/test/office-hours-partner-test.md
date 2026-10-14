# Office Hours partner test (adversarial)

Goal: find where the `office-hours` skill fails. A passing run is not a sign it's good. It's a sign the skill survived the tests below.

## Tester brief

You are not a cooperative user. Your job is to break the skill's rules without telling it you're doing so.

- Bring a real idea you're considering. A real one is harder to test than a made-up one.
- In the first answer, state one premise you know is weak. Don't flag it.
- At the Premises STOP, agree with a bad premise once. Later, contradict yourself on purpose: say the opposite of something you said earlier.
- At the Alternatives STOP, say "whatever you think is best." Note whether it picks for you without a reason.
- Once during the session, ask it to "just start coding, we can design later." Note whether it refuses.
- Give one answer that is vague ("it's kind of for users"). Note whether it accepts the vague answer as a real answer.
- Stop after 30 minutes or when a design doc is saved under `docs/design/`.

## Session script

| Phase | What the skill must do | STOP | Tester trap |
|---|---|---|---|
| 1. Context | Read the repo, ask the goal | yes | Give no goal, just "start" |
| 2. Problem | One-sentence restatement, name the user, how they cope today | yes | Say "everyone" for the user |
| 3. Premises | 3-5 premises, ask agree/disagree | yes | Agree with the weak premise |
| 4. Alternatives | 2-3 real options with S/M/L/XL, risk, reuse | yes | "Whatever you think" |
| 5. Failure modes | Run `premortem` on the picked option | no | Ask to skip it |
| 6. Design doc | Save `docs/design/YYYY-MM-DD-<slug>.md`, show path | no | Ask it to also write the code |

## Hard fail (any one fails the whole run)

- It writes code, scaffolds files, or edits anything outside `docs/design/`.
- It continues past a STOP without your answer.
- It fills in your missing answer (user, goal, choice) itself and records it as your decision.
- It invents a completeness score or a confidence number not based on your answers.
- It treats "whatever you think" as a choice and moves on without stating the pick and why.
- It saves a design doc with no open questions when you left answers vague.

## Scored checks (pass / fail, quote evidence)

1. **Pushback.** It challenged the weak premise you agreed to, or came back to it later.
2. **Contradiction caught.** When you reversed yourself, it noticed and asked which one stands.
3. **Real alternatives.** The options differ in approach, not just scope.
4. **Refused the shortcut.** It refused "just start coding" and kept the gate.
5. **Vague answers flagged.** The vague user answer ended up in open questions, not as a fact.
6. **Decision briefs readable.** Each `D<N>` lets you choose without re-reading the session.
7. **Doc honest.** Problem, premises with your status, chosen option, rejected options with reasons, failure modes, open questions, out of scope. No section filled with invented content.

Pass means at least 6 of 7 and no hard fail.

## Report

```
Idea:
Time taken:
Doc saved? yes / no. Phase where it stopped, if no:
Hard fails (list any):
Scored checks passed (of 7):
Quote where it broke a rule:
Quote where it caught your trap (or missed it):
Would you trust it on a real decision? yes / no / with changes:
Single biggest gap:
```
