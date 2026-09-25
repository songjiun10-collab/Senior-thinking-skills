> Tuned for Claude Fable 5.1 (and Claude Mythos 5.1, which shares its Anthropic prompting guide). See SKILL.md for the model index.

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

State the goal and constraints, not a prescriptive step-by-step design walkthrough — your own reasoning about tradeoffs between idempotency, partial-update semantics, and failure modes tends to outperform a scripted sequence handed to you one step at a time. Given the goal, work out:

- Function signatures, input/output types, and what each method guarantees (idempotency, partial updates, failure behavior) — before the code
- The error cases explicitly: what happens on a missing resource? Invalid input? How is partial failure represented?
- The call site for this contract from the caller's point of view first — is it pleasant to use?

If you're briefing this skill to someone else (or writing it into a plan another session will follow), give them the contract and constraints as a spec, not a click-by-click sequence — the same principle applies when you're the one being handed the task.

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

- **Narrate progress during a long contract review.** Working through a wide interface surface (many endpoints, many consumers to check) is exactly the kind of long agentic loop where you tend to go quiet — say explicitly what you're checking as you go, especially if someone is watching the review happen, or is relying on progress visibility to trust the result.
- This skill's discipline holds over long, autonomous stretches of design work without needing a check-in every few steps — use that; don't manufacture artificial checkpoints where the goal-and-constraints framing above already covers the ground.
