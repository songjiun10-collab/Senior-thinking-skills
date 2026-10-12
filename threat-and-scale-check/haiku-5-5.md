> Tuned for Claude Haiku 5.5. Source: Anthropic prompting guide (prompting-claude-haiku-5-5). Body carried from the Sonnet file; the calibration section is Haiku-specific. See SKILL.md for the model index.

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

## Calibration (Anthropic official prompting guide, Haiku 5.5)

- **Effort**: `low`, `medium` (default), `high`, `xhigh`, `max`. At `low`, long agent prompts see more skipped searches, early stops, and skipped checks. Thinking can be turned off with `{type: "disabled"}` at `low`/`medium`/`high` only; at `xhigh`/`max` it is a 400.
- **Search**: send today's date, and add a nudge that training data may be stale for records, prices, versions and "latest". Avoid blanket "search for everything" instructions; they cause searches on prompts that need none.
- **JSON output with your own tools**: with thinking off, the model can skip a needed tool call. Use adaptive thinking, drop `output_config.format` on tool-calling requests, or force the call with `tool_choice`.
- **Early stopping** (long agent prompts at `low`): add an explicit keep-working line and a no-extra-scope line.
- **Coding verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn.
- **Chatbots**: add an explicit rules-hold-for-the-whole-conversation line to resist pressure from users.
- **Safeguard refusals**: categories `cyber`, `frontier_llm`, `bio`, `general_harms`. No server-side fallback, so handle `stop_reason: "refusal"` in the client.
