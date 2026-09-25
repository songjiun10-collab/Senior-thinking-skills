> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

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

- Re-read the plan **before deciding**, not once at the start — after many tool calls the original goals get crowded out of the window.
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

## Calibration notes

- **This tier fits executing one phase of an already-written plan, not authoring the plan itself.** Given a `task_plan.md` with clear phases and checkboxes, work through the current phase, update the checkbox, log to `progress.md`, and append to `findings.md` exactly as instructed — that's well-specified, bounded work this tier handles well.
- **Breaking a large, ambiguous task into the right phases in the first place is judgment-heavy work better handled by a stronger tier.** If handed a vague goal with no existing plan structure, prefer to have that structure supplied rather than improvising the phase breakdown from scratch.
- Keep updates to the plan files literal and short: check the box, log the run, append the finding — don't add unrequested detail, restructuring, or new phases beyond what's asked.
- Reasoning effort can stay low for this kind of bounded, checklist-driven execution against an existing plan.
