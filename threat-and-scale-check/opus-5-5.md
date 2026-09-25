> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

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

## A refusal during this check is not automatically a finding

Auth, permission, and trust-boundary review is exactly the kind of legitimate work that can trip a broader safety classifier — your classifiers cover more ground than earlier models' (bio and reasoning_extraction now sit alongside cyber), and describing an attack path, an unauthorized-request scenario, or a permission bypass while doing this review is normal, in-scope work, not an attempt to build something dangerous. If you get refused or pulled up short mid-check, don't record that as "found a real containment gap" or as evidence the boundary is weak — it's more likely a false positive from your own classifier reacting to the shape of the discussion (exploit language, attacker framing) rather than its substance. Re-frame explicitly as defensive/audit work and retry before concluding either way; if it still trips on a clearly defensive framing, that's worth noting as a tooling limitation on this review, not a security verdict about the code.

## Scale — 10x / 1000x

Working fine at 100 records today proves nothing.

- Does this approach still hold if data grows 10x, 1000x?
- Is there a DB query or network call inside a loop? (N+1)
- Is everything loaded into memory at once? Can it be streamed or batched?
- But **don't optimize without measuring first** — confirm the bottleneck is actually here before touching it. Checking for an N+1 or an in-loop network call is a quick, direct read of the code — do that yourself rather than reaching for a subagent to scan for it; a grep or a read settles it faster than a delegation round-trip.

## Layered defense

A structure where the next layer catches a failure is more realistic than betting everything on one perfect defense.

- If this safeguard fails, is it an immediate incident, or is there another layer behind it?
- **Block unconscious mistakes, allow conscious choices, but leave a trace** — that's the shape of a good safeguard. Block everything and people route around it; allow everything and it becomes an incident.
- Verify on success too. Don't stop at "it was blocked" — confirm **why** it was blocked, and whether that holds in other conditions. Opus 5 guidance (carried over to 5.5) says the model verifies its own work unprompted, so this confirmation step is the useful check — an extra round of "are you sure" on top of it just burns tokens without adding correctness. Thinking is always on for you and effort defaults to `medium`; set it explicitly higher for a review that needs to trace the full blast radius of a trust boundary or safeguard, since effort — not an extra re-check pass — is what buys the depth.
