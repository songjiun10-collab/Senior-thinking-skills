---
name: clarify-the-real-problem
description: Dig out the actual goal behind a request before building anything. Use when a request is ambiguous, when the literal ask smells like an X-Y problem (they asked for a solution, not a problem), or when a wrong interpretation would waste significant work. Also use when the user says "still thinking about it", "what's the best way to do this?", or hands over a vague one-liner that implies hours of work.
---

# Clarify the Real Problem

What's requested and what's needed often differ. If the real problem behind "build me a CSV parser" is "I need to get data out of Excel," you may not need to write a parser at all.

## What to Ask

- What's the **actual goal** behind this request?
- Does building exactly what was asked achieve that goal, or is there a shorter path?
- Is this request describing a problem, or a solution already decided on? If it's a solution, why was that solution chosen?
- Is a one-line request actually hours of work? **Reading it narrow reads as ignoring it** — scope it broad, then confirm, rather than interpreting it small.
- **Principal-level angle:** if doing exactly what's asked sets a pattern other teams will copy (a new endpoint shape, a shared schema, a naming convention), the real problem includes "what precedent does this set," not just what satisfies the requester.
- **Distinguished/Fellow angle:** if the pattern is likely to harden into doctrine everyone in the company is expected to follow rather than something a few teams happen to copy, the real problem includes whether it deserves the scrutiny of a public write-up before it calcifies, because undoing company-wide doctrine costs years, not a sprint.
- **Executive angle (CTO/VP-Eng):** if the "real problem" actually requires new headcount, a different skill set, or exposes the company to regulatory or customer-trust risk, that's a staffing and risk decision that belongs in front of whoever owns budget — not something to solve quietly inside the original request's scope.

## Handling Ambiguity

- If interpretations diverge and the outcomes differ significantly, **present the branches.** Don't silently pick one and proceed.
- When asking back, **one question at a time.** A barrage of questions blocks progress just as much as guessing wrong.
- If it's reversible, don't ask — do it and show the result. Only confirm upfront when it's irreversible.
- If confused, don't hide it — **name exactly what's confusing** and say so.

## State Assumptions Explicitly

Any blank filled in by guessing must be stated explicitly. "Proceeded assuming X" — one line now saves hours later.
