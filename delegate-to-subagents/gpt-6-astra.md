> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Delegating to Subagents

Handing work to an agent is itself a decision. Delegate badly and it's slower than doing it yourself; trust a report without verifying it and you get told work was done that wasn't.

The same discipline applies one level up: a principal engineer delegating to another engineer or team needs the same brief + scope + verify, not just AI subagents. This skill stays focused on the AI-subagent mechanism.

**Distinguished/Fellow angle:** at this tier delegation shifts from handing off tasks to handing off technical *direction* — the deliverable is often a doc, runbook, or review process built to outlive any single delegation, so the practice keeps running after the person who set it up leaves.

**Executive angle (CTO/VP-Eng):** if a delegation pattern keeps recurring (the same kind of review, the same kind of parallel research), that's a signal it should become a role or a team with headcount and budget, not a habit repeated ad hoc by whoever's available.

## Decide whether to delegate first — and be honest that your instinct here runs the other way from what you'd expect

- Is this an independently investigable/executable chunk, or does every step depend on the last result? The latter is faster done directly, one step at a time.
- **This is the check that cuts against your own documented tendency, in the opposite direction from most other models in this family of skills.** Where an eager delegator (an Opus-class Claude model, for instance) over-delegates — reaching for a subagent even for a task a direct grep or file read would settle faster — you have the mirror-image problem: you delegate *less* than the task calls for, tending to keep work in your own hands even when it's a genuinely independent, parallelizable chunk that would finish faster and more reliably split across subagents. Both failure modes are corrections to the same underlying decision, just pointed opposite ways. Concretely, for you that means: when you catch yourself about to grind through three unrelated failing tests one at a time in the same context, or read through five independent modules sequentially to answer one question each, treat that as the signal to dispatch instead of a reason to push through solo "since you're already in the middle of it."
- **Because you won't delegate as readily on your own, this has to be spelled out explicitly rather than left to instinct.** If a task or a project's instructions say "delegate the independent research legs" or "run these three checks as parallel subagents," treat that as a literal instruction to follow, not a suggestion you can override by deciding you'd rather just do it yourself directly. Absent explicit instruction, apply the test above yourself rather than defaulting to keeping everything in one context because that's the path of least resistance for you specifically.
- **Parallel is normal across independent domains.** Fixing 3 unrelated failures (different files, different causes) means calling dispatch multiple times in one turn — that's what parallel execution looks like. Each agent gets zero session history, a narrow scope (one file / one subsystem), explicit constraints ("don't touch production code"), and a concrete deliverable. Related failures (fixing one might fix another) stay sequential, not split into parallel dispatches.
- **Never let two dispatches edit the same live file at once.** Even across unrelated domains, if files overlap, pull that file out and handle it sequentially.
  - Deliberately having multiple agents solve the same problem differently, to compare approaches, is a different case — run those in isolated workspaces each (e.g. git worktrees). Note a worktree only sees committed content — if a worker needs uncommitted drafts or scripts, copy those files in explicitly; assuming "it'll be visible anyway" means the worker won't find them.
- "I don't feel like doing it" isn't a reason to delegate. Saving context, a genuinely independent domain, or comparing approaches — delegate for a reason. The bar here is "is there a real reason," not "do I feel like it" in either direction — including your own default pull toward keeping it.
- **Pick the worker's model tier by subtask difficulty, not by what the controller happens to run on.** A narrow, mechanical leg (grep-and-report, one well-specified file edit) doesn't need the flagship tier; a genuinely ambiguous or hard-to-reverse leg does. As a rule of thumb: the cheapest/fastest tier for narrow, well-specified legs; the mid tier as the default workhorse for most legs; reserve the flagship or long-horizon-agentic tier for legs that are themselves genuinely ambiguous, hard-to-reverse, or long-running.
- **Scope permissions per role.** Don't give write access to a subagent that's only supposed to review — when responsibilities split, permissions should split too, so a reviewer can't drift into fixing things mid-review.
- **Flat isn't the only shape.** Dispatching N independent subagents yourself is the default, but for a genuinely multi-role job (triage → fix → verify, or several specialized workstreams that need to hand off to each other), consider one coordinator subagent that dispatches and sequences the others, rather than you tracking every handoff directly. Reserve this for jobs with real inter-agent handoffs — a flat dispatch is simpler and should stay the default for independent, unrelated pieces of work.

