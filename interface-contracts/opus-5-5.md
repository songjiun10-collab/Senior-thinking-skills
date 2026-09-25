> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

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

- Write function signatures, input/output types, and what each method guarantees (idempotency, partial updates, failure behavior) before the code
- Spell out error cases explicitly: what happens on a missing resource? Invalid input? How is partial failure represented?
- Write the call site for this contract from the caller's point of view first — is it pleasant to use?
- **Keep the contract itself minimal.** Your default lean is toward adding flexibility the caller didn't ask for — an extra config knob, a generic abstraction layer, an options object with fields nobody requested. Every one of those is a promise the moment it ships. Write only the contract the current callers need; don't design in headroom for hypothetical future ones.

## One-version rule

Never make consumers choose between multiple versions of the same dependency or API. Different consumers wanting different versions creates a diamond-dependency problem. Always design for a world where exactly one version exists — extend it, don't fork it.

## Checklist

- Does this interface expose anything that could **unintentionally** become a promise? (error message wording, return ordering, internal type names)
- How painful would it be to change this later? If it's painful, design more carefully now.
- Is the shape and ownership of data crossing this boundary clear? Is it hard to misuse?
- Does this change break an existing consumer's **undocumented** observed behavior? Ask this regardless of whether the tests pass.
- Did you add anything here — a flag, a fallback path, an extra layer of indirection — that no current caller asked for? Cut it. Extra surface is extra promise, and it's the default failure mode to watch for on this contract review, not a maybe.
- Principal angle: for a widely-consumed interface, a breaking change isn't just a code diff — it's a migration you're imposing on every team downstream. Weigh a deprecation window and a communicated migration path as part of the design, not as cleanup after the fact.
- Distinguished/Fellow angle: if this becomes the pattern every service in the company copies, the real question is whether other teams can operate it correctly five years out without you personally there to explain the edge cases.
- Executive angle (CTO/VP-Eng): a promise baked into a public interface is a standing support and liability cost — weigh what it takes to keep honoring it (or the customer/contractual fallout of breaking it) against the convenience of shipping it now.

## Calibration notes

- **Set effort explicitly for a real contract review.** Your default effort is `medium`, one step below what a genuinely tricky interface decision (a public API boundary, a cross-team contract) deserves — bump it up when the stakes are that high, since brevity in the response doesn't drop much on its own at lower effort.
- **Don't over-verify a contract you've already reasoned through carefully.** You self-check well already; re-running the same "does this leak an implementation detail" pass three times over adds latency without catching more.
- **Read the code yourself before reaching for a subagent.** For questions like "what does this endpoint currently return" or "is this field already relied on elsewhere," a direct grep or file read settles it faster than delegating.
