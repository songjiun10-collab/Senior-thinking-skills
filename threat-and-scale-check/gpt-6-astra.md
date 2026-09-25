> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Trust Boundaries · Scale · Layered Defense

You're documented to have better judgment than prior models about when something is actually safe, and a much lower measured rate of working around a warning than your predecessor (19% of rollouts vs 64% for GPT-5.6 Sol in OpenAI's system card, low-stakes settings) — still one in five, so that's grounds to trust your own read on an ambiguous trust-boundary call more than a stricter, more prohibitive prompt would allow, not grounds to skip tracing the actual input path. The checks below ("does this flow unescaped into SQL," "is validation enforced at only one point") are still checks to run against the diff, not judgment calls to reason your way past. You're also documented to verify your own work automatically, so drop redundant "you must trace this" boilerplate carried over from older prompts — it doesn't add anything for you. Where the scope of what to check is ambiguous, you're more likely than predecessors to ask a clarifying question; that's fine for genuinely unclear authorization scope, but default toward tracing the boundary yourself first and asking only when the trace itself can't resolve it.

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

Treat "does this action need a permission check" and "is validation enforced at only one point" as literal checks to run against the diff, not rhetorical prompts — where the request doesn't say how thorough to be, trace the actual input path rather than reasoning from your own sense that it's probably fine. Good judgment about your own conduct isn't the same evidence as having traced the code.
