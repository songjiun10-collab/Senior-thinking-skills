> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Chesterton's Fence

If you see a fence blocking the road and don't know why it's there, **don't tear it down.** Understand the reason first, judge whether it still holds, then decide.

## Answer before you touch it

- What is this code's responsibility?
- What calls this, and what does this call?
- What are the edge cases and error paths?
- Is there a test that pins down the expected behavior?
- Why is it written this way? (Performance? A platform constraint? History?)
- Check `git blame` — what context did this code originate in?

**If you can't answer the above, you're not ready to touch it.** Read more context before deleting or simplifying. Treat "I can't answer this" as a real stop condition that actually gates the next action, not a formality to note and move past.

## Once you know the reason

Judge whether the reason still holds:

- Is it still true **today**, or does it no longer apply (dropped browser support, a constraint that's gone)?
- If the reason is gone, removing or simplifying is safe — **but record why it's safe** (commit message, comment)
- If the reason still holds and the code looks complex, the complexity may just be reflecting that constraint. Ask whether **the same constraint can be met in a simpler form** — don't simplify by dropping the constraint
- If the fence enforces a contract other teams or services rely on (a shared library, an API, a config format), removing it isn't a local call — confirm who else depends on it before you act, not after their build breaks.
- **Distinguished/Fellow angle:** If the reason this fence exists lives only in one person's head, write it down now — a fence whose justification depends on someone who might leave in the next reorg is a fence nobody five years from now will know is safe to remove.
- **Executive angle (CTO/VP-Eng):** If the fence exists because of a regulatory, contractual, or compliance constraint, removing it is a business-risk decision for legal/compliance to sign off on, not an engineering judgment call — the cost of guessing wrong is an audit finding or a broken customer contract, not a bug.

## Common traps

- "I don't know why this is here, but it looks unused, so delete it" — whether it's really unused usually needs **outside** confirmation (search callers, production logs, other services)
- "This is the old way, probably not needed anymore" — that's an unverified guess. Confirm it with `search-first` or `root-cause-discipline`
- Found unrelated dead code? **Mention it, don't delete it.** That's out of scope for this task (see `surgical-change`)

## Calibration for this model

With a 1.05M-token context window, there's rarely a reason to only skim `git blame` or read one caller when investigating a fence — pull the full history and every call site the question above actually needs; a mid-investigation increase in reasoning effort, or pulling in an extra tool to search more callers, doesn't reset the prompt cache, so escalate the investigation when the fence turns out to matter more than it first looked.

State the exploration scope for the investigation up front: which callers, which history, and where the investigation stops once the "answer before you touch it" questions are actually answered. This model tends to keep investigating past the point of having enough evidence, or to stop and check in for approval before actually acting on a clearly-safe conclusion — naming both the scope and what "answered enough to proceed" looks like lets it work through the investigation and then act, rather than pausing to ask when the fence has clearly already fallen or clearly still holds.

Don't add "you must verify this is really unused before deleting" as a separate reminder — this model already treats an unconfirmed "looks unused" as a guess needing outside confirmation on its own; the investigation steps above already carry that discipline. Where a "cleanup" or "remove the old check" request doesn't say whether investigation is expected, treat any deletion or simplification of unfamiliar code as implicitly requiring this skill by default — bias toward doing the investigation and acting, rather than pausing to ask whether it's wanted.
