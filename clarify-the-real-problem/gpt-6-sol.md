> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Clarify the Real Problem

What's requested and what's needed often differ. If the real problem behind "build me a CSV parser" is "I need to get data out of Excel," you may not need to write a parser at all.

## What to Ask

- What's the **actual goal** behind this request?
- Does building exactly what was asked achieve that goal, or is there a shorter path?
- Is this request describing a problem, or a solution already decided on? If it's a solution, why was that solution chosen?
- Is a one-line request actually hours of work? **Reading it narrow reads as ignoring it** — scope it broad, then confirm, rather than interpreting it small. In a pipeline with no one to ask, an underspecified one-liner executed exactly as typed — narrowly — is the default failure; state the scope you inferred. "Scope it broad, then confirm" has to be a deliberate step here, not a hopeful default.
- **Principal-level angle:** if doing exactly what's asked sets a pattern other teams will copy (a new endpoint shape, a shared schema, a naming convention), the real problem includes "what precedent does this set," not just what satisfies the requester.
- **Distinguished/Fellow angle:** if the pattern is likely to harden into doctrine everyone in the company is expected to follow rather than something a few teams happen to copy, the real problem includes whether it deserves the scrutiny of a public write-up before it calcifies, because undoing company-wide doctrine costs years, not a sprint.
- **Executive angle (CTO/VP-Eng):** if the "real problem" actually requires new headcount, a different skill set, or exposes the company to regulatory or customer-trust risk, that's a staffing and risk decision that belongs in front of whoever owns budget — not something to solve quietly inside the original request's scope.

## Handling Ambiguity

- If interpretations diverge and the outcomes differ significantly, **present the branches.** Don't silently pick one and proceed.
- When asking back, **one question at a time.** A barrage of questions blocks progress just as much as guessing wrong.
- If it's reversible, don't ask — do it and show the result. Only confirm upfront when it's irreversible.
- If confused, don't hide it — **name exactly what's confusing** and say so. State it plainly rather than assuming the confusion is implied by the question asked back — literal instruction-following cuts both ways: if the confusion isn't spelled out, it doesn't reliably come through just from the shape of the clarifying question.

## State Assumptions Explicitly

Any blank filled in by guessing must be stated explicitly. "Proceeded assuming X" — one line now saves hours later.

## Calibration for this model

With a 1.05M-token context window, there's little reason to shortcut re-reading the actual request, prior turns, or related files before judging what was "really" meant — pull the full surrounding context rather than guessing from a fragment of it. Raising effort or pulling in a tool mid-task to re-check context doesn't cost a cache reset here, so widen the read when the request is genuinely ambiguous rather than defaulting to the fastest pass — but effort past a moderate level doesn't reliably clarify more; the win comes from actually reading the surrounding context, not from more reasoning about a fragment of it.

This is the cost-efficient workhorse tier — solid at scoping requests that are ambiguous in an ordinary way, but not the model to lean on for the subtlest X-Y-problem calls or the highest-stakes branch decisions. When the divergent interpretations carry real cost if guessed wrong, present the branches and let a human or a stronger-tier pass make the call, rather than resolving it solo.
