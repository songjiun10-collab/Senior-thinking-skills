> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Bite-Sized Plan

A plan must be concrete enough that **a competent developer who knows nothing about this codebase, has no judgment call to make, and hates writing tests** could follow it as-is. Clear that bar and the plan can stand on its own.

Other coding agents converge on the same idea from a different angle — OpenAI Codex's Plan Mode (`/plan`) breaks a task into a reviewable step sequence with acceptance criteria *before touching any code*, and asks follow-up questions first when something's unclear, rather than guessing and building the plan on top of the guess. Same principle; this skill just goes one level more granular (2-5 minute steps, not just phases).

## 1. Sketch the file layout first

Before breaking work into tasks, write down **what files get created or changed, and what each one is responsible for.** This is where the decomposition gets locked in.

- One responsibility per file. Split along clear boundaries and interfaces.
- **A size you can hold in your head at once** beats a large, miscellaneous file — small, focused files make fewer mistakes.
- Keep things that change together, together. Split by **responsibility**, not by technical layer.
- In an existing codebase, follow its existing patterns. Don't unilaterally re-architect a codebase that favors large files.
- Principal angle: a file layout that other teams will build on top of (a shared library, a public module) sets a pattern others will copy — get the boundary right here, because fixing it later means a migration, not a refactor.
- **Distinguished/Fellow angle:** a layout meant to become a company-wide standard or get open-sourced has to make sense to someone joining in five years with zero memory of why it was drawn this way — write the reasoning down, not just the boundary.
- **Executive angle (CTO/VP-Eng):** does this decomposition imply a team boundary (who owns which module, how many people it takes to run it) that needs to be reflected in org structure and headcount, not just in the repo.

On this model, the file-layout call itself is the part most worth having a stronger model or a human make — see the calibration note below.

## 2. Sizing a task

**One task = the smallest unit that has its own test cycle and is worth a reviewer's judgment.**

- Fold setup, scaffolding, or docs steps **into the task that needs them.** Don't split them out separately.
- Only split A and B into separate tasks if a reviewer could approve one and reject the other.
- Each task ends in an **independently testable** deliverable.

## 3. Steps are one action, 2-5 minutes each

Each step inside a task is a single, explicit action:

```
1. Write a failing test
2. Run it, confirm it fails
3. Write the minimum code to pass
4. Run it, confirm it passes
5. Commit
```

**Write the trigger for each action explicitly**, not just the action itself — "run it" should say which command, "confirm it fails" should say what output confirms that. This is the level of literalness this model handles best: a fully explicit step list, with no gap left to fill by inference.

## 4. What every task needs

- Exact file paths (don't make anyone guess)
- What it verifies, and **how**
- Pointers to relevant docs or existing code
- A completion condition — what state means this task is done

## 5. Scope check

If a plan spans several independent subsystems, **split the plan.** Each plan should stand on its own with a working, testable result. With a 1.05M-token context window, even a long, fully-spelled-out plan can stay loaded across its own execution without external notes — but keep each plan itself narrow: this model is best used on a series of small, well-specified plans rather than one sprawling structural one.

## Warning signs

| Thought | Reality |
|---|---|
| "Plan's good enough, I'll sort it out while coding" | Deciding while coding is drift, not a plan |
| "This task is big but let's keep it as one chunk" | If you can't test it in one shot, it isn't one task |
| "File layout can wait" | Decomposition decisions are expensive to reverse. Sketch them first |
| "Writing out steps is overkill" | Not for the next person (or you, next session) |
| "The step's intent is obvious, I don't need to spell out the exact command/trigger" | This model executes exactly what's written; an implicit step is a gap, not a shortcut |

## Calibration note for this model

This is the fastest and cheapest tier, well-suited to executing a plan whose file layout and task boundaries were already decided — following the fully-specified step list above is exactly its kind of narrow, well-bounded work. It's the weakest fit in this family for making the layout and sizing decisions themselves under real ambiguity (step 1 and step 2 above). For a **Structural** task or anything with real judgment calls in the decomposition, have a stronger model or a human do the file-layout sketch and task sizing, then hand this model the resulting bite-sized steps to execute.
