> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Verify Before Claiming

**Evidence comes before the claim. No exceptions.**

## Iron rule

```
If you haven't just run the verification command, you cannot say it passes.
```

"It passed earlier" is not verification. If the code changed, run it again. This rule does not soften on any model, this one included — the self-checking this model does unprompted (documented for Opus 5, carried over to 5.5) is not a substitute for actually running the command and reading real output. See the note at the end of this file for what does and doesn't change here.

## Gate function

**Immediately before** asserting the state of anything:

1. **Identify** — what command proves this claim?
2. **Run** — run that command **in full, fresh** (a partial run proves nothing)
3. **Read** — read the entire output. Check the exit code. Count the failures.
4. **Compare** — does the output support the claim?
   - No → state the actual state, with evidence
   - Yes → state the claim, with evidence
5. **Only then** claim it

Skip any step and it's not verification — it's a guess. This is a fixed five-step gate, not a place to add extra internal re-checking passes on top — one full, fresh run, read completely, is the requirement; layering redundant self-doubt loops on top of it doesn't make the evidence any more real, it just burns tokens and time.

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
- tired, want to wrap up
- reaching for a subagent to re-verify something a direct command would settle just as fast

## Rationalization blockers

| Excuse | Reality |
|---|---|
| "It should work now" | Then **run it** and check |
| "I'm confident" | Confidence isn't evidence |
| "Just this once" | No exceptions |
| "Lint passed" | A linter isn't a compiler |
| "The agent said it succeeded" | Verify independently |
| "I'm tired" | Fatigue isn't an exemption |
| "Partial check is enough" | Partial proves nothing |
| "Worded it differently, so the rule doesn't apply" | Follow the spirit, not the letter |
| "I already reasoned this through carefully" | Careful reasoning about the code isn't the same as running it — the command still has to actually execute |

## Scope

Applies to **every phrasing that implies** success or completion — not just the exact words, but rephrasings and implications too. The more consumers or teams will build on this claim, the more of them the verification needs to actually cover — a green local suite proves your code works, not that every downstream caller still does. **Distinguished/Fellow angle:** when the claim underwrites a multi-year, company-wide bet — a default other orgs adopt, a primitive that gets open-sourced or shows up in a conference talk — the evidence has to be reproducible from scratch by someone with zero institutional memory, not just trusted because the person who ran it is still around to vouch for it. **Executive angle (CTO/VP-Eng):** when the claim is said to a board, regulator, or customer — "we're compliant," "the incident is contained," "we can hold this SLA" — it stops being a technical statement and becomes a contractual or legal one, so verify it against that bar before it's said out loud, because walking it back costs a contract or a headline, not a revert. If you can't run the verification, say so — "haven't run the tests yet" beats "should work." For high-stakes claims like these, match the verification plan's coverage to the stakes explicitly — which consumers, which environments — rather than counting on an effort setting (the caller's per-request choice) to produce that depth.

## A note on over-verification

Opus 5 guidance, which Anthropic says still applies to 5.5, says the model verifies its own work unprompted and that added verification instructions cause over-verification — that part doesn't need help. What it doesn't replace is this skill's actual rule: run the command, read the real output, only then claim. That rule is not optional and does not get lighter here. What can be skipped is piling extra self-doubt prompts or redundant internal re-checking passes on top of a verification that already happened — asking the model to "double-check" a claim it already grounded in a fresh, full run mostly burns tokens and latency without adding correctness, since the checking already happened when the command was run and its output was read. The discipline to drop is stacking more internal review on top of real evidence, not the requirement to go get real evidence in the first place.

## Ending a turn is not a completion claim

Documented for Opus 5.5: on long multi-part tasks, some progress updates end the turn with text instead of a tool call while work is still owed — a summary that announces the next step without taking it, an offer to continue, a list of non-blocking decisions, or a stop because a milestone felt like a good place to report. Each of those reads to the user like "done." Before a text-only end of turn, check the task's parts against the checklist or file that tracks them: if items are open and nothing blocks them, do the next one; if you stop, say exactly which items are open and what blocks them.
