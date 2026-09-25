> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

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

- State function signatures, input/output types, and what each method guarantees — idempotency, partial-update behavior, failure semantics — before writing code. Draft this from the context you already have rather than opening with a round of clarifying questions: infer the caller's intent, write the contract, and flag the specific points that are genuinely ambiguous rather than pausing on the whole design.
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

- **State completion criteria and scope up front.** For a real interface review — walking a wide consumer surface, auditing several services for undocumented dependencies — say explicitly what "done" looks like (every listed consumer checked, the checklist above satisfied) and where the exploration stops (which services, which endpoints). Left open-ended, the review tends to stay tentative about calling itself finished rather than running long past the useful boundary; a stated scope and completion bar fixes that.
- **Default to drafting, not asking.** When a task implies a contract review or interface design without spelling out "apply the full checklist," still bring the discipline above — but don't stall on clarifying questions to get there. Infer intent from context, write the draft contract, and surface only the ambiguities that actually change the design.
- **Delegation needs to be spelled out, not assumed.** Checking many downstream consumers for undocumented reliance is naturally parallel work. State explicitly when a subagent should check one consumer's usage independently and when the check should stay in-session — left unstated, the default here leans toward doing it all directly even where splitting it out would be faster.
- **No need for extra "you must verify this" scaffolding.** Testing and verifying a drafted contract against its stated guarantees happens on its own; instructions layered on top of the checklist to force it are redundant.
- **Write the contract itself in plain, direct prose.** State the guarantee directly rather than through a contrastive frame ("returns null, not an exception" reads better as "returns null on missing input"). Keep the checklist and tables above as lists — their items are genuinely parallel — but don't reach for bullets to describe a single guarantee or a single tradeoff; a sentence does that better.
