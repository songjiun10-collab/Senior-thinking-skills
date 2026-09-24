---
name: plan-on-disk
description: Keep the active plan on disk instead of in the context window — task_plan.md, findings.md, progress.md — so it survives /clear, compaction, crashes, and hour ten of a long run. Use when starting multi-step work expected to outlast one sitting or one context window, resuming after a /clear or compaction, when work drifts from the original intent after many tool calls, or when handing a long-running task to an agent or subagent chain. Skip for short tasks that fit in one sitting and never leave the session.
---

# Plan on Disk

**Context window = RAM (volatile, limited). Filesystem = disk (persistent, unlimited).** Anything important gets written to disk. The to-do list inside the context window dies with it — on `/clear`, on compaction, on a crash. The plan does not have to.

This is the pattern behind Manus's context engineering and OthmanAdi/planning-with-files. `bite-sized-plan` decides what the plan contains; this skill decides where it lives and how it survives the run. Related: `context-economy` decides what goes in context vs. a file in general — this skill is the execution-state case of that rule.

## The three files

For every complex task, three files in the project root:

```
task_plan.md   → phases + checkboxes; the resume point after /clear
findings.md    → research notes and decisions, appended as you go
progress.md    → session log and test results
```

- `task_plan.md` is the resume point — phases with checkboxes, the current phase marked `in_progress`
- `findings.md` is **appended, never rewritten from memory** — a finding only exists once it's on disk
- `progress.md` logs what was run and what came back, so a crashed session resumes at the last known state, not at zero

## Recitation, not memory

- Re-read the plan **before deciding**, not once at the start — after 50+ tool calls the original goals get crowded out of the window
- Check a box **right after the milestone**, not batched for later — a finished-but-unchecked box is a lie the next session inherits
- Log failures in the plan file too — an error that isn't recorded repeats itself (`honest-artifacts`)
- **Principal angle:** a plan another team or a future session resumes sets a pattern — write it so someone with zero context lands at the current phase, not at zero. Losing it to compaction costs their velocity, not just yours.
- **Distinguished/Fellow angle:** a plan that accumulates across months of sessions is a company asset only while it stays honest — review it the way `persistent-memory` says, resolve conflicting entries, delete what fossilized. One that only makes sense with unwritten context is a bus-factor-of-one liability.
- **Executive angle (CTO/VP-Eng):** agents re-orienting for half a session after every crash are an engineering-cost line, and a plan that lets an agent declare "done" early is a delivery-risk decision — worth standardizing the pattern across teams rather than leaving it to each agent's habit.

## Completion is a gate, not a feeling

- No "done" while a checkbox stands unchecked or a phase is `in_progress` — `verify-before-claiming` applies to the plan itself, not just the code
- The plan files are **working memory, not a deliverable**: gitignored by default, overwritten by the next task. Anything worth keeping gets promoted into code, a commit, or a doc
- Corrections and preferences belong in `persistent-memory` (durable per-topic files); execution state belongs here. Don't mix them

## Parallel tasks

Isolated directories, not one shared root plan: `.planning/YYYY-MM-DD-slug/` with the same three files inside. Two sessions writing one root `task_plan.md` overwrite each other's phases.

## Warning signs

| Thought | Reality |
|---|---|
| "The plan is in my context, I'll remember" | Context dies on /clear, compaction, or hour ten |
| "Basically done" (2 of 5 boxes checked) | The boxes are the gate, not a feeling |
| "I'll write the findings down at the end" | A finding not on disk when discovered gets re-derived or lost |
| "One shared plan file is fine for two agents" | They overwrite each other's phases |

## Model notes

- **Haiku 4.5** — With only a 200K window, this pattern matters more here than elsewhere — recite the plan from disk more often, since irrelevant context gets crowded out sooner.
- **Sonnet 5** — Default — apply as written.
- **Opus 5** — No tier-specific adjustment — apply as written.
- **Opus 5.5** — No tier-specific adjustment — apply as written.
- **Fable 5.1** — Write `task_plan.md` as goals and phases, not a prescriptive step list — its own reasoning per phase tends to exceed a human-scripted sequence; it also handles long-horizon runs between check-ins well, so the plan file matters more for resumability than for step-by-step direction.
