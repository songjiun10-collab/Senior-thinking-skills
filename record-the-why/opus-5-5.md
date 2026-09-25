> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

# Record the why

Code shows **what** was done, not **why**. Six months from now, whoever runs into that decision again (usually you) can't answer "why is this like this?" from the code alone.

Thinking is always on for this model, but effort — not thinking — is the depth control, and it defaults to `medium`. In Anthropic's testing `medium` on 5.5 matched or beat Opus 5 at `high`, so the default is usually enough; for a record that carries real weight (an architectural call, a reversed decision), the depth comes mainly from answering the rejected-alternatives questions below, not from a higher setting.

## When to record it

- When you make a decision that's **expensive to reverse**: an architectural choice, a public API or data format change, a library pick
- When you reverse an earlier decision — especially why the old approach stopped fitting
- When you wrote unnatural-looking code to work around a non-obvious constraint (the spot where someone will look and think "why is this written this way?")
- Principal angle: when the decision sets a **precedent** other teams or future features will copy — record it even if this instance alone would be trivially reversible, because the pattern it establishes isn't
- Distinguished/Fellow angle: if the person who made this call could leave tomorrow, the record has to stand on its own — legible to someone joining the company in five years with zero institutional memory of the meeting where this was decided
- Executive angle (CTO/VP-Eng): if the decision moves headcount, vendor/infra spend, or carries regulatory exposure, the record needs to be legible to a board or investor audit and traceable to the budget line it justified — not just clear to the next engineer

Skip it where the code explains itself (naming, function decomposition already do the job) — a comment that just restates the code is noise. Don't pad a simple decision into a longer document than it needs just because more depth is available — Opus 5 guidance (still applicable to 5.5) notes written deliverables run longer than needed, and an ADR is not exempt: match the record's length to the decision's actual weight.

## Where to record it

- Check this repo's existing convention first (an ADR directory, design docs, commit message format) and match it — don't invent a new format
- No convention → at minimum, in the commit message or a comment near the code: **decision + rejected alternatives + reasoning**
- If `weigh-tradeoffs` already compared the alternatives, carry that result over as-is — don't rewrite it

## Never delete the record

- When a decision changes, don't delete and rewrite the old record — **overturn it with a new one.** Why it changed is itself information a future reader (or another team hitting the same tradeoff) needs.
- "I'll clean it up later" means the context at that moment — why this was the best call then — is gone for good. Right after the decision is the cheapest time to write it down.

This model already reasons through tradeoffs and writes a solid first draft on its own — once the record is written, don't add a second "double-check your reasoning" pass on top of it; that's wasted latency, not a better record. Put the effort into the initial write.
