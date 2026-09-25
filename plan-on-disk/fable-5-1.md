> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

# Plan on Disk

**Context window = RAM (volatile, limited). Filesystem = disk (persistent, unlimited).** Anything important gets written to disk. The to-do list inside the context window dies with it — on `/clear`, on compaction, on a crash. The plan does not have to.

This is the pattern behind Manus's context engineering and OthmanAdi/planning-with-files. `bite-sized-plan` decides what the plan contains; this skill decides where it lives and how it survives the run. Related: `context-economy` decides what goes in context vs. a file in general — this skill is the execution-state case of that rule.

## The three files

For every complex task, three files in the project root:

```
task_plan.md   → phases + goals; the resume point after /clear
findings.md    → research notes and decisions, appended as you go
progress.md    → session log and test results
```

- `task_plan.md` is the resume point — phases with checkboxes and the goal each phase serves, current phase marked `in_progress`. Because this is specifically the thing a *fresh context* reads after `/clear`, compaction, or a crash, write enough into each phase (concrete files, the check that proves it's done, the order that matters) that a session with none of the current reasoning can pick it up without re-deriving judgment calls — a bare goal statement asks the resuming context to reconstruct exactly what this pattern exists to avoid losing. Where this model's own step-by-step reasoning genuinely exceeds a pre-scripted sequence is *live, in the session that's actively executing the phase* — it's fine to deviate from the written detail there when you have a concrete reason to, but that's a live judgment call layered on top of a concrete plan, not a reason to write the plan itself at the goal level only.
- `findings.md` is **appended, never rewritten from memory** — a finding only exists once it's on disk
- `progress.md` logs what was run and what came back, so a crashed session resumes at the last known state, not at zero

## Recitation, not memory

- Re-read the plan **before deciding**, not once at the start — after 50+ tool calls the original goals get crowded out of the window
- Check a box **right after the milestone**, not batched for later — a finished-but-unchecked box is a lie the next session inherits
- Log failures in the plan file too — an error that isn't recorded repeats itself (`honest-artifacts`)
- **Write progress updates into `progress.md` more deliberately than you'd otherwise narrate out loud** — you tend to produce fewer user-facing updates between tool calls during a long agentic run, which makes the on-disk log the place visibility actually lives for this pattern. If anyone (a future session, a teammate, the user) needs to see what happened without replaying the whole run, `progress.md` is where that visibility has to be, since the run itself won't surface much of it live.
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
| "I don't need to log progress, I'll just say what happened at the end" | Long runs here produce little live narration by default — if it isn't on disk in `progress.md`, it effectively didn't get surfaced |

## Calibration notes

- This pattern is specifically suited to how you tend to work: long autonomous stretches between check-ins, and strong step-by-step reasoning once a phase is underway. Lean into that for *live execution* — trust your own reasoning to work out the moment-by-moment sequence within a phase rather than needing it pre-scripted. But keep writing `task_plan.md` itself with concrete enough detail per phase to survive a handoff to a context with none of that reasoning (see above) — and lean harder on `progress.md` as the place explicit status actually gets recorded, since it won't happen much in the live conversation otherwise.
