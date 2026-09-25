> Tuned for Claude Sonnet 5. See SKILL.md for the model index.

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

- Re-read the plan **before deciding**, not once at the start — after 50+ tool calls the original goals get crowded out of the window. With a 1M-token window this pattern still applies: even where the raw plan text would technically still fit, re-reading it is what keeps it *weighted* in your actual decision, not just present somewhere in a long context.
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
| "I have a huge context window, I don't need to re-read the plan file" | Fitting in context isn't the same as staying weighted in the decision — re-read it anyway |

## Calibration notes

- When a task is multi-step and expected to outlast one sitting, set up the three files explicitly rather than assuming the instruction to do so is implied — state the plan-on-disk setup as its own explicit step at the start of the work, since underspecified framing here tends to get followed literally rather than filled in generously.
