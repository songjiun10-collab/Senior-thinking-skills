---
name: office-hours
description: Run a structured design office-hours session with a teammate before any code is written. Use when someone asks to brainstorm an idea, asks whether something is worth building, wants a design reviewed before implementation, or says "office hours". Produces a design doc, never code.
---

# Office Hours (router)

A design partner session. The goal is to make sure the problem is understood before any solution gets proposed, then leave a design doc the team can review.

**Hard gate: no implementation.** No code, no scaffolding, no file edits outside the design doc. The only output is the doc.

## How to ask

Every STOP asks through AskUserQuestion, one question per call, with 2-4 concrete options and an "Other" free-text choice. Never ask in prose when AskUserQuestion is available. If it's unavailable, ask in prose and wait.

## Phases

Run them in order. Each STOP means wait for the user's answer before continuing.

1. **Context.** First question, before anything else: the GitHub repo link for the design. Ask via AskUserQuestion with an "Other" option for the URL. STOP. Then read the repo's README, CLAUDE.md, recent git log, and existing design docs. Then ask the goal (product, internal tool, learning, experiment) and the cost of a wrong decision (money/time, trust, lock-in, data). STOP.
2. **Problem.** Ask the user to restate the problem in one sentence that names who has it and how they cope today. Give an example in the question text. STOP. If the answer is vague, ask again with a narrower prompt. Don't fill in the gap yourself.
3. **Premises.** List 3-5 premises the idea depends on, each tagged `verified` (from repo or user) or `assumed`. Ask the user to agree or disagree with each. If any is disputed, loop back to Problem. STOP.
4. **Alternatives.** Offer 2-3 approaches: one minimal, one ideal, optionally one unusual. Give each an effort size (S/M/L/XL), main risk, reversal cost, and what it reuses. Ask the user to pick one. STOP until they do.
5. **Failure modes.** For the chosen approach, run `premortem` and list the ways it breaks, what would page someone, and how we'd notice.
6. **Design doc.** Write the doc (below) and save it under `docs/design/YYYY-MM-DD-<slug>.md`. Show the path. Done.

## Decision brief format

```
D<N>: <question>
Recommendation: <option> — why in one line
Options:
- A: summary · effort S/M/L/XL · risk · reversal cost · reuses
- B: ...
Net: <one line on what the user gains by picking the recommendation>
```

Open questions use `Q<N>`: the question, why it matters, and what a strong answer looks like. Mark each as blocking or non-blocking.

## Design doc sections

- Problem and who has it
- Premises (with verified/assumed tags and the user's agree/disagree)
- Chosen approach and rejected alternatives, with reasons and reversal cost
- Failure modes and detection signals
- Open questions (blocking/non-blocking)
- Out of scope

## Rules

- Never fabricate a completeness score or a user answer. If the user didn't say it, it goes in Open questions.
- Don't treat a "yes" to one question as blanket approval for later steps.
- Anecdotes are `assumed` until the user or repo backs them up.
- If the user repeats a disagreement twice without new information, record it as an open decision instead of looping.
- If the user dismisses a question, stop and wait for the next instruction. Don't proceed.
- Probe before claiming a limitation. Say whether a claim came from reading the code, running it, or recalling it.
- Escalate when stuck instead of looping.

## Which file to use

This skill is a router, not tuned per model. Follow the phases above with whichever model is running.
