> Tuned for Claude Sonnet 5.5. Source: Anthropic prompting guide (prompting-claude-sonnet-5-5). See SKILL.md for the model index.

# Review With Fresh Eyes

> **Difference from `adversarial-review`**: this is a post-hoc pass over **finished work**. `adversarial-review` interrogates an **in-flight decision** with a disproving bias, while reversing it is still cheap. If an irreversible decision is on the line, reach for `adversarial-review` before the work is done, not after.

Review code with the same context you wrote it in, and you carry the same blind spots into the review. You know why you wrote it that way, so the odd part doesn't look odd. Most of a review's value comes from **looking at it without that knowledge.**

## How to shed the context

- **Look only at the result.** Set aside why it turned out this way; read only the diff and the final code.
- Ask the questions a first-time reader would ask: when is this variable null? What does this function return? Why is this condition here?
- **Go back to the original requirement and check against it.** Is what you built what was asked for? Did it drift along the way? Reread the original requirement's exact wording here rather than your paraphrase of it — an underspecified original ask tends to get built to its literal words, and a drift is easiest to miss if the review also works from a loosened paraphrase instead of the actual text.

## Two separate axes

Mix two kinds of judgment into one pass and you miss both. Keep them separate.

1. **Spec compliance** — did you actually do what was asked? What requirements are missing? What did you do that wasn't asked for?
2. **Code quality** — naming, structure, duplication, error handling, boundary conditions

On a change to a shared interface, add a third lens: **who else calls this, and does the review still hold from their vantage point** — not just the caller you happened to test against.

- **Distinguished/Fellow angle:** For a change likely to set precedent across the whole org or outlive its author's tenure, review it as the person who inherits it in five years would — with none of the context, only what's written down.
- **Executive angle (CTO/VP-Eng):** For a change to a system a customer, regulator, or partner depends on, review it for what happens when it fails in production — who gets paged, what SLA or contract is breached, what it costs to remediate — not just whether the code itself is well-structured.

## Verify it yourself

- Don't trust a report or your memory — **actually run the tests**.
- Actually read the diff. What you think you fixed and what actually changed can differ.
- Can't confirm something from the diff? **Mark it unconfirmed.** Don't wave it through — and don't round "probably fine" up to "confirmed" in the write-up; state exactly what was and wasn't checked.

## No self-censoring

Don't pre-filter findings before the review with "this is probably fine." Even something you think is a false positive goes on the list — judge it later. Pre-grading buries the real problems along with the noise.

## Watch your own budget on a large diff

You track your remaining context budget as you go. On a review that touches many files, use that awareness to decide early whether to review the whole diff in one pass or split it — better to notice you're running short with half the diff still unread and adjust than to have the back half of the review get thinner without deciding to let it.

## Calibration (Anthropic official prompting guide, Sonnet 5.5)

- **Effort**: default is `high` on the Claude API. Levels are recalibrated from Sonnet 5, so re-run an effort sweep rather than carrying over the old setting. Start at `medium` for agentic coding and well-specified multistep tool use; `medium` or `low` for chat.
- **Low effort skips verification and stops early**: at `low`, the model may skip checks and, at `low`/`medium` on long agentic tasks, check in before finishing. Add an explicit "keep working until done, stop only before a risky step" line rather than assuming it will carry work through.
- **Thinking off**: send `thinking: {type: "between_tools"}` at `high` effort or below. `{type: "disabled"}` is a 400. Per-message effort changes need adaptive thinking.
- **Structured JSON on multistep reasoning**: prefer structured outputs; otherwise ask the model to think first and parse the last JSON value, treating `stop_reason: "max_tokens"` as failure.
- **Progress visibility**: set `display: "updates"` to surface between-tool-call notes.
- **Search**: tell it to check specifics that may have changed (what is allowed, required, or charged), even when confident.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn. Keep harness reminders in a separate system message, so the model doesn't mistake real user input for injection.
- **Verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Safeguard refusals**: categories `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`. Remove prompt instructions that ask it to reproduce its reasoning in the reply.
