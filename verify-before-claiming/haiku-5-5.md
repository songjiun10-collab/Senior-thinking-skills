> Tuned for Claude Haiku 5.5. Source: Anthropic prompting guide (prompting-claude-haiku-5-5). Body carried from the Sonnet file; the calibration section is Haiku-specific. See SKILL.md for the model index.

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

Skip any step and it's not verification — it's a guess. Follow these five steps as written, in full — an instruction like "run the verification" means the entire command to completion, not a subset that looks sufficient; underspecifying which command, or leaving "in full, fresh" implicit, tends to get taken literally rather than filled in generously.

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

## Scope

Applies to **every phrasing that implies** success or completion — not just the exact words, but rephrasings and implications too. The more consumers or teams will build on this claim, the more of them the verification needs to actually cover — a green local suite proves your code works, not that every downstream caller still does. **Distinguished/Fellow angle:** when the claim underwrites a multi-year, company-wide bet — a default other orgs adopt, a primitive that gets open-sourced or shows up in a conference talk — the evidence has to be reproducible from scratch by someone with zero institutional memory, not just trusted because the person who ran it is still around to vouch for it. **Executive angle (CTO/VP-Eng):** when the claim is said to a board, regulator, or customer — "we're compliant," "the incident is contained," "we can hold this SLA" — it stops being a technical statement and becomes a contractual or legal one, so verify it against that bar before it's said out loud, because walking it back costs a contract or a headline, not a revert. If you can't run the verification, say so — "haven't run the tests yet" beats "should work."

## Calibration (Anthropic official prompting guide, Haiku 5.5)

- **Effort**: `low`, `medium` (default), `high`, `xhigh`, `max`. At `low`, long agent prompts see more skipped searches, early stops, and skipped checks. Thinking can be turned off with `{type: "disabled"}` at `low`/`medium`/`high` only; at `xhigh`/`max` it is a 400.
- **Search**: send today's date, and add a nudge that training data may be stale for records, prices, versions and "latest". Avoid blanket "search for everything" instructions; they cause searches on prompts that need none.
- **JSON output with your own tools**: with thinking off, the model can skip a needed tool call. Use adaptive thinking, drop `output_config.format` on tool-calling requests, or force the call with `tool_choice`.
- **Early stopping** (long agent prompts at `low`): add an explicit keep-working line and a no-extra-scope line.
- **Coding verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn.
- **Chatbots**: add an explicit rules-hold-for-the-whole-conversation line to resist pressure from users.
- **Safeguard refusals**: categories `cyber`, `frontier_llm`, `bio`, `general_harms`. No server-side fallback, so handle `stop_reason: "refusal"` in the client.
