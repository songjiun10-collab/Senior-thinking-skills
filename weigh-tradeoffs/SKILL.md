---
name: weigh-tradeoffs
description: Compare real alternatives explicitly and record why one was chosen. Use when picking between libraries, data structures, architectures, or storage options; when a decision is hard to reverse (schema, public API, data format, dependency); or when the user asks "which is better, A or B". Also use to decide how much deliberation a decision even deserves.
---

# Tradeoffs and Decision Weight

## First: How Heavy Is This Decision

Not every decision deserves the same amount of time.

- **Easily reversible decisions** (a function's internal implementation, file location, variable names) → build it, don't agonize, fix later.
- **Hard-to-reverse decisions** (DB schema, public API, data format, core dependency, an interface already shipped) → spend more time, take alternatives seriously.

Confirmation follows the same tier: reversible → just do it; irreversible → confirm first. **Gate everything at the same weight, and the gate itself gets ignored.**

## How to Compare

- Lay out the pros and cons of 2-3 real alternatives **in one line each**: speed vs. complexity, flexibility vs. learning curve, easier now vs. easier later, performance vs. readability.
- Don't pick something reflexively because it's familiar. Familiarity is a legitimate advantage, but it has to be a **stated** one.
- Look at the cost of each alternative being wrong. If the cost is asymmetric (one is easy to reverse, the other isn't), that's usually the deciding factor.
- **Principal-level angle:** for a decision other teams will build against (a shared schema, a public API, a dependency others will also adopt), weigh org-level cost too — migration cost across consumers, and whether it's the direction you want other teams defaulting to for the next few quarters, not just whether it's right for this one codebase.
- **Distinguished/Fellow-level angle:** for a multi-year, company-wide bet (a protocol or format other companies might also converge on), weigh whether it still holds up to someone joining in five years with none of today's context, and whether explaining it depends on people who might not be around to ask.
- **Executive angle (CTO/VP-Eng):** put total cost of ownership on the table, not just engineering effort — license fees, infra spend, and the opportunity cost of the team that would build and maintain it are what a CFO or board asks about before the technical merits.

## Record the Reason

- Leave **one or two sentences** on why this was chosen — in a code comment, commit message, or design note.
- It should answer "why did we do it this way?" six months from now. If it can't, the next person just rips it out.
- **Record the rejected alternatives too.** Without knowing why they weren't used, the next person walks down the same path again.
