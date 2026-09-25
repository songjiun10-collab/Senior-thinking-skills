> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Tradeoffs and Decision Weight

## First: How Heavy Is This Decision

Not every decision deserves the same amount of time.

- **Easily reversible decisions** (a function's internal implementation, file location, variable names) → build it, don't agonize, fix later.
- **Hard-to-reverse decisions** (DB schema, public API, data format, core dependency, an interface already shipped) → spend more time, take alternatives seriously. Thinking is always on for this model and effort defaults to `medium` (Opus 5 defaulted to `high`; in Anthropic's testing 5.5 at `medium` matched or beat Opus 5 at `high`). Medium is fine for the reversible tier; for a schema or public API decision, the scrutiny comes from taking alternatives seriously, and a higher setting — the caller's per-request choice — is worth it where it has shown a gain.

Confirmation follows the same tier: reversible → just do it; irreversible → confirm first. **Gate everything at the same weight, and the gate itself gets ignored.**

## How to Compare

- Lay out the pros and cons of 2-3 real alternatives **in one line each**: speed vs. complexity, flexibility vs. learning curve, easier now vs. easier later, performance vs. readability. Keep the comparison itself terse — response length doesn't shrink much just from lowering effort, so brevity in the write-up has to be asked for explicitly rather than assumed to follow from a quick pass
- Don't pick something reflexively because it's familiar. Familiarity is a legitimate advantage, but it has to be a **stated** one.
- Look at the cost of each alternative being wrong. If the cost is asymmetric (one is easy to reverse, the other isn't), that's usually the deciding factor.
- **Principal-level angle:** for a decision other teams will build against (a shared schema, a public API, a dependency others will also adopt), weigh org-level cost too — migration cost across consumers, and whether it's the direction you want other teams defaulting to for the next few quarters, not just whether it's right for this one codebase.
- **Distinguished/Fellow-level angle:** for a multi-year, company-wide bet (a protocol or format other companies might also converge on), weigh whether it still holds up to someone joining in five years with none of today's context, and whether explaining it depends on people who might not be around to ask.
- **Executive angle (CTO/VP-Eng):** put total cost of ownership on the table, not just engineering effort — license fees, infra spend, and the opportunity cost of the team that would build and maintain it are what a CFO or board asks about before the technical merits.

## Record the Reason

- Leave **one or two sentences** on why this was chosen — in a code comment, commit message, or design note. Keep it to that length on purpose; a longer default output doesn't make the record more useful, and terse is the actual goal here
- It should answer "why did we do it this way?" six months from now. If it can't, the next person just rips it out.
- **Record the rejected alternatives too.** Without knowing why they weren't used, the next person walks down the same path again.

## A note on effort for this model

Thinking can't be turned off here, and effort controls its depth; the default is `medium`. For anything in the irreversible tier — schema, public API, core dependency — don't trust any setting to produce a deep comparison by itself: write the alternatives and their costs down explicitly, and if a higher level has shown a gain on decisions like this, say so, so the caller can set it for that request. And because output length doesn't reliably drop at lower effort (carried over from Opus 5 guidance), ask explicitly for the one-line-per-alternative format if the comparison is running long; it won't compress itself.
