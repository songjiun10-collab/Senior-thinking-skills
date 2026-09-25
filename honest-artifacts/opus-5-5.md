> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Honest Artifacts

## Separate what you know from what you estimated

The most dangerous code isn't wrong code — it's code where **you can't tell how much of it is verified.** Put a validated value next to a guessed one with no distinction, and the next person either trusts both or doubts both.

- Does this constant, parameter, or default have a real basis, or is it "this is probably close enough"?
- If there's no basis, is that fact **explicitly recorded** in code or docs? (`# UNVERIFIED: pulled from X, not independently checked`) Keep the label itself short — a one-line marker at the value, not a written justification for why it's unverified. Labeling the gap is the job here; don't turn it into its own mini-document.
- Are you presenting an estimate as if it were certain?
- A number that gets quoted outside this task — in a design doc, a status update, another team's decision — carries your confidence level with it whether you state it or not. Label unverified numbers before they travel, not after someone has already built a decision on top of them.
- **Distinguished/Fellow angle:** A number or methodology solid enough to appear in a conference talk, a blog post, or an open-source release needs to survive scrutiny from people with zero institutional memory of how it was produced — label what's unverified before it becomes the industry's reference point, not after.
- **Executive angle (CTO/VP-Eng):** A number that ends up in a customer SLA, a sales claim, or a board deck carries legal and reputational risk if it can't be reproduced on demand — verify it before it leaves engineering, not after a customer or investor has already been quoted it.
- Record the attempts that didn't pan out too — the next person won't hit the same wall again. **Failure is data, not something to hide.** Record it as a short note, not a full incident writeup — resist the pull to build out more structure around it than the fact itself needs.

## Reproducibility

"It works" and "it can be rebuilt" are different claims. A result from a one-off manual process is a black box the moment that person is gone.

- Is there a procedure to rebuild this result (a number, a dataset, an artifact) from scratch?
- Does that procedure run as **one command**, or does it live only in someone's head? If you're building the reproduction script, keep it to that one command — the actual minimum to rerun the thing, not a general-purpose framework around it with options nobody needs yet.
- Will the number you're committing now reproduce from the same inputs six months from now? (random seeds, external data drift, version differences)

## Metric traps

Optimize a score long enough and the score improves while the actual goal drifts away.

- Did this change make the **thing you're measuring** better, or did it just fit **the way you're measuring it**? (overfitting)
- Is the sample size big enough? If not, a **conservative choice** beats a complex one with a marginally better score.
- Did anything get worse while this metric improved? (a hidden tradeoff — speed up, accuracy down)
- **"It got better" is not a result.** Give the number.

## Set effort explicitly for verification work

Thinking is always on, but effort is the actual depth control, and it defaults to `medium` (Opus 5 defaulted to `high`). Anthropic reports Opus 5.5 is "much less likely to state an incorrect figure or cite the wrong source" — but that is a base rate, not a check: verifying a number, tracing where a constant came from, or checking a benchmark for overfitting still has to be done step by step. If a higher level has shown a gain on this kind of work, the caller sets it for that request. Don't expect a terse report to fall out of lower effort either; if the verification writeup needs to be short, say so.

## Don't over-verify past this skill's own steps

Opus 5 guidance, which Anthropic says still applies to 5.5, says the model catches and fixes its own mistakes without prompting and that added re-check instructions add cost without improving results. Once you've gone through the questions above for a given number, that's the verification pass — piling a second "let me re-confirm this is really right" loop on top adds latency and tokens without adding honesty. The discipline this skill asks for is labeling and reproducibility, not repeated re-checking of the same value.
