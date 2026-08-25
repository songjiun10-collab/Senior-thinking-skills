---
name: bite-sized-plan
description: Turn an approved design into a plan of independently testable, bite-sized tasks. Use after a design is agreed and before touching code on any multi-step work. Also use when a task has sprawled beyond what fits in one sitting, when handing implementation to someone (or something) without your context, or when work keeps drifting from the original intent.
---

# Bite-Sized Plan

A plan must be concrete enough that **a competent developer who knows nothing about this codebase, has no judgment call to make, and hates writing tests** could follow it as-is. Clear that bar and the plan can stand on its own.

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
