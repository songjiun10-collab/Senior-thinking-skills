> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Tradeoffs and Decision Weight

## First: How Heavy Is This Decision

Not every decision deserves the same amount of time.

- **Easily reversible decisions** (a function's internal implementation, file location, variable names) → build it, don't agonize, fix later.
- **Hard-to-reverse decisions** (DB schema, public API, data format, core dependency, an interface already shipped) → spend more time, take alternatives seriously. State the exploration scope up front for this tier — which alternatives to actually investigate and where to stop — since this model is more tentative than predecessors about deciding a comparison is finished on its own, and an open-ended "look into some options" tends to either stall or under-explore without a stated boundary.

Confirmation follows the same tier: reversible → just do it; irreversible → confirm first. **Gate everything at the same weight, and the gate itself gets ignored.**

## How to Compare

- Lay out the pros and cons of 2-3 real alternatives **in one line each**: speed vs. complexity, flexibility vs. learning curve, easier now vs. easier later, performance vs. readability
- Don't pick something reflexively because it's familiar. Familiarity is a legitimate advantage, but it has to be a **stated** one.
- Look at the cost of each alternative being wrong. If the cost is asymmetric (one is easy to reverse, the other isn't), that's usually the deciding factor.
- **Principal-level angle:** for a decision other teams will build against (a shared schema, a public API, a dependency others will also adopt), weigh org-level cost too — migration cost across consumers, and whether it's the direction you want other teams defaulting to for the next few quarters, not just whether it's right for this one codebase.
- **Distinguished/Fellow-level angle:** for a multi-year, company-wide bet (a protocol or format other companies might also converge on), weigh whether it still holds up to someone joining in five years with none of today's context, and whether explaining it depends on people who might not be around to ask.
- **Executive angle (CTO/VP-Eng):** put total cost of ownership on the table, not just engineering effort — license fees, infra spend, and the opportunity cost of the team that would build and maintain it are what a CFO or board asks about before the technical merits.

## Record the Reason

- Leave **one or two sentences** on why this was chosen — in a code comment, commit message, or design note. Write it as plain, direct prose rather than a bulleted list of reasons — this model reads a short, well-formed paragraph as clearly as a list, and a tradeoffs record is exactly the kind of "truly sequential" content a paragraph fits better than a fragmented bullet stack.
- It should answer "why did we do it this way?" six months from now. If it can't, the next person just rips it out.
- **Record the rejected alternatives too.** Without knowing why they weren't used, the next person walks down the same path again.

## A note on how this model runs this skill

Two of this model's documented tendencies matter here more than usual. It's more tentative than predecessors about calling an exploration finished, so a hard-to-reverse decision needs an explicit scope and stopping point stated up front — "compare these three, spend no more than X, and land on one" — rather than leaving "weigh the alternatives" open-ended. And it delegates to subagents less than expected on its own, so if the comparison should be split up (one subagent prototyping option A, another checking option B against existing consumers), say so explicitly rather than assuming it will parallelize the work by default. Neither tendency changes the substance of the comparison itself: reversible decisions still get built without agonizing, irreversible ones still get a real side-by-side with a recorded reason.
