> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

# Bite-Sized Plan

A plan must be concrete enough that **a competent developer who knows nothing about this codebase, has no judgment call to make, and hates writing tests** could follow it as-is. Clear that bar and the plan can stand on its own.

Other coding agents converge on the same idea from a different angle — OpenAI Codex's Plan Mode (`/plan`) breaks a task into a reviewable step sequence with acceptance criteria *before touching any code*, and asks follow-up questions first when something's unclear, rather than guessing and building the plan on top of the guess. Same principle; this skill just goes one level more granular (2-5 minute steps, not just phases).

## 1. Sketch the file layout first

Before breaking work into tasks, write down **what files get created or changed, and what each one is responsible for.** This is where the decomposition gets locked in.

- One responsibility per file. Split along clear boundaries and interfaces.
- **A size you can hold in your head at once** beats a large, miscellaneous file — small, focused files make fewer mistakes.
- Keep things that change together, together. Split by **responsibility**, not by technical layer.
- In an existing codebase, follow its existing patterns. Don't unilaterally re-architect a codebase that favors large files.
- **Watch the over-engineering instinct here specifically.** Left unconstrained, this model tends toward extra files, speculative abstractions, and unrequested flexibility — and "one responsibility per file" can read as license to do that. It's a floor for clarity, not a target to maximize. If the existing codebase uses fewer, larger files, match that; don't split further just because splitting is available.
- Principal angle: a file layout that other teams will build on top of (a shared library, a public module) sets a pattern others will copy — get the boundary right here, because fixing it later means a migration, not a refactor.
- **Distinguished/Fellow angle:** a layout meant to become a company-wide standard or get open-sourced has to make sense to someone joining in five years with zero memory of why it was drawn this way — write the reasoning down, not just the boundary.
- **Executive angle (CTO/VP-Eng):** does this decomposition imply a team boundary (who owns which module, how many people it takes to run it) that needs to be reflected in org structure and headcount, not just in the repo.

## 2. Sizing a task

**One task = the smallest unit that has its own test cycle and is worth a reviewer's judgment.**

- Fold setup, scaffolding, or docs steps **into the task that needs them.** Don't split them out separately.
- Only split A and B into separate tasks if a reviewer could approve one and reject the other.
- Each task ends in an **independently testable** deliverable.

## 3. Steps are one action, 2-5 minutes each

Each step inside a task is a single action:

```
1. Write a failing test
2. Run it, confirm it fails
3. Write the minimum code to pass
4. Run it, confirm it passes
5. Commit
```

## 4. What every task needs

- Exact file paths (don't make anyone guess)
- What it verifies, and **how**
- Pointers to relevant docs or existing code
- A completion condition — what state means this task is done

## 5. Scope check

If a plan spans several independent subsystems, **split the plan.** Each plan should stand on its own with a working, testable result.

## Warning signs

| Thought | Reality |
|---|---|
| "Plan's good enough, I'll sort it out while coding" | Deciding while coding is drift, not a plan |
| "This task is big but let's keep it as one chunk" | If you can't test it in one shot, it isn't one task |
| "File layout can wait" | Decomposition decisions are expensive to reverse. Sketch them first |
| "Writing out steps is overkill" | Not for the next person (or you, next session) |
| "This plan needs a config system / plugin layer / extra abstraction to be safe" | That's the over-engineering instinct talking, not the task. If nothing in the request asked for it, it doesn't belong in the plan |

## Calibration for this model

Thinking is always on for this model, and its default effort is a notch below what deep planning benefits from — **set effort explicitly higher before sketching the file layout** (step 1) and sizing tasks (step 2), where the real decomposition mistakes happen; low-effort output on this tier doesn't get meaningfully shorter, so brevity in the final plan doc still has to be asked for directly if that's the goal.

Producing this plan is itself a good candidate for doing directly rather than delegating to a subagent — this model reaches for a subagent more eagerly than earlier ones, including for planning work that's faster done in the main thread since it needs the same context the rest of the session already has. Save delegation for executing the plan's independent tasks once they're written, not for writing the plan itself.

If a review or self-check pass over the finished plan feels tempting, know this model already verifies its own output well — an extra "double check this plan is complete" instruction on top of the Scope check and Warning signs above is likely to cost tokens without finding anything those two didn't already catch.
