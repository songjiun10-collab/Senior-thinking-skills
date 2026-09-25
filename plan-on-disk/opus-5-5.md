> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

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

Keep these three files and nothing more. The habit to actively resist here is scaffolding the plan itself — extra files per phase, a metadata index on top of `task_plan.md`, a status-tracking layer beyond the checkboxes. Three files is the whole system.

## Recitation, not memory

- Re-read the plan **before deciding**, not once at the start — after 50+ tool calls the original goals get crowded out of the window
- Check a box **right after the milestone**, not batched for later — a finished-but-unchecked box is a lie the next session inherits
- Log failures in the plan file too — an error that isn't recorded repeats itself (`honest-artifacts`)
- Read `task_plan.md` and `findings.md` directly yourself when re-orienting — a quick file read is faster than dispatching a subagent to summarize progress so far, even though handing off a "catch me up" pass can feel like the natural move on a task that's gotten long.
- **Principal angle:** a plan another team or a future session resumes sets a pattern — write it so someone with zero context lands at the current phase, not at zero. Losing it to compaction costs their velocity, not just yours.
- **Distinguished/Fellow angle:** a plan that accumulates across months of sessions is a company asset only while it stays honest — review it the way `persistent-memory` says, resolve conflicting entries, delete what fossilized. One that only makes sense with unwritten context is a bus-factor-of-one liability.
- **Executive angle (CTO/VP-Eng):** agents re-orienting for half a session after every crash are an engineering-cost line, and a plan that lets an agent declare "done" early is a delivery-risk decision — worth standardizing the pattern across teams rather than leaving it to each agent's habit.

## Completion is a gate, not a feeling

- No "done" while a checkbox stands unchecked or a phase is `in_progress` — `verify-before-claiming` applies to the plan itself, not just the code
- **Documented for Opus 5.5:** on long multi-part tasks, some progress updates end the turn with text instead of a tool call while work remains, and an unattended loop stops right there. Anthropic's fix is exactly this file: keep the parts in a checklist the model updates. Before any text-only end of turn, re-read `task_plan.md` — open, unblocked boxes mean do the next one, not report
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
| "This plan needs its own subfolder structure to stay organized" | Three flat files is the system; extra structure is scope the task didn't ask for |

## Calibration notes

- **Set effort explicitly for planning a genuinely large multi-phase task.** Effort defaults to `medium` (in Anthropic's testing, 5.5 at `medium` matched or beat Opus 5 at `high`). A plan spanning many phases and unknowns is where a bad breakdown gets baked in — if a higher level has shown a gain there, the caller sets it for that request.
- **Keep `task_plan.md` itself lean.** Don't over-engineer the plan file — no premature phase subdivision, no speculative future-phase placeholders, no configurability nobody asked for. Write the phases the task actually needs.
- **Trust your own re-orientation reads over delegating them.** Checking `task_plan.md` and `findings.md` after a long stretch is a direct file read, not a research task worth a subagent dispatch.
