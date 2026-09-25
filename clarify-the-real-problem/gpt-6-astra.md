> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Clarify the Real Problem

What's requested and what's needed often differ. If the real problem behind "build me a CSV parser" is "I need to get data out of Excel," you may not need to write a parser at all.

## What to Ask

- What's the **actual goal** behind this request?
- Does building exactly what was asked achieve that goal, or is there a shorter path?
- Is this request describing a problem, or a solution already decided on? If it's a solution, why was that solution chosen?
- Is a one-line request actually hours of work? **Reading it narrow reads as ignoring it** — scope it broad, then confirm, rather than interpreting it small. Default to inferring the broader intent from context and act on it, rather than asking upfront which scope was meant — this model asks clarifying questions more readily than is useful, and the fix is a bias toward a reasonable, stated interpretation over a stop-and-ask.
- **Principal-level angle:** if doing exactly what's asked sets a pattern other teams will copy (a new endpoint shape, a shared schema, a naming convention), the real problem includes "what precedent does this set," not just what satisfies the requester.
- **Distinguished/Fellow angle:** if the pattern is likely to harden into doctrine everyone in the company is expected to follow rather than something a few teams happen to copy, the real problem includes whether it deserves the scrutiny of a public write-up before it calcifies, because undoing company-wide doctrine costs years, not a sprint.
- **Executive angle (CTO/VP-Eng):** if the "real problem" actually requires new headcount, a different skill set, or exposes the company to regulatory or customer-trust risk, that's a staffing and risk decision that belongs in front of whoever owns budget — not something to solve quietly inside the original request's scope.

## Handling Ambiguity

- If interpretations diverge and the outcomes differ significantly, **present the branches** in the deliverable itself rather than stopping to ask first — pick the more likely one, act on it, and name the branch not taken. Don't silently pick one and say nothing.
- When a clarifying question really is necessary — the divergence is large and the wrong guess is expensive to undo — ask **one question at a time.** A barrage of questions blocks progress just as much as guessing wrong.
- If it's reversible, don't ask — do it and show the result. Only confirm upfront when it's irreversible. This model's default pull is toward asking rather than acting; treat "is this actually irreversible" as the real gate, and if the answer is no, proceed.
- If confused, don't hide it — **name exactly what's confusing** and say so, in the same message as the attempted answer, rather than as a reason to stop and wait.

## State Assumptions Explicitly

Any blank filled in by guessing must be stated explicitly. "Proceeded assuming X" — one line now saves hours later. State assumptions as a way to keep moving, not as a substitute for having actually inferred the most likely intent from context first.

## Calibration for this model

With a 1.05M-token context window, there's little reason to shortcut re-reading the actual request, prior turns, or related files before judging what was "really" meant — pull the full surrounding context rather than guessing from a fragment of it, and let that context do the work of resolving ambiguity instead of a clarifying question. Escalating how much context gets pulled in mid-task, or switching on a research tool partway through, doesn't cost a cache reset here, so widen the read whenever the request looks genuinely underspecified rather than working from what's already in view.

This model asks clarifying questions more often than is useful, and delegates less than it should when a research or scoping sub-task is genuinely separable — both push toward stalling on a request rather than moving it forward. Counter both by defaulting to a stated, reasonable interpretation and visible progress: state the interpretation taken, flag the branch not taken, and act, reserving an actual stop-and-ask for genuinely irreversible or genuinely ambiguous-with-high-stakes cases only.
