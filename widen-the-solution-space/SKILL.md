---
name: widen-the-solution-space
description: Deliberately widen the set of candidate approaches before committing to one. Use before irreversible decisions (architecture, DB schema, data format, public API), when the first solution feels complicated or awkward, when the user is deciding rather than instructing ("what's the best way to do this?"), or when a previous attempt at the same problem failed. Skip for routine work with one obvious answer.
---

# Diverge Then Converge

The most common failure: **the first plausible idea that comes to mind immediately becomes the answer.** Because it isn't bad, there's no felt need to look for anything better. The more fluently you can generate code, the deeper this trap.

## Diverge: 12 Stimulus Axes

Run through these quickly, in your head. One line each is enough — don't force every one to be filled in.

1. **The obvious solution** — whatever comes to mind first. Keep it as a baseline.
2. **Industry standard** — how do people who already solved this problem usually do it?
3. **The simplest possible thing** — embarrassingly simple. Surprisingly often the right answer.
4. **Build nothing** — can an existing library, feature, or manual process replace this?
5. **Eliminate the problem** — can something upstream change so this situation never arises in the first place?
6. **The opposite direction** — what if the premise is flipped? (push↔pull, sync↔async, store↔recompute, eager↔lazy)
7. **Solve it at a different layer** — in the DB instead of the app, in infra instead of code, at build time instead of runtime
8. **A scoped-down version** — a solution covering 80%. Is the remaining 20% actually needed?
9. **Borrow from an adjacent domain** — does a pattern familiar from a different domain fit here?
10. **A different data structure or model** — does representing the data differently make the problem easier?
11. **Buy or borrow** — an external service or tool instead of building it yourself
12. **Work backward from the future** — from a version of this working well a year from now, what comes first?

## Converge

- Keep only the **2-3** candidates actually worth evaluating. Drop the clearly-nonviable ones silently, without justifying each rejection.
- Hand the remaining candidates to `weigh-tradeoffs`.
- **Mention in one line if a rejected candidate was a close call** — the user might actually want that direction, or it becomes a lead if the project pivots later.
- **Principal-level angle:** for an irreversible or externally-visible choice (schema, API, data format), weigh which candidate is easiest for other teams to adopt or extend — the option that wins on your metrics alone but is hardest for others to build on sets bad precedent.
- **Distinguished/Fellow angle:** if one candidate is a multi-year, company-wide bet that could get open-sourced or presented at a conference, that candidate has to survive scrutiny from people outside this org entirely — a different bar than "wins on this quarter's metrics."
- **Executive angle (CTO/VP-Eng):** if the winning candidate becomes the default, weigh how many engineers you can realistically hire or retain who already know it — a technically superior but rare skill set is a hiring bottleneck, not a win.

## Output

**Don't list all 12.** Divergence mostly happens in your head — show the user only the narrowed 2-3 and why they were chosen. The idea list itself has no value to the user.
