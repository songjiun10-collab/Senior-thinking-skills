> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

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

**Write the trigger for each action explicitly**, not just the action itself — "run it" should say which command, "confirm it fails" should say what output confirms that. A step left implicit (an assumed test runner, an assumed confirmation method) is a gap whoever executes the plan has to guess at — and in a pipeline, nobody is there to ask. Underspecifying a step here isn't a shortcut, it's where the plan actually breaks.

## 4. What every task needs

- Exact file paths (don't make anyone guess)
- What it verifies, and **how**
- Pointers to relevant docs or existing code
- A completion condition — what state means this task is done

## 5. Scope check

If a plan spans several independent subsystems, **split the plan.** Each plan should stand on its own with a working, testable result. With a 1.05M-token context window, a large multi-task plan can stay loaded across its own execution without needing external notes to track prior tasks — but scope-split by subsystem independence regardless, since that's about review boundaries and blast radius, not what fits in context. Reasoning effort is set per request, before it starts — each task in a plan is its own request, so it's fine (and expected) for one task's request to run at a different effort than the last; that's not something changed mid-task, it's a choice made when that task's request begins. Effort/tool-set changes between tasks no longer reset the prompt cache, so there's no cost reason to hold every task at the same level — but pick the effort level each task actually needs rather than defaulting to the highest one; more effort doesn't reliably improve plan quality on this model past a certain point.

## Warning signs

| Thought | Reality |
|---|---|
| "Plan's good enough, I'll sort it out while coding" | Deciding while coding is drift, not a plan |
| "This task is big but let's keep it as one chunk" | If you can't test it in one shot, it isn't one task |
| "File layout can wait" | Decomposition decisions are expensive to reverse. Sketch them first |
| "Writing out steps is overkill" | Not for the next person (or you, next session) |
| "The step's intent is obvious, I don't need to spell out the exact command/trigger" | Whoever executes it — this model in a pipeline, or a worker with no context — gets only what's written; an implicit step is a gap, not a shortcut |

## Calibration note for this model

This is the cost-efficient mid tier, well-suited to running a bite-sized plan end to end across a multi-step agentic workflow at a fraction of the flagship tier's cost. OpenAI positions it as a lower-cost alternative to Astra, not the top of the family — so for the file-layout and task-boundary decisions themselves, when the codebase or the requirements are genuinely ambiguous, have a stronger model (or a human) sign off on the file layout in step 1 before this model executes the resulting task list; the execution itself, including the literal step-by-step discipline above, is squarely this model's strength.
