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

**If you can't answer the above, you're not ready to touch it.** Read more context before deleting or simplifying. Treat "I can't answer this" as a real stop condition, not a formality to note and move past — if the check is skimmed rather than actually gating the next action, the work proceeds on an unanswered question.

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

With a 1.05M-token context window, there's rarely a reason to only skim `git blame` or read one caller when investigating a fence — pull the full history and every call site the question above actually needs. If a fence turns out to be more tangled than the effort level this investigation started at can handle, that's a signal to flag explicitly and re-run the investigation as a new request at higher effort — effort is fixed by the caller when a request starts, not something to raise from inside the current one, but a mid-conversation effort change no longer resets the prompt cache, so there's no cost reason to hold off on that re-run. Don't default that next attempt to the top effort level either; a fence investigation is usually well served by a moderate level — a higher setting costs more without a guaranteed matching gain, and the win here comes from reading more of the actual history, not from more reasoning about the fragment already in hand.

If a request to "clean this up" or "remove the old check" doesn't explicitly say whether investigation is expected first, don't assume it's implied — if Chesterton's Fence should apply, say so, or treat any deletion/simplification request touching unfamiliar code as implicitly requiring it by default.

Given that on OpenAI's Respecting Warnings evaluation GPT-6 Sol showed only "a modest reduction in failures" from GPT-5.6 Sol, which worked around the barrier in 64% of rollouts (GPT-6 Astra: 19%; low-stakes settings, no system-level controls), be more insistent than usual about the stop condition above ("if you can't answer the above, you're not ready to touch it") actually holding when the code in question is security-, auth-, or compliance-adjacent — don't let a plausible-sounding "probably fine to remove" substitute for the outside confirmation the traps section calls for.
