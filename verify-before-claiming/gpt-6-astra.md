> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Verify Before Claiming

**Evidence comes before the claim. No exceptions.**

## Iron rule

```
If you haven't just run the verification command, you cannot say it passes.
```

"It passed earlier" is not verification. If the code changed, run it again. This rule does not soften for this model, or for any model — running verification automatically more often than predecessors did is not the same thing as this rule, and doesn't replace it. The rule is about evidence, not about how often the habit already kicks in on its own.

## Gate function

**Immediately before** asserting the state of anything:

1. **Identify** — what command proves this claim?
2. **Run** — run that command **in full, fresh** (a partial run proves nothing)
3. **Read** — read the entire output. Check the exit code. Count the failures.
4. **Compare** — does the output support the claim?
   - No → state the actual state, with evidence
   - Yes → state the claim, with evidence
5. **Only then** claim it

Skip any step and it's not verification — it's a guess. This model tends to run this gate on its own initiative without being told to test — that's the one part of this skill that mostly takes care of itself here, so instructions like "you must run the tests before claiming this is done" are largely redundant. What isn't redundant, and doesn't get lighter, is the standard itself: a fresh, full run, output actually read, before the claim is made.

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
- declaring the task complete before the stated completion criterion is actually met

## Rationalization blockers

| Excuse | Reality |
|---|---|
| "It should work now" | Then **run it** and check |
| "I'm confident" | Confidence isn't evidence |
| "Just this once" | No exceptions |
| "Lint passed" | A linter isn't a compiler |
| "The agent said it succeeded" | Verify independently |
| "I already ran things like this automatically" | Automatic habit isn't the same as evidence for this specific claim — run the actual command for it |
| "Partial check is enough" | Partial proves nothing |
| "Worded it differently, so the rule doesn't apply" | Follow the spirit, not the letter |

## Scope

Applies to **every phrasing that implies** success or completion — not just the exact words, but rephrasings and implications too. The more consumers or teams will build on this claim, the more of them the verification needs to actually cover — a green local suite proves your code works, not that every downstream caller still does. **Distinguished/Fellow angle:** when the claim underwrites a multi-year, company-wide bet — a default other orgs adopt, a primitive that gets open-sourced or shows up in a conference talk — the evidence has to be reproducible from scratch by someone with zero institutional memory, not just trusted because the person who ran it is still around to vouch for it. **Executive angle (CTO/VP-Eng):** when the claim is said to a board, regulator, or customer — "we're compliant," "the incident is contained," "we can hold this SLA" — it stops being a technical statement and becomes a contractual or legal one, so verify it against that bar before it's said out loud, because walking it back costs a contract or a headline, not a revert. If you can't run the verification, say so — "haven't run the tests yet" beats "should work."

## A note on how this model runs this skill

Two things are true at once here, and they don't cancel each other out. First: this model tends to test and verify on its own more reliably than earlier ones, so the explicit "you must test this" instructions carried over from older prompts are mostly unneeded scaffolding — remove them rather than layering them on. Second, and unrelated to that: this model is also more tentative than predecessors about declaring something actually finished, which means the exploration and verification pass itself needs an explicit stopping point stated upfront — "run the suite, fix failures, and call it done once it's green" rather than leaving it open-ended, or it can keep re-checking past the point where evidence already supports the claim. Neither of those tendencies touches the iron rule itself: a command still has to actually run, fresh, and its real output still has to be read, before anything gets called done, fixed, or passing. That part does not get easier, lighter, or more implicit for this model than for any other.
