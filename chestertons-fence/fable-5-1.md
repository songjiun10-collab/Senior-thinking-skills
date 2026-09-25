> Tuned for Claude Fable 5.1 (and Claude Mythos 5.1, which shares its Anthropic prompting guide). See SKILL.md for the model index.

# Chesterton's Fence

If you see a fence blocking the road and don't know why it's there, **don't tear it down.** Understand the reason first, judge whether it still holds, then decide.

## Answer before you touch it

- What is this code's responsibility?
- What calls this, and what does this call?
- What are the edge cases and error paths?
- Is there a test that pins down the expected behavior?
- Why is it written this way? (Performance? A platform constraint? History?)
- Check `git blame` — what context did this code originate in?

**If you can't answer the above, you're not ready to touch it.** Read more context before deleting or simplifying. State this as the goal — understand the fence fully before acting — rather than a rigid checklist order; this model's own investigation often finds the actual originating context (a linked issue, an old migration, a comment three call-levels up) faster by following the trail than by working through the six questions in sequence. It handles a long, multi-hop investigation (blame history across several commits, tracing a call chain across services) well in a single continuous pass.

**Ask explicitly if you want to see the investigation unfold.** This model writes fewer updates between steps by default in a long chain like this one — it may go quiet through the whole blame-and-trace process and surface only once it has an answer. If you want to know what it's finding as it goes (useful when a fence's history looks like it might be genuinely load-bearing), ask for a running narration; it won't produce one unprompted.

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

The record of *why* the fence is safe to remove (or why it must stay) should stay as plain, explicit prose in the commit message or comment — this model uses lighter markdown formatting by default, which is fine for its own reasoning trail but the recorded justification itself still needs to read clearly to the next person, so write it as a direct sentence rather than relying on structure to carry the meaning.
