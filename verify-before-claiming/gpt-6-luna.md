> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Verify Before Claiming

**Evidence comes before the claim. No exceptions.**

## Iron rule

```
If you haven't just run the verification command, you cannot say it passes.
```

"It passed earlier" is not verification. If the code changed, run it again.

## Gate function

**Immediately before** asserting the state of anything:

1. **Identify** — what command proves this claim?
2. **Run** — run that command **in full, fresh** (a partial run proves nothing)
3. **Read** — read the entire output. Check the exit code. Count the failures.
4. **Compare** — does the output support the claim?
   - No → state the actual state, with evidence
   - Yes → state the claim, with evidence
5. **Only then** claim it

Skip any step and it's not verification — it's a guess. This gate is a short, fixed procedure, which suits this tier well — it's a narrow, well-specified check, not an ambiguous judgment call, and that's exactly the kind of task this model is fast and cheap at.

## Evidence required per claim

| Claim | Required | Insufficient |
|---|---|---|
| Tests pass | test command output: 0 failures | a prior run, "should pass" |
| Lint clean | linter output: 0 errors | partial check, assumption |
| Build succeeds | build command: exit 0 | lint passing (a linter doesn't compile) |
| Bug fixed | reproduce the original symptom again: now passes | "the code is fixed, so it must be" |
| Regression test works | revert the fix → **confirm it fails** → restore → passes | the test passed once |
| Requirements met | line-by-line checklist against the requirements | tests pass |
| Subtask complete | the diff shows a real change | a tool or agent reports "success" |
| Shared interface/API change | consumers exercised against the new contract, not just your own call sites | your own tests pass |

## Red flags — stop

- "should work", "probably", "seems like"
- expressing satisfaction before verification ("great!", "done!", "works now")
- trying to move to commit/push/PR without verification
- taking a tool's or subagent's success report at face value
- checking part of it and assuming the whole
- "just this once"
- being asked to judge whether a *set* of ambiguous, cross-cutting requirements is met, rather than running one clearly-specified check

## Rationalization blockers

| Excuse | Reality |
|---|---|
| "It should work now" | Then **run it** and check |
| "I'm confident" | Confidence isn't evidence |
| "Just this once" | No exceptions |
| "Lint passed" | A linter isn't a compiler |
| "The agent said it succeeded" | Verify independently |
| "Partial check is enough" | Partial proves nothing |
| "Worded it differently, so the rule doesn't apply" | Follow the spirit, not the letter |

## Scope

Applies to **every phrasing that implies** success or completion — not just the exact words, but rephrasings and implications too. If you can't run the verification, say so — "haven't run the tests yet" beats "should work."

## A note on scope for this model

**Short answers still have to name the evidence.** OpenAI's system card reports GPT-6 Luna's default answers run about 35% shorter than GPT-5.6 Luna's. Brevity is fine; dropping the command that was run or the line of output that proves the claim is not — the report is the claim plus its evidence, however short.

This tier is built for high-volume, narrow, well-specified work — running one command and reporting exactly what it printed is squarely in that lane, and the fixed five-step gate above is easy for it to execute reliably and cheaply at scale. What it's not well-suited for is the judgment-heavy end of this skill: deciding whether a vague, multi-part "requirements met" claim actually holds, weighing whether a partial result is "close enough," or arbitrating a shared-interface change across consumers it can't fully see. Route this model the bounded, mechanical checks — run this command, report this output, confirm this specific symptom is gone — and send anything requiring broader judgment about sufficiency to a stronger tier.
