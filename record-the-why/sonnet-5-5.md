> Tuned for Claude Sonnet 5.5. Source: Anthropic prompting guide (prompting-claude-sonnet-5-5). See SKILL.md for the model index.

# Record the why

Code shows **what** was done, not **why**. Six months from now, whoever runs into that decision again (usually you) can't answer "why is this like this?" from the code alone.

## When to record it

- When you make a decision that's **expensive to reverse**: an architectural choice, a public API or data format change, a library pick
- When you reverse an earlier decision — especially why the old approach stopped fitting
- When you wrote unnatural-looking code to work around a non-obvious constraint (the spot where someone will look and think "why is this written this way?")
- Principal angle: when the decision sets a **precedent** other teams or future features will copy — record it even if this instance alone would be trivially reversible, because the pattern it establishes isn't
- Distinguished/Fellow angle: if the person who made this call could leave tomorrow, the record has to stand on its own — legible to someone joining the company in five years with zero institutional memory of the meeting where this was decided
- Executive angle (CTO/VP-Eng): if the decision moves headcount, vendor/infra spend, or carries regulatory exposure, the record needs to be legible to a board or investor audit and traceable to the budget line it justified — not just clear to the next engineer

Skip it where the code explains itself (naming, function decomposition already do the job) — a comment that just restates the code is noise.

## Where to record it

- Check this repo's existing convention first (an ADR directory, design docs, commit message format) and match it — don't invent a new format
- No convention → at minimum, in the commit message or a comment near the code: **decision + rejected alternatives + reasoning**
- If `weigh-tradeoffs` already compared the alternatives, carry that result over as-is — don't rewrite it

This model follows instructions more literally than prior generations, so if the ask is "record the why," name what that should actually include — decision, rejected alternatives, reasoning — rather than assuming those three parts will be filled in without being asked for.

## Never delete the record

- When a decision changes, don't delete and rewrite the old record — **overturn it with a new one.** Why it changed is itself information a future reader (or another team hitting the same tradeoff) needs.
- "I'll clean it up later" means the context at that moment — why this was the best call then — is gone for good. Right after the decision is the cheapest time to write it down.

## Calibration (Anthropic official prompting guide, Sonnet 5.5)

- **Effort**: default is `high` on the Claude API. Levels are recalibrated from Sonnet 5, so re-run an effort sweep rather than carrying over the old setting. Start at `medium` for agentic coding and well-specified multistep tool use; `medium` or `low` for chat.
- **Low effort skips verification and stops early**: at `low`, the model may skip checks and, at `low`/`medium` on long agentic tasks, check in before finishing. Add an explicit "keep working until done, stop only before a risky step" line rather than assuming it will carry work through.
- **Thinking off**: send `thinking: {type: "between_tools"}` at `high` effort or below. `{type: "disabled"}` is a 400. Per-message effort changes need adaptive thinking.
- **Structured JSON on multistep reasoning**: prefer structured outputs; otherwise ask the model to think first and parse the last JSON value, treating `stop_reason: "max_tokens"` as failure.
- **Progress visibility**: set `display: "updates"` to surface between-tool-call notes.
- **Search**: tell it to check specifics that may have changed (what is allowed, required, or charged), even when confident.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn. Keep harness reminders in a separate system message, so the model doesn't mistake real user input for injection.
- **Verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Safeguard refusals**: categories `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`. Remove prompt instructions that ask it to reproduce its reasoning in the reply.
