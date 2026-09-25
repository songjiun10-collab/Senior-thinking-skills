> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

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

- `task_plan.md` is the resume point — phases with checkboxes, the current phase marked `in_progress`. Write each phase with an explicit exploration scope and completion criterion (what to check, where to stop, what "done" looks like for that phase) — not just a goal statement. That's what lets the plan itself answer "is this phase finished" without the question defaulting to open-ended, indefinite continuation.
- `findings.md` is **appended, never rewritten from memory** — a finding only exists once it's on disk.
- `progress.md` logs what was run and what came back, so a crashed session resumes at the last known state, not at zero.

## Recitation, not memory

- Re-read the plan **before deciding**, not once at the start — after 50+ tool calls the original goals get crowded out of the window. With a 1M+-token window this pattern still applies: even where the raw plan text would technically still fit, re-reading it is what keeps it *weighted* in your actual decision, not just present somewhere in a long context.
- Check a box **right after the milestone**, not batched for later — a finished-but-unchecked box is a lie the next session inherits.
- Log failures in the plan file too — an error that isn't recorded repeats itself (`honest-artifacts`).
- **Principal angle:** a plan another team or a future session resumes sets a pattern — write it so someone with zero context lands at the current phase, not at zero. Losing it to compaction costs their velocity, not just yours.
- **Distinguished/Fellow angle:** a plan that accumulates across months of sessions is a company asset only while it stays honest — review it the way `persistent-memory` says, resolve conflicting entries, delete what fossilized. One that only makes sense with unwritten context is a bus-factor-of-one liability.
- **Executive angle (CTO/VP-Eng):** agents re-orienting for half a session after every crash are an engineering-cost line, and a plan that lets an agent declare "done" early is a delivery-risk decision — worth standardizing the pattern across teams rather than leaving it to each agent's habit.

## Completion is a gate, not a feeling

- No "done" while a checkbox stands unchecked or a phase is `in_progress` — `verify-before-claiming` applies to the plan itself, not just the code. State this as the literal completion criterion for the run, since the pull otherwise is to stay cautious about declaring a phase finished rather than checking it against the boxes and moving on.
- **A checked box has to stay checked.** A user report ([openai/codex#46700](https://github.com/openai/codex/issues/46700), one instance, not a documented rate) describes a long unattended run at high effort that repeatedly reverted and rewrote its own earlier changes — "completed phases were never treated as done" — while writing close to 1TB to `/tmp` over a full day without finishing the plan. Re-read `task_plan.md` before revisiting a phase already checked off; reopening one is a decision to log, not something to slide into while chasing a later phase.
- The plan files are **working memory, not a deliverable**: gitignored by default, overwritten by the next task. Anything worth keeping gets promoted into code, a commit, or a doc.
- Corrections and preferences belong in `persistent-memory` (durable per-topic files); execution state belongs here. Don't mix them.

## Parallel tasks

Isolated directories, not one shared root plan: `.planning/YYYY-MM-DD-slug/` with the same three files inside. Two sessions writing one root `task_plan.md` overwrite each other's phases. State explicitly which phases or files a subagent owns when splitting a plan across delegates — this tier's default leans toward under-delegating a genuinely parallelizable plan rather than splitting it out on its own.

## Warning signs

| Thought | Reality |
|---|---|
| "The plan is in my context, I'll remember" | Context dies on /clear, compaction, or hour ten |
| "Basically done" (2 of 5 boxes checked) | The boxes are the gate, not a feeling |
| "I'll write the findings down at the end" | A finding not on disk when discovered gets re-derived or lost |
| "One shared plan file is fine for two agents" | They overwrite each other's phases |
| "I have a huge context window, I don't need to re-read the plan file" | Fitting in context isn't the same as staying weighted in the decision — re-read it anyway |
| "I should check in before starting the next phase" | If the plan already states the phase and its completion criterion, act on it — check in only where the plan is genuinely ambiguous |

## Calibration notes

- **Write explicit completion criteria and exploration scope into every phase of `task_plan.md`.** This is the single highest-leverage change for this tier: a phase written as a bare goal invites either premature "done" calls that don't hold up or open-ended continuation past what the task needs. A phase written with "check X, Y, Z; stop when the verification gate passes" gives a concrete stopping point either way.
- **Act on the plan rather than confirming it before each phase.** Once `task_plan.md` states the next phase and its scope, start it — infer the intent behind ambiguous phase wording from the surrounding findings and plan context rather than pausing to ask, and raise only the genuine blockers.
- **Delegation across a plan's phases needs to be spelled out.** When phases are independent enough to split across subagents, say so explicitly in the plan file (who owns which phase, which files); don't rely on it happening by default.
- No need for a separate "make sure you verify the checkboxes" instruction — checking real state against the plan before declaring a phase done is expected to happen without being told each time.
- Keep `progress.md` entries and phase descriptions in plain, direct prose — what ran, what came back, what's next — rather than a "not X but Y" framing of a decision. Keep the checkbox lists and the warning-sign table as-is; they're genuinely parallel and belong as lists.