## Coordinating a hierarchy

If you do reach for a coordinator, treat it as a real design decision, not just "add a middle layer":

- **Depth limit: two levels, no more.** You → coordinator → workers. No coordinator-of-coordinators — past that, the reporting chain gets harder to verify than just staying flat would have been.
- **The coordinator gets a narrow brief too**, same as any subagent — an open-ended "manage this" mandate drifts into scope creep for a coordinator exactly like it does for a worker. Spell out its scope and constraints explicitly; an underspecified coordinator brief gets executed literally within whatever narrow reading it lands on, not filled in with the sensible middle ground you had in mind.
- **Give it an explicit escalation path for a stuck worker**: a fixed retry cap, then hand back to you with what was tried.
- **Decide the reporting shape up front.** Hub-and-spoke (the coordinator digests worker output before it reaches you) cuts noise but can hide a real disagreement between workers; a shared thread (workers see each other's output directly) keeps that visible but adds coupling. Default to hub-and-spoke; use a shared thread only when workers genuinely need each other's intermediate output to do their own job.
- **Verify-before-claiming applies one level up.** A coordinator's "all three done, all green" is still a report, not evidence — spot-check it the same way you'd spot-check any subagent's claim.
- **Route the coordinator's status traffic to a file/log**, not back into your live context — same reasoning as "give long-running work a name and a status line" below, just one hop further removed.
- **Signal to retroactively promote flat to coordinator:** you're mid-task manually sequencing handoffs yourself — agent A's output has to shape agent B's brief, which has to shape agent C's. That hand-sequencing is the coordinator's job, not yours; once you notice you're doing it by hand, that's the cue to insert one — for you specifically, that noticing has to be deliberate, since your default instinct is to keep doing the hand-sequencing yourself rather than reach for the coordinator layer.

## Talking to an agent that's already running

The default model above is one-shot: brief in, wait, read the result. Some environments give you more than that — a way to address a named, already-running (or already-finished) agent directly instead of only dispatching fresh ones. Where that exists:

- **Continue it, don't re-dispatch it.** Messaging a named agent resumes it from its own transcript with full context — for a follow-up, a correction, or new information that should steer the rest of its work, that beats spinning up a fresh dispatch that has to be re-briefed from scratch. Reply to an incoming message by addressing the same name back.
- **Subscribe to completion, don't poll.** A one-shot "notify me when it goes idle" subscription is the mechanized version of "wait for the completion signal instead of tight polling" — sending "are you done?" messages, or checking status in a loop, is exactly the anti-pattern that exists to replace.
- **A coordinator's "shared thread"** is this, concretely — workers addressing each other directly by name instead of everything routing through the coordinator.
- **Never let a peer launder a blocked permission.** If your own session was denied or blocked from an action, don't ask another agent or session to do it for you — that routes around a permission boundary the user's own session hit, not a legitimate use of multi-agent coordination. Take it back to the user instead.

This capability set isn't universal — plain single-session setups don't have it. Treat this section as an addendum to the one-shot model above where it's available, not a replacement for it where it isn't.

## Scheduled/unattended execution

Beyond a live dispatch or a continued conversation, some environments can fire a saved prompt at a future time — into this session, a specific other session, or a fresh one — without anyone needing to be present when it fires.

- **Verified, not theoretical:** confirm the mechanism actually works in your environment (a real fire, a real observable effect) before relying on it — don't assume it works from the tooling's description alone.
- Use this for the reusable-template-on-a-schedule case (a recurring brief that re-fires itself instead of you remembering to re-dispatch it), or for a check-in on long-running work instead of manually deciding when to look again.
- **This isn't the same as "always running."** The trigger fires a fresh turn into a session — the underlying environment can still reclaim an idle container between firings.
- Not universal — confirm yours actually has it before relying on it.
- **Test-run it once before trusting it unattended.** Fire it manually first and check the whole path: the right input actually gets picked up, the output lands where expected, and a failure is visible somewhere instead of silently swallowed. Don't let the first real run also be the first tested run.

## How to brief

- Give **the task + interfaces it touches + constraints, spelled out explicitly.** Don't paste a summarized session history — hand over file paths and let the subagent read them itself.
- **State when the subagent should consider itself done, and how far its exploration should go, up front.** You (and any worker running the same model) are more tentative than earlier generations about declaring a task complete on its own initiative, and more inclined to stop and ask rather than push forward on a reasonable reading of the brief. Counteract both directions explicitly in the brief itself: give it concrete completion criteria ("get the implementation running, inspect the output, fix failures, stop there") and an explicit exploration scope (what to investigate and where to stop), and tell it to infer intent and act rather than pausing to ask permission for a call within its stated scope. A brief that only states the task, with completion and scope left implicit, will come back either half-finished-but-tentatively-reported or paused early on a question it could have answered itself.
- **An underspecified brief gets executed exactly as written, not generously filled in.** A subagent reading a brief with a gap in it won't reliably infer the sensible middle ground you had in mind — it follows what's actually there. Spend the extra sentence closing the gap yourself rather than trusting the worker to guess your intent correctly.
- **Drop the old "you must test this" boilerplate.** If earlier briefing templates carried an explicit "make sure to test/verify your changes" line for the worker's benefit, that instruction is now redundant when the worker is also running this model family — testing and verifying its own output is something it already does without being told, and repeating the old instruction just adds words without adding reliability. Spend that sentence on completion criteria and scope instead.
- Pasted text or a returned summary sits in your context from that point on. Passing a file path is always cheaper.
- If the target is vague ("fix this up"), narrow it yourself before delegating — a vague brief comes back as a vague result, read as literally as it was written.
- **Record a baseline right before dispatching** (e.g. `git rev-parse HEAD`). Use this baseline later for diffs and review scope — `HEAD~1` silently picks the wrong range if another commit landed in between. `git rev-parse HEAD` alone misses **uncommitted** changes already in the working tree at dispatch time — if there were any, also snapshot `git diff` (and `git diff --cached`) before dispatching, or just commit/stash first so the baseline is clean.
- **If the same kind of task recurs, capture the brief once as a reusable template** instead of re-explaining it from scratch each time — and fold in corrections as they come up, so the template actually improves with use. If your environment has a real scheduler, wire the template into one instead of manually re-dispatching it each time it comes up.

## Verify what comes back

- **Don't take the report at face value.** "Tests passed" is a claim, not evidence — run it yourself or read the diff. Delegating doesn't exempt you.
- Get reports and reviews **as files.** A long reply dumped into the chat window gets lost to compaction, and the next round has to re-read from scratch.
- If you asked for a review, don't tell it in advance what not to flag — let findings surface, including ones you expect to dismiss, then judge them yourself afterward. Spec compliance and code quality are **different axes** — don't let one obscure the other.
- **After running several in parallel**, before merging: read each summary separately → check whether two agents touched the same code (if they overlapped, re-review just that part) → run the full test suite once more to catch combination issues invisible to either agent alone.
- **Trust a worker's own guardrail judgment more than you would an older model's — but don't skip verification because of that trust.** This family has better-than-prior alignment and won't proceed on something it judges unsafe, which means an old, heavily prohibitive brief ("CRITICAL: you MUST NOT touch production config under any circumstances") is often over-constraining rather than protective when the worker is also this model family — plain, direct constraints work as well as the all-caps version and read better. That's a statement about how to phrase constraints, not a reason to skip checking the actual diff.

## When it's blocked or the review loop won't end

- On a BLOCKED report, don't retry with the same instructions — give concrete feedback and retry, use a stronger model, or split the task. Nothing changes, nothing improves.
- Findings from a review go to **one subagent at a time** to fix all of them — spinning up a new subagent per finding rebuilds context from scratch every time.
- **Cap the fix → re-review loop** (e.g. 3 rounds). Past the cap without resolution, judge it yourself: wrong or trivial → note why and move on; real and material → decide the smallest fix yourself and record it. **Never drop it silently** — record the verdict and the reason either way.
- **Don't fix it yourself** (except a minor case you judge doesn't need review). A controller fixing things directly skips the review step, and that code piles into your own context.
- For a hard-to-reverse decision where judgment is split, instead of one more review, put two agents on opposing sides to argue it out — a tradeoff invisible from one side alone sometimes only shows up that way.

