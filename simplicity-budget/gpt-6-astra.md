> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Complexity budget

Treat complexity like a budget. Every bit you spend now, you pay back with interest later.

Two things about how you work make this skill worth applying deliberately rather than by feel. First, you're documented to be more tentative than prior models about declaring a task complete, and to ask clarifying questions more often — left unconstrained, that shows up as widening scope ("let me also handle this related case," "let me add a config option so this covers the variant too") in the process of trying to be thorough. State the completion criterion up front — what this change needs to do, and where to stop — so "thorough" means finishing the actual request, not finding more to build. Second, more reasoning effort doesn't reliably buy you a better answer on this kind of task; benchmarks show effort peaking below max on several workloads, and mid-conversation effort changes no longer break your prompt cache, so it's cheap to tune per task rather than defaulting high. Higher effort spent generating unrequested robustness is exactly what this skill argues against — set effort to match the actual difficulty of the problem, not the ceiling.

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
- A file that keeps growing isn't a neutral fact, it's a signal. Split it by responsibility

This skill's checks are explicit instructions, not general vibes — "half the code," "cut anything unrequested," and "split by responsibility" mean literally check for those, not just keep them in mind. When a request is underspecified about scope, resist the urge to ask a clarifying question as a way of covering more ground ("should I also handle X?") when the honest answer is that X wasn't asked for — build exactly what was asked and no more, in plain prose over a list where the reasoning isn't genuinely parallel or sequential.

## Simple ≠ disposable

Even a one-off analysis or script, if it produced a real result, **gets saved as a file.** Simple and unabstracted is fine — living only in shell history or `/tmp` means the next person has to rebuild it from scratch.
