> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Complexity budget

Treat complexity like a budget. Every bit you spend now, you pay back with interest later.

**Read this one carefully — you over-engineer by default.** Absent an explicit constraint, the documented tendency is extra files, unneeded abstractions, and unrequested flexibility. This skill is the direct counter to that tendency, and applying it "as written" isn't enough here: apply it assertively. Treat every abstraction, extra file, and config knob you're about to add as guilty until proven necessary by the request in front of you, not by a plausible future one. Two mechanics make this harder for you specifically, so name them up front: thinking is always on and effort defaults to `medium` — a higher effort setting will happily spend that extra depth generating robustness nobody asked for, so set effort deliberately and pair it with an explicit brevity/simplicity instruction; and your response length doesn't shrink much on its own just because effort is lower, so "keep it small" has to be said outright, not assumed from a lower effort setting.

## YAGNI — don't build what isn't needed now

Abstractions, config options, extension points added "in case it's needed later" mostly go unused — and in the meantime make the code harder to read **today**. This is the exact trap the over-engineering tendency walks into: a plausible-sounding "might need it later" is not evidence of need.

- Is this feature, parameter, or layer needed **now**? If the honest answer is "it'd be nice to have," that's a no
- Are you designing on top of a guess like "we might swap the DB someday"? Notice when you're about to build for a hypothetical, and stop
- Cut anything unrequested: abstractions built for a single call site, error handling for cases that can't happen, a factory or plugin system for one implementation
- Before adding a new file, ask whether the existing structure can hold this instead — an extra file is often the first sign of unrequested scope creep, not a sign of good organization
- Extensibility isn't something you build in now — it's a structure that stays **easy to extend later**
- Principal angle: an abstraction or config knob added here becomes the template other teams copy once it ships — a speculative extension point left in shared/library code costs more than the same thing in a leaf module, because someone else will build on the wrong joint
- Distinguished/Fellow angle: an abstraction placed in a company-wide foundation risks becoming the thing that shows up in a conference talk or gets open-sourced — budget its complexity against years and every team in the org, not one quarter's roadmap
- Executive angle (CTO/VP-Eng): weigh the complexity against total cost of ownership — the infra spend, licensing, and specialized headcount it takes to run and hire for — not just the engineering hours to build it

## Complexity check

- Is there a way to solve this with **half the code**? If 200 lines can become 50, rewrite it. If your first draft added a helper module, a config object, and a strategy interface for what could be a 10-line function, that's the tendency showing up — cut back to the smallest version that satisfies the actual request
- "Would a senior engineer call this overcomplicated?" — if yes, simplify. Ask this specifically about anything you added that wasn't explicitly requested
- Does each new dependency, concept, or layer actually earn its cost? "Earns its cost" means the current request needs it, not that it's good practice in general
- If conditional branches keep multiplying, can the case be made **not happen** in the first place instead of handling it?
- A file that keeps growing isn't a neutral fact, it's a signal. Split it by responsibility — but don't pre-split a file that isn't growing yet just because splitting is generally good hygiene

## Simple ≠ disposable

Even a one-off analysis or script, if it produced a real result, **gets saved as a file.** Simple and unabstracted is fine — living only in shell history or `/tmp` means the next person has to rebuild it from scratch. Saving it as a file doesn't mean wrapping it in structure it doesn't need; a flat script that does the job is the right shape more often than a small framework around it.
