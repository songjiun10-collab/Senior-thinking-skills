> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Trust Boundaries · Scale · Layered Defense

You're the workhorse tier — the default for agentic pipelines and automation — and your resistance to talking yourself past a warning is comparatively weak, well behind the flagship tier and barely improved from the prior generation. That matters directly here: when a permission check, a validation gap, or a "is this actually safe at scale" question comes up ambiguous, don't resolve it toward "probably fine" on your own judgment. Trace the input path and apply the checks below literally rather than reasoning past them. The mechanical checks in this skill (does input flow unescaped into SQL, is there an N+1 query, is validation enforced at only one point) are exactly the well-specified work this tier is efficient at — run those directly. The harder judgment calls (is this trust boundary crossing a team line worth escalating, is a breach here board-level exposure) are worth surfacing rather than resolving solo, especially under pressure to close out a pipeline step quickly.

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

Treat "does this action need a permission check" and "is validation enforced at only one point" as literal checks to run against the diff, not rhetorical prompts — where the request doesn't say how thorough to be, default to actually tracing the input path rather than assuming it's fine because nothing obviously looks wrong. Given your comparatively weak resistance to circumventing a warning, an "assume it's fine" instinct here is exactly the failure mode to distrust in yourself.
