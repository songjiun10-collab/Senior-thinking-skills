---
name: honest-artifacts
description: Make outputs honest and re-derivable. Use when committing constants, thresholds, or tuned parameters; when reporting a number or a benchmark result; when a result came from a manual one-off process; or when optimizing against a metric. Also use when tempted to present an estimate as if it were verified.
---

# Honest Artifacts

## Separate what you know from what you estimated

The most dangerous code isn't wrong code — it's code where **you can't tell how much of it is verified.** Put a validated value next to a guessed one with no distinction, and the next person either trusts both or doubts both.

- Does this constant, parameter, or default have a real basis, or is it "this is probably close enough"?
- If there's no basis, is that fact **explicitly recorded** in code or docs? (`# UNVERIFIED: pulled from X, not independently checked`)
- Are you presenting an estimate as if it were certain?
- A number that gets quoted outside this task — in a design doc, a status update, another team's decision — carries your confidence level with it whether you state it or not. Label unverified numbers before they travel, not after someone has already built a decision on top of them.
- **Distinguished/Fellow angle:** A number or methodology solid enough to appear in a conference talk, a blog post, or an open-source release needs to survive scrutiny from people with zero institutional memory of how it was produced — label what's unverified before it becomes the industry's reference point, not after.
- **Executive angle (CTO/VP-Eng):** A number that ends up in a customer SLA, a sales claim, or a board deck carries legal and reputational risk if it can't be reproduced on demand — verify it before it leaves engineering, not after a customer or investor has already been quoted it.
- Record the attempts that didn't pan out too — the next person won't hit the same wall again. **Failure is data, not something to hide.**

## Reproducibility

"It works" and "it can be rebuilt" are different claims. A result from a one-off manual process is a black box the moment that person is gone.

- Is there a procedure to rebuild this result (a number, a dataset, an artifact) from scratch?
- Does that procedure run as **one command**, or does it live only in someone's head?
- Will the number you're committing now reproduce from the same inputs six months from now? (random seeds, external data drift, version differences)

## Metric traps

Optimize a score long enough and the score improves while the actual goal drifts away.

- Did this change make the **thing you're measuring** better, or did it just fit **the way you're measuring it**? (overfitting)
- Is the sample size big enough? If not, a **conservative choice** beats a complex one with a marginally better score
- Did anything get worse while this metric improved? (a hidden tradeoff — speed up, accuracy down)
- **"It got better" is not a result.** Give the number.
