> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Complexity budget

Treat complexity like a budget. Every bit you spend now, you pay back with interest later.

You're built for high-volume, narrow, well-specified work — classification, extraction, routing, structured summarization — not for the ambiguous, structural calls where "does this abstraction earn its cost" is itself a judgment call. That's actually a natural fit for this skill: the well-specified leg of a task is exactly where the simplest implementation is also the correct one, and you should default to the flattest, most literal solution the request describes rather than reaching for a layer of structure to handle cases nobody asked about. Where a task drifts into judgment-heavy territory — should this be its own module, does this justify a new dependency, is this abstraction going to become an org-wide pattern — that call belongs to a more capable tier; flag it rather than deciding it yourself.

## YAGNI — don't build what isn't needed now

Abstractions, config options, extension points added "in case it's needed later" mostly go unused — and in the meantime make the code harder to read **today**.

- Is this feature, parameter, or layer needed **now**?
- Are you designing on top of a guess like "we might swap the DB someday"?
- Cut anything unrequested: abstractions built for a single call site, error handling for cases that can't happen
- Extensibility isn't something you build in now — it's a structure that stays **easy to extend later**
- Principal angle: an abstraction or config knob added here becomes the template other teams copy once it ships — a speculative extension point left in shared/library code costs more than the same thing in a leaf module, because someone else will build on the wrong joint
- Distinguished/Fellow angle: an abstraction placed in a company-wide foundation risks becoming the thing that shows up in a conference talk or gets open-sourced — budget its complexity against years and every team in the org, not one quarter's roadmap
- Executive angle (CTO/VP-Eng): weigh the complexity against total cost of ownership — the infra spend, licensing, and specialized headcount it takes to run and hire for — not just the engineering hours to build it

## Complexity check

- Is there a way to solve this with **half the code**? If 200 lines can become 50, rewrite it
- "Would a senior engineer call this overcomplicated?" — if yes, simplify. If you're unsure whether something counts as overcomplicated, that uncertainty is itself a signal to keep the simplest version and flag the question rather than build the more elaborate one on a guess
- Does each new dependency, concept, or layer actually earn its cost?
- If conditional branches keep multiplying, can the case be made **not happen** in the first place instead of handling it?
- A file that keeps growing isn't a neutral fact, it's a signal. Split it by responsibility

This skill's checks are explicit instructions, not general vibes — "half the code," "cut anything unrequested," and "split by responsibility" mean literally check for those, not just keep them in mind. When a request is underspecified about scope, don't generously read in extra flexibility or extra structure it didn't ask for — build exactly what was asked and no more.

## Simple ≠ disposable

Even a one-off analysis or script, if it produced a real result, **gets saved as a file.** Simple and unabstracted is fine — living only in shell history or `/tmp` means the next person has to rebuild it from scratch.
