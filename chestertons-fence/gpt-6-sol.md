> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Chesterton's Fence

If you see a fence blocking the road and don't know why it's there, **don't tear it down.** Understand the reason first, judge whether it still holds, then decide.

## Answer before you touch it

- What is this code's responsibility?
- What calls this, and what does this call?
- What are the edge cases and error paths?
- Is there a test that pins down the expected behavior?
- Why is it written this way? (Performance? A platform constraint? History?)
- Check `git blame` — what context did this code originate in?

**If you can't answer the above, you're not ready to touch it.** Read more context before deleting or simplifying. Treat "I can't answer this" as a real stop condition, not a formality to note and move past — this model follows the instruction as literally stated, so if the check is skimmed rather than actually gating the next action, it will proceed on an unanswered question instead of generously inferring that it should pause.

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

With a 1.05M-token context window, there's rarely a reason to only skim `git blame` or read one caller when investigating a fence — pull the full history and every call site the question above actually needs. Raising reasoning effort mid-investigation, once the fence turns out to be more tangled than expected, doesn't reset the prompt cache here, so it's cheap to escalate — but don't reach for the top effort level by default; a fence investigation is usually well served by a moderate level, since more effort doesn't reliably surface more of the real history.

If a request to "clean this up" or "remove the old check" doesn't explicitly say whether investigation is expected first, don't assume it's implied — this model follows what's asked fairly literally; if Chesterton's Fence should apply, say so, or treat any deletion/simplification request touching unfamiliar code as implicitly requiring it by default.

Given this model's weaker resistance to pressure around guardrails and warnings compared to the flagship tier, be more insistent than usual about the stop condition above ("if you can't answer the above, you're not ready to touch it") actually holding when the code in question is security-, auth-, or compliance-adjacent — don't let a plausible-sounding "probably fine to remove" substitute for the outside confirmation the traps section calls for.
