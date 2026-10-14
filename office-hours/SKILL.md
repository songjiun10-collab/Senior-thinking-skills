---
name: office-hours
description: Run a structured design office-hours session with a teammate before any code is written. Use when someone asks to brainstorm an idea, asks whether something is worth building, wants a design reviewed before implementation, or says "office hours". Produces a design doc, never code.
---

# Office Hours (router)

A design partner session. The goal is to make sure the problem is understood before any solution gets proposed, then leave a design doc the team can review.

**Hard gate: no implementation.** No code, no scaffolding, no file edits outside the design doc. The only output is the doc.

## Phases

Run them in order. Each STOP means wait for the user's answer before continuing.

1. **Context.** Read the repo's README, CLAUDE.md, recent git log, and any existing design docs. Ask one question: what is the goal (product, internal tool, learning, experiment). STOP.
2. **Problem.** Restate the problem in one sentence and ask whether it's right. Name the user who has it and how they cope today. STOP if either is missing.
3. **Premises.** List 3-5 premises the idea depends on. Ask the user to agree or disagree with each. If any is disputed, loop back to Problem.
4. **Alternatives.** Offer 2-3 approaches: one minimal, one ideal, optionally one unusual. Give each an effort size (S/M/L/XL), main risk, and what it reuses. Ask the user to pick one. STOP until they do.
5. **Failure modes.** For the chosen approach, run `premortem` and list the ways it breaks and how we'd notice.
6. **Design doc.** Write the doc (below) and save it under `docs/design/YYYY-MM-DD-<slug>.md`. Show the path. Done.

## Decision brief format

Use this whenever a choice needs the user:

```
D<N>: <question>
Recommendation: <option> — why in one line
Options:
- A: summary · effort S/M/L/XL · risk · reuses
- B: ...
Net: <one line on what the user gains by picking the recommendation>
```

Open questions use `Q<N>`: the question, why it matters, and what a strong answer looks like.

## Design doc sections

- Problem and who has it
- Premises (with the user's agree/disagree status)
- Chosen approach and rejected alternatives, with reasons (`record-the-why` style)
- Failure modes and detection
- Open questions
- Out of scope

## Rules

- Never fabricate a completeness score or a user answer. If the user didn't say it, it goes in Open questions.
- Don't treat a "yes" to one question as blanket approval for later steps.
- If the user repeats a disagreement twice without new information, record it as an open decision instead of looping.
- Probe before claiming a limitation. Say whether a claim came from reading the code, running it, or recalling it.
- Escalate when stuck instead of looping.

## Which file to use

This skill is a router, not tuned per model. Follow the phases above with whichever model is running.
