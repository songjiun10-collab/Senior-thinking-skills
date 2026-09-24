> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

# Bite-Sized Plan

A plan must be concrete enough that **a competent developer who knows nothing about this codebase, has no judgment call to make, and hates writing tests** could follow it as-is. Clear that bar and the plan can stand on its own.

Other coding agents converge on the same idea from a different angle — OpenAI Codex's Plan Mode (`/plan`) breaks a task into a reviewable step sequence with acceptance criteria *before touching any code*, and asks follow-up questions first when something's unclear, rather than guessing and building the plan on top of the guess. Same principle; this skill just goes one level more granular for a human executor (2-5 minute steps, not just phases) — see the calibration note below on when that granularity is and isn't the right call for this model specifically.

## 1. Sketch the file layout first

Before breaking work into tasks, write down **what files get created or changed, and what each one is responsible for.** This is where the decomposition gets locked in.

- One responsibility per file. Split along clear boundaries and interfaces.
- **A size you can hold in your head at once** beats a large, miscellaneous file — small, focused files make fewer mistakes.
- Keep things that change together, together. Split by **responsibility**, not by technical layer.
- In an existing codebase, follow its existing patterns. Don't unilaterally re-architect a codebase that favors large files.
- Principal angle: a file layout that other teams will build on top of (a shared library, a public module) sets a pattern others will copy — get the boundary right here, because fixing it later means a migration, not a refactor.
- **Distinguished/Fellow angle:** a layout meant to become a company-wide standard or get open-sourced has to make sense to someone joining in five years with zero memory of why it was drawn this way — write the reasoning down, not just the boundary.
- **Executive angle (CTO/VP-Eng):** does this decomposition imply a team boundary (who owns which module, how many people it takes to run it) that needs to be reflected in org structure and headcount, not just in the repo.

## 2. Sizing a task

**One task = the smallest unit that has its own test cycle and is worth a reviewer's judgment.**

- Fold setup, scaffolding, or docs steps **into the task that needs them.** Don't split them out separately.
- Only split A and B into separate tasks if a reviewer could approve one and reject the other.
- Each task ends in an **independently testable** deliverable.

## 3. Steps, sized to who's executing them

The reference shape for one task's steps:

```
1. Write a failing test
2. Run it, confirm it fails
3. Write the minimum code to pass
4. Run it, confirm it passes
5. Commit
```

**This is written for a human executor or a lower-autonomy agent.** For this model specifically, a plan scripted down to rigid single-action steps tends to underperform a plan that states the task's goal and constraints and lets it reason through the sequence — its own step-by-step reasoning routinely exceeds what a human would have pre-scripted. Keep the file layout (section 1) and task boundaries (section 2) — those decomposition calls are still worth locking in explicitly — but when this model is the one *executing* the plan, write each task as "goal: X, constraints: Y, verify by: Z" rather than a forced 2-5 minute step list, and let it work out the write-test/run/commit sequence itself. Reserve the rigid numbered-step form for handoff to a different, less autonomous executor.

## 4. What every task needs

- Exact file paths (don't make anyone guess)
- What it verifies, and **how**
- Pointers to relevant docs or existing code
- A completion condition — what state means this task is done

These stay explicit regardless of executor — they're the task's contract, not its step sequence.

## 5. Scope check

If a plan spans several independent subsystems, **split the plan.** Each plan should stand on its own with a working, testable result. This model handles a long multi-task plan executed in one continuous run well — splitting is still about subsystem independence, not about turn length.

## Warning signs

| Thought | Reality |
|---|---|
| "Plan's good enough, I'll sort it out while coding" | Deciding while coding is drift, not a plan |
| "This task is big but let's keep it as one chunk" | If you can't test it in one shot, it isn't one task |
| "File layout can wait" | Decomposition decisions are expensive to reverse. Sketch them first |
| "Writing out steps is overkill" | Not for the next person (or you, next session) — though for this model, "steps" often means the task's goal and contract, not a forced action list; see section 3 |

## Calibration for this model

This model writes noticeably fewer user-facing updates between steps during a long execution run — quiet by default. If visibility into which task or step is in progress matters (a long-running multi-task plan, unattended execution), ask explicitly for a status line after each task completes; it won't volunteer that narration unprompted. It also uses less markdown formatting by default — a plan doc handed to it doesn't need heavy structure to be legible to it, though keep the structure a human reviewer of the plan still needs.
