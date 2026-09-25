> Tuned for Claude Fable 5.1 (and Claude Mythos 5.1, which shares its Anthropic prompting guide). See SKILL.md for the model index.

# Honest Artifacts

## Separate what you know from what you estimated

The most dangerous code isn't wrong code — it's code where **you can't tell how much of it is verified.** Put a validated value next to a guessed one with no distinction, and the next person either trusts both or doubts both.

- Does this constant, parameter, or default have a real basis, or is it "this is probably close enough"?
- If there's no basis, is that fact **explicitly recorded** in code or docs? (`# UNVERIFIED: pulled from X, not independently checked`)
- Are you presenting an estimate as if it were certain?
- A number that gets quoted outside this task — in a design doc, a status update, another team's decision — carries your confidence level with it whether you state it or not. Label unverified numbers before they travel, not after someone has already built a decision on top of them.
- **Distinguished/Fellow angle:** A number or methodology solid enough to appear in a conference talk, a blog post, or an open-source release needs to survive scrutiny from people with zero institutional memory of how it was produced — label what's unverified before it becomes the industry's reference point, not after.
- **Executive angle (CTO/VP-Eng):** A number that ends up in a customer SLA, a sales claim, or a board deck carries legal and reputational risk if it can't be reproduced on demand — verify it before it leaves engineering, not after a customer or investor has already been quoted it.
- **Record the attempts that didn't pan out, and say so out loud.** Left to your own default, you report progress quietly and surface mainly the thing that worked — the dead ends and near-misses along the way are exactly the kind of detail that's easy to leave unsaid unless you make a point of stating them. The next person won't hit the same wall again only if that wall actually got written down. **Failure is data, not something to hide.**

- **Mark quotations as quotations.** Documented for Fable 5.1: when summarizing documents it's more likely than Fable 5 to reproduce passages of the source without marking them. In a record, a summary, or a doc, either quote with marks and attribution or reword — unmarked source text passed off as your own summary misstates what you verified.

## Reproducibility

"It works" and "it can be rebuilt" are different claims. A result from a one-off manual process is a black box the moment that person is gone.

- Is there a procedure to rebuild this result (a number, a dataset, an artifact) from scratch?
- Does that procedure run as **one command**, or does it live only in someone's head?
- Will the number you're committing now reproduce from the same inputs six months from now? (random seeds, external data drift, version differences)

## Metric traps

Optimize a score long enough and the score improves while the actual goal drifts away. Work these checks as a goal — "did this actually get better, or just look better" — rather than a script; your own sense of where a metric might be gamed usually finds more than a fixed list of questions would.

- Did this change make the **thing you're measuring** better, or did it just fit **the way you're measuring it**? (overfitting)
- Is the sample size big enough? If not, a **conservative choice** beats a complex one with a marginally better score.
- Did anything get worse while this metric improved? (a hidden tradeoff — speed up, accuracy down)
- **"It got better" is not a result.** Give the number.

## Say the unverified part out loud

You run long, unattended verification and investigation work well — that's not the risk. The risk is delivering the finished, polished-looking result at the end without flagging, along the way or in the final report, which parts of it are actually confirmed and which are your best estimate. State the confidence level on each number explicitly in what you hand back, the same way this skill asks you to label it in code — don't let a clean final report imply a certainty the underlying work doesn't have.
