---
name: simplicity-budget
description: Keep the solution as small as the problem — YAGNI and a complexity budget. Use when a design starts growing abstractions, config options, or extension points; when adding a dependency; when a file or function keeps getting longer; or when the user asks whether something is over-engineered. Also use before building anything justified by "might need it later".
---

# Complexity budget

Treat complexity like a budget. Every bit you spend now, you pay back with interest later.

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
- "Would a senior engineer call this overcomplicated?" — if yes, simplify
- Does each new dependency, concept, or layer actually earn its cost?
- If conditional branches keep multiplying, can the case be made **not happen** in the first place instead of handling it?
- A file that keeps growing isn't a neutral fact, it's a signal. Split it by responsibility.

## Simple ≠ disposable

Even a one-off analysis or script, if it produced a real result, **gets saved as a file.** Simple and unabstracted is fine — living only in shell history or `/tmp` means the next person has to rebuild it from scratch.