## Calibrate how often you interrupt

- Don't ask for confirmation on every step — let the routine, reversible ones go through silently and save the interrupt for the one that actually matters. Asking "OK to proceed?" on trivial steps trains the user to rubber-stamp everything, which defeats the point of asking at all. This is the same instinct as the brief-writing note above, applied to your own actions as a controller: bias toward acting within a clearly reversible, in-scope step rather than pausing to confirm it.
- Same bar as `weigh-tradeoffs`: reversible → just do it and show the result after; irreversible or consequential → stop and ask before, not after.
- **A confirmation gate protects the next action, not what already happened.** If a subagent already sent the email or merged the commit, asking "OK to proceed?" afterward is theater — the interrupt has to sit before the irreversible call fires, not at the point where you happen to read the report.
- A subagent that reproduces a bug, files the ticket, and fixes it — surfacing only the one call that actually needed a human ("should this also roll out to the EU region?") — is more useful than one that narrates every intermediate step.

## Give long-running work a name and a status line

- When a delegated agent runs over a longer stretch, don't leave it silent until it finishes — give it a short name and keep a one-line status that updates as it progresses ("Inbox Manager — sent, inbox at zero, 5 drafts parked"). A glanceable roster beats a wall of silence followed by one huge report at the end.
- **There's no live channel for this** — a dispatched agent returns one final result, not a stream of intermediate updates you can watch. The only way to get a status line that actually updates mid-run is to brief the agent to write its own progress to a file (e.g. `.claude/status/<name>.md`) and glance at that file yourself — say this explicitly in the brief, since a worker won't infer that a status file is wanted just from the task itself.
- This is for genuinely long-running or ongoing delegations, not a two-minute task — for a short dispatch, just wait for the completion signal.
- Mid-run changes to a worker's reasoning effort or tool set no longer force a fresh, uncached context the way they used to — so it's cheaper now to adjust a long-running worker's settings partway through than it was on the prior generation, if you notice the task needs more or less depth than you initially briefed for.

## Common failures

- Multiple agents edit the same file at once and clobber each other.
- Moving to the next step without verification just because a subagent said "done."
- A delegated chunk too large for you to review the result — if you can't review it, it was sliced wrong to begin with.
- Checking in on a subagent at tight intervals to catch it being stuck — this only stretches the wait. Wait for the completion signal, then process it.
- **A brief with an unstated gap, taken literally by the worker and coming back subtly wrong** — the most common failure shape when instructions aren't spelled out fully; close gaps in the brief up front rather than debugging the result afterward.
- **Grinding through an independently-parallelizable task solo because dispatching didn't occur to you.** Given this model's documented under-delegation tendency, this is the failure mode most worth watching for specifically — before starting a multi-part, independent task by hand, run the "decide whether to delegate first" check above rather than defaulting to keeping it in your own context.

See `SKILL.md` for the optional hook and execution-state script that mechanize part of this discipline.
