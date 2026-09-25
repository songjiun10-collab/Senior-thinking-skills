> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Interface contracts

## Hyrum's Law

> With a sufficient number of API consumers, it does not matter what you promise in the contract — **all observable behavior** of your system will be depended on by somebody.

Undocumented quirks, exact error message wording, ordering, even timing — **everything visible becomes a de facto contract.** What that means in practice:

- Be **deliberate** about what you expose. Every observable behavior is a potential promise.
- Don't let implementation details leak. If it's visible, someone will depend on it.
- Anything that's hard to remove later — plan to remove it (or never expose it) **at design time.**
- Passing tests isn't the same as safe. Even a perfect contract test suite doesn't stop a "safe" change from breaking a consumer who depended on undocumented behavior.
- Principal angle: this is exactly how cross-team blast radius happens — a field, an ordering, or an error string never meant as a promise gets consumed by another team's service, and now your "internal" change is their incident.

## Define the interface first

Write the contract before the implementation. The contract is the spec; the implementation just satisfies it.

- Write function signatures, input/output types, and what each method guarantees **explicitly** — idempotency, partial-update behavior, failure semantics — before the code. Spell these out rather than leaving them implied: an underspecified contract gets followed exactly as written, gaps and all, not generously filled in.
- Spell out error cases explicitly: what happens on a missing resource? Invalid input? How is partial failure represented?
- Write the call site for this contract from the caller's point of view first — is it pleasant to use?

## One-version rule

Never make consumers choose between multiple versions of the same dependency or API. Different consumers wanting different versions creates a diamond-dependency problem. Always design for a world where exactly one version exists — extend it, don't fork it.

## Checklist

- Does this interface expose anything that could **unintentionally** become a promise? (error message wording, return ordering, internal type names)
- How painful would it be to change this later? If it's painful, design more carefully now.
- Is the shape and ownership of data crossing this boundary clear? Is it hard to misuse?
- Does this change break an existing consumer's **undocumented** observed behavior? Ask this regardless of whether the tests pass.
- Principal angle: for a widely-consumed interface, a breaking change isn't just a code diff — it's a migration you're imposing on every team downstream. Weigh a deprecation window and a communicated migration path as part of the design, not as cleanup after the fact.
- Distinguished/Fellow angle: if this becomes the pattern every service in the company copies, the real question is whether other teams can operate it correctly five years out without you personally there to explain the edge cases.
- Executive angle (CTO/VP-Eng): a promise baked into a public interface is a standing support and liability cost — weigh what it takes to keep honoring it (or the customer/contractual fallout of breaking it) against the convenience of shipping it now.

## Calibration notes

- When a task involves designing or reviewing an interface, say so explicitly — don't rely on this tier to infer the full checklist from a vague "clean this up."
- **This tier fits a narrow, well-specified piece of a contract review, not the whole judgment call.** Use it for a bounded leg — checking one endpoint against a written contract, confirming one field's type matches the spec, scanning one consumer's call sites for a specific pattern — rather than the open-ended "is this interface well-designed" question, which needs more headroom than this tier is built for.
- Give it the contract explicitly rather than leaving it to infer one: state the exact guarantees to check (idempotency, error shape, field names) up front. It's well-suited to verifying a checklist item against given criteria; it's not the model to trust with drafting the criteria themselves for a genuinely ambiguous or high-stakes interface.
- Keep reasoning effort low for this kind of bounded check — the task doesn't call for deep exploration, and pushing effort up here mainly adds latency without a matching gain in judgment quality on the harder calls this tier isn't suited for anyway.
