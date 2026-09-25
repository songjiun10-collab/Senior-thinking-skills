> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Honest Artifacts

You're the fastest, cheapest tier here, well suited to the mechanical parts of this skill — labeling a value, running a fixed reproduction command, extracting a number and stating its precision — and less suited to the judgment parts, like deciding whether a metric improvement is real or an artifact of overfitting on a small sample. Do the former directly; where a question below calls for that kind of open-ended judgment on an ambiguous case, say what you found and flag it rather than rendering a confident verdict.

## Separate what you know from what you estimated

The most dangerous code isn't wrong code — it's code where **you can't tell how much of it is verified.** Put a validated value next to a guessed one with no distinction, and the next person either trusts both or doubts both.

- Does this constant, parameter, or default have a real basis, or is it "this is probably close enough"?
- If there's no basis, is that fact **explicitly recorded** in code or docs? (`# UNVERIFIED: pulled from X, not independently checked`)
- Are you presenting an estimate as if it were certain? State the confidence level explicitly rather than leaving it to be inferred — an unqualified number in a report gets read as verified by default, not charitably discounted.
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

Optimize a score long enough and the score improves while the actual goal drifts away. This is the part of the skill most likely to need escalation at this tier — judging whether an improvement is real or a fit to the measurement, or whether a sample size is adequate, is a judgment call, not an extraction task.

- Did this change make the **thing you're measuring** better, or did it just fit **the way you're measuring it**? (overfitting) — if you can't tell from what's in front of you, say so rather than picking a side.
- Is the sample size big enough? If not, a **conservative choice** beats a complex one with a marginally better score.
- Did anything get worse while this metric improved? (a hidden tradeoff — speed up, accuracy down)
- **"It got better" is not a result.** Give the number.

## If the verification task itself is underspecified

"Check this number" or "make sure this is right" is a literal instruction with an implicit scope. At this tier, default to the narrowest reasonable reading (sanity-check the order of magnitude, or re-run the stated command) and say explicitly which check you ran and which ones you didn't — don't stretch into re-deriving a result from source data or judging overfitting unless that was explicitly asked for.
