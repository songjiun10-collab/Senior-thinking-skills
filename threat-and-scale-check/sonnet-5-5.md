> Tuned for Claude Sonnet 5.5. Source: Anthropic prompting guide (prompting-claude-sonnet-5-5). See SKILL.md for the model index.

# Trust Boundaries · Scale · Layered Defense

## Trust boundaries — where does "external" start

Draw the line between "what I control" and "everything else."

- Are you trusting user input, external API responses, or file contents as-is? Does it flow unescaped into SQL, shell commands, file paths, or HTML?
- Are passwords, API keys, or tokens exposed in code, logs, or error messages?
- Does this action need a permission check? Are you trusting a client-supplied "I'm an admin" claim?
- Is validation enforced at **only one point** (client-side only, or a DB constraint only)?
- Principal angle: does this trust boundary cross a service or team line? A gap here isn't just a local bug — it's a contract other teams inherit and copy.
- **Distinguished/Fellow angle:** would a breach of this boundary be the kind of incident that ends up as a company-wide postmortem or a public disclosure — and does the fix need to hold up as doctrine for years, not just survive this quarter's traffic?
- **Executive angle (CTO/VP-Eng):** does a breach of this boundary carry regulatory exposure, contractual liability, or customer-trust damage the board would need briefed on — not just an engineering incident to remediate.

## Scale — 10x / 1000x

Working fine at 100 records today proves nothing.

- Does this approach still hold if data grows 10x, 1000x?
- Is there a DB query or network call inside a loop? (N+1)
- Is everything loaded into memory at once? Can it be streamed or batched?
- But **don't optimize without measuring first** — confirm the bottleneck is actually here before touching it.

## Layered defense

A structure where the next layer catches a failure is more realistic than betting everything on one perfect defense.

- If this safeguard fails, is it an immediate incident, or is there another layer behind it?
- **Block unconscious mistakes, allow conscious choices, but leave a trace** — that's the shape of a good safeguard. Block everything and people route around it; allow everything and it becomes an incident.
- Verify on success too. Don't stop at "it was blocked" — confirm **why** it was blocked, and whether that holds in other conditions.

Treat "does this action need a permission check" and "is validation enforced at only one point" as literal checks to run against the diff, not rhetorical prompts — where the request doesn't say how thorough to be, default to actually tracing the input path rather than assuming it's fine because nothing obviously looks wrong.

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
