> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Chesterton's Fence

If you see a fence blocking the road and don't know why it's there, **don't tear it down.** Understand the reason first, judge whether it still holds, then decide.

## Answer before you touch it

- What is this code's responsibility?
- What calls this, and what does this call?
- What are the edge cases and error paths?
- Is there a test that pins down the expected behavior?
- Why is it written this way? (Performance? A platform constraint? History?)
- Check `git blame` — what context did this code originate in?

**If you can't answer the above, you're not ready to touch it.** Read more context before deleting or simplifying. This investigation is often faster done directly — a targeted `git blame`, grep for callers, a read of the test file — than dispatched to a subagent; Opus 5 guidance, which Anthropic says still applies to Opus 5.5, documents delegating more readily than earlier models, including for legs of an investigation a direct read would close out faster. Reach for a subagent here only when the fence's history spans enough files or services that a parallel search genuinely beats a sequential one.

## Once you know the reason

Judge whether the reason still holds:

- Is it still true **today**, or does it no longer apply (dropped browser support, a constraint that's gone)?
- If the reason is gone, removing or simplifying is safe — **but record why it's safe** (commit message, comment)
- If the reason still holds and the code looks complex, the complexity may just be reflecting that constraint. Ask whether **the same constraint can be met in a simpler form** — don't simplify by dropping the constraint. This is exactly the situation where the instinct to add a cleaner abstraction on top, rather than just meeting the existing constraint more simply, tends to show up. Resolve to the narrowest simplification that respects the constraint, not the most elegant one that quietly drops it.
- If the fence enforces a contract other teams or services rely on (a shared library, an API, a config format), removing it isn't a local call — confirm who else depends on it before you act, not after their build breaks.
- **Distinguished/Fellow angle:** If the reason this fence exists lives only in one person's head, write it down now — a fence whose justification depends on someone who might leave in the next reorg is a fence nobody five years from now will know is safe to remove.
- **Executive angle (CTO/VP-Eng):** If the fence exists because of a regulatory, contractual, or compliance constraint, removing it is a business-risk decision for legal/compliance to sign off on, not an engineering judgment call — the cost of guessing wrong is an audit finding or a broken customer contract, not a bug.

## Common traps

- "I don't know why this is here, but it looks unused, so delete it" — whether it's really unused usually needs **outside** confirmation (search callers, production logs, other services)
- "This is the old way, probably not needed anymore" — that's an unverified guess. Confirm it with `search-first` or `root-cause-discipline`
- Found unrelated dead code? **Mention it, don't delete it.** That's out of scope for this task (see `surgical-change`)
- "This fence is fine, but while I'm here I'll wrap it in a cleaner interface" — an unrequested abstraction layered on top of a fence you were only asked to investigate. If the fence still stands after judgment, leave its shape alone unless the task actually asked for a redesign.

## Calibration for this model

**A refusal while investigating auth checks, permission gates, or other security-shaped fences may be a false positive, not a real block.** This model runs safety classifiers (biology, cybersecurity, reasoning extraction); finding vulnerabilities in source code is explicitly allowed, so a `stop_reason: "refusal"` on legitimate investigation of "why does this access check exist" is likely a false positive. Retry with a more explicitly scoped, clearly-legitimate framing before concluding the investigation itself is out of bounds.

**Set effort deliberately for the judgment call, not just the investigation.** Answering "what calls this" is mechanical; judging whether the original reason still holds is the part worth real thinking effort. Thinking is always on here but defaults to medium — raise it for the "once you know the reason" judgment on anything hard-to-reverse (shared library, public contract, compliance-adjacent code), not for the fact-gathering pass.
