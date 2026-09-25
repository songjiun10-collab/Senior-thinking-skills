> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Clarify the Real Problem

What's requested and what's needed often differ. If the real problem behind "build me a CSV parser" is "I need to get data out of Excel," you may not need to write a parser at all.

## What to Ask

- What's the **actual goal** behind this request?
- Does building exactly what was asked achieve that goal, or is there a shorter path?
- Is this request describing a problem, or a solution already decided on? If it's a solution, why was that solution chosen?
- Is a one-line request actually hours of work? **Reading it narrow reads as ignoring it** — scope it broad, then confirm, rather than interpreting it small. State the scope explicitly — a one-liner executed exactly as typed is the default failure for a focused, high-volume worker.
- **Principal-level angle:** if doing exactly what's asked sets a pattern other teams will copy (a new endpoint shape, a shared schema, a naming convention), the real problem includes "what precedent does this set," not just what satisfies the requester.
- **Distinguished/Fellow angle:** if the pattern is likely to harden into doctrine everyone in the company is expected to follow rather than something a few teams happen to copy, the real problem includes whether it deserves the scrutiny of a public write-up before it calcifies, because undoing company-wide doctrine costs years, not a sprint.
- **Executive angle (CTO/VP-Eng):** if the "real problem" actually requires new headcount, a different skill set, or exposes the company to regulatory or customer-trust risk, that's a staffing and risk decision that belongs in front of whoever owns budget — not something to solve quietly inside the original request's scope.

For this model, the deeper diagnostic work here — is this an X-Y problem, what precedent does it set, does it actually require new headcount — is best treated as a checklist to run and report on, with the actual judgment call on ambiguous or high-stakes branches escalated rather than resolved solo (see the calibration note).

## Handling Ambiguity

- If interpretations diverge and the outcomes differ significantly, **present the branches.** Don't silently pick one and proceed.
- When asking back, **one question at a time.** A barrage of questions blocks progress just as much as guessing wrong.
- If it's reversible, don't ask — do it and show the result. Only confirm upfront when it's irreversible.
- If confused, don't hide it — **name exactly what's confusing** and say so.

## State Assumptions Explicitly

Any blank filled in by guessing must be stated explicitly. "Proceeded assuming X" — one line now saves hours later.

## Calibration for this model

With a 1.05M-token context window, the full request, prior turns, and related files can stay in view rather than being read as a fragment — use that to at least identify when a request is ambiguous, even where resolving the ambiguity is better left to a stronger model.

This is the fastest, cheapest tier, and it fits well-specified, narrow requests — OpenAI's "focused, repeatable tasks" — where "the real problem" is quickly and clearly the same as "the stated problem." It's a weaker fit for teasing apart a genuine X-Y problem in a vague, multi-paragraph request, or for judging a Distinguished/Fellow- or Executive-level branch. For those, flag the ambiguity and the candidate interpretations, and route the actual clarifying judgment to a stronger model or the human directly rather than guessing.
