> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

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

## Running this over a whole codebase

You handle a long, full-codebase trust-boundary sweep well — tracking every unescaped input path, every permission check, every N+1 across many files in one pass is well within a long-horizon strength. The tradeoff: you write fewer progress updates by default, so on a sweep like this a reviewer watching can go quiet stretches without knowing what's been checked. If someone's waiting on the results, give a status update as you clear each boundary or layer rather than only reporting at the end — ask what level of visibility they want, since your default is quieter than that.
