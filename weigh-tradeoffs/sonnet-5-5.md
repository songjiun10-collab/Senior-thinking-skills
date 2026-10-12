> Tuned for Claude Sonnet 5.5. Source: Anthropic prompting guide (prompting-claude-sonnet-5-5). See SKILL.md for the model index.

# Tradeoffs and Decision Weight

## First: How Heavy Is This Decision

Not every decision deserves the same amount of time.

- **Easily reversible decisions** (a function's internal implementation, file location, variable names) → build it, don't agonize, fix later.
- **Hard-to-reverse decisions** (DB schema, public API, data format, core dependency, an interface already shipped) → spend more time, take alternatives seriously.

Confirmation follows the same tier: reversible → just do it; irreversible → confirm first. **Gate everything at the same weight, and the gate itself gets ignored.** Be explicit about which tier a decision falls into when handing it off or asking for confirmation — this model follows what's stated rather than generously inferring the weight of an underspecified request, so naming the tier out loud (not just implying it) is what actually triggers the right amount of deliberation.

## How to Compare

- Lay out the pros and cons of 2-3 real alternatives **in one line each**: speed vs. complexity, flexibility vs. learning curve, easier now vs. easier later, performance vs. readability.
- Don't pick something reflexively because it's familiar. Familiarity is a legitimate advantage, but it has to be a **stated** one.
- Look at the cost of each alternative being wrong. If the cost is asymmetric (one is easy to reverse, the other isn't), that's usually the deciding factor.
- **Principal-level angle:** for a decision other teams will build against (a shared schema, a public API, a dependency others will also adopt), weigh org-level cost too — migration cost across consumers, and whether it's the direction you want other teams defaulting to for the next few quarters, not just whether it's right for this one codebase.
- **Distinguished/Fellow-level angle:** for a multi-year, company-wide bet (a protocol or format other companies might also converge on), weigh whether it still holds up to someone joining in five years with none of today's context, and whether explaining it depends on people who might not be around to ask.
- **Executive angle (CTO/VP-Eng):** put total cost of ownership on the table, not just engineering effort — license fees, infra spend, and the opportunity cost of the team that would build and maintain it are what a CFO or board asks about before the technical merits.

## Record the Reason

- Leave **one or two sentences** on why this was chosen — in a code comment, commit message, or design note.
- It should answer "why did we do it this way?" six months from now. If it can't, the next person just rips it out.
- **Record the rejected alternatives too.** Without knowing why they weren't used, the next person walks down the same path again.

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
