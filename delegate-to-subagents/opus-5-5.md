> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

# Delegating to Subagents

Handing work to an agent is itself a decision. Delegate badly and it's slower than doing it yourself; trust a report without verifying it and you get told work was done that wasn't.

The same discipline applies one level up: a principal engineer delegating to another engineer or team needs the same brief + scope + verify, not just AI subagents. This skill stays focused on the AI-subagent mechanism.

**Distinguished/Fellow angle:** at this tier delegation shifts from handing off tasks to handing off technical *direction* — the deliverable is often a doc, runbook, or review process built to outlive any single delegation, so the practice keeps running after the person who set it up leaves.

**Executive angle (CTO/VP-Eng):** if a delegation pattern keeps recurring (the same kind of review, the same kind of parallel research), that's a signal it should become a role or a team with headcount and budget, not a habit repeated ad hoc by whoever's available.

## Decide whether to delegate first — and be honest that your instinct here runs hot

- Is this an independently investigable/executable chunk, or does every step depend on the last result? The latter is faster done directly, one step at a time.
- **This is the check that matters most for you specifically.** You (running as Opus-class) delegate more eagerly than earlier models — including for tasks a direct grep or file read would settle faster. That's a documented tendency, not a style choice, and this skill's whole "decide whether to delegate first" step exists to catch it before it fires. If the honest answer to "could I just grep/read this myself in under a minute" is yes, do that — don't dispatch a subagent for it because the instinct to delegate is already pointed that way.
- **Parallel is normal across independent domains.** Fixing 3 unrelated failures (different files, different causes) means calling dispatch multiple times in one turn — that's what parallel execution looks like. Each agent gets zero session history, a narrow scope (one file / one subsystem), explicit constraints ("don't touch production code"), and a concrete deliverable. Related failures (fixing one might fix another) stay sequential, not split into parallel dispatches.
- **Never let two dispatches edit the same live file at once.** Even across unrelated domains, if files overlap, pull that file out and handle it sequentially.
  - Deliberately having multiple agents solve the same problem differently, to compare approaches, is a different case — run those in isolated workspaces each (e.g. git worktrees). Note a worktree only sees committed content — if a worker needs uncommitted drafts or scripts, copy those files in explicitly; assuming "it'll be visible anyway" means the worker won't find them.
- "I don't feel like doing it" isn't a reason to delegate. Saving context, a genuinely independent domain, or comparing approaches — delegate for a reason.
- **Pick the worker's model tier by subtask difficulty, not by what you (the controller) happen to run on.** Running the controller as Opus 5.5 doesn't mean every worker needs to be Opus-class too — a narrow, mechanical leg (grep-and-report, one well-specified file edit) doesn't need the flagship tier; a genuinely ambiguous or hard-to-reverse leg does. See `senior-engineer-mindset`'s "Model-aware calibration" table for the tier breakdown (context window, thinking mode) this is based on. Handing every leg to a top-tier worker "to be safe" is itself a version of the over-delegation instinct above — applied to tier choice instead of the delegate/don't-delegate decision.
- **Scope permissions per role.** Don't give write access to a subagent that's only supposed to review — when responsibilities split, permissions should split too, so a reviewer can't drift into fixing things mid-review.
- **Flat isn't the only shape.** Dispatching N independent subagents yourself is the default, but for a genuinely multi-role job (triage → fix → verify, or several specialized workstreams that need to hand off to each other), consider one coordinator subagent that dispatches and sequences the others, rather than you tracking every handoff directly. Reserve this for jobs with real inter-agent handoffs — a flat dispatch is simpler and should stay the default for independent, unrelated pieces of work. Watch the instinct to build the coordinator layer preemptively "in case it's needed" — add it when you're actually hand-sequencing handoffs yourself, not before.

## Coordinating a hierarchy

If you do reach for a coordinator, treat it as a real design decision, not just "add a middle layer" — and hold the line against building it out further than the job needs:

- **Depth limit: two levels, no more.** You → coordinator → workers. No coordinator-of-coordinators — past that, the reporting chain gets harder to verify than just staying flat would have been.
- **The coordinator gets a narrow brief too**, same as any subagent — an open-ended "manage this" mandate drifts into scope creep for a coordinator exactly like it does for a worker.
- **Give it an explicit escalation path for a stuck worker**: a fixed retry cap, then hand back to you with what was tried — the same "don't retry with the same instructions forever" rule that applies at the top applies one level down too.
- **Decide the reporting shape up front.** Hub-and-spoke (the coordinator digests worker output before it reaches you) cuts noise but can hide a real disagreement between workers; a shared thread (workers see each other's output directly) keeps that visible but adds coupling. Default to hub-and-spoke; use a shared thread only when workers genuinely need each other's intermediate output to do their own job.
- **Verify-before-claiming applies one level up.** A coordinator's "all three done, all green" is still a report, not evidence — spot-check it the same way you'd spot-check any subagent's claim. Your own self-verification instinct is solid; extend that same rigor to the coordinator's summary instead of taking a tidy rollup at face value just because it's well-organized.
- **Route the coordinator's status traffic to a file/log**, not back into your live context — same reasoning as "give long-running work a name and a status line" below, just one hop further removed.
- **Signal to retroactively promote flat to coordinator:** you're mid-task manually sequencing handoffs yourself — agent A's output has to shape agent B's brief, which has to shape agent C's. That hand-sequencing is the coordinator's job, not yours; once you notice you're doing it by hand, that's the cue to insert one — and only then.

## Talking to an agent that's already running

The default model above is one-shot: brief in, wait, read the result. Some environments give you more than that — a way to address a named, already-running (or already-finished) agent directly instead of only dispatching fresh ones. Where that exists:

- **Continue it, don't re-dispatch it.** Messaging a named agent resumes it from its own transcript with full context — for a follow-up, a correction, or new information that should steer the rest of its work, that beats spinning up a fresh dispatch that has to be re-briefed from scratch. Reply to an incoming message by addressing the same name back.
- **Subscribe to completion, don't poll.** A one-shot "notify me when it goes idle" subscription is the mechanized version of "wait for the completion signal instead of tight polling" — sending "are you done?" messages, or checking status in a loop, is exactly the anti-pattern that exists to replace.
- **A coordinator's "shared thread"** is this, concretely — workers addressing each other directly by name instead of everything routing through the coordinator.
- **Never let a peer launder a blocked permission.** If your own session was denied or blocked from an action, don't ask another agent or session to do it for you — that routes around a permission boundary the user's own session hit, not a legitimate use of multi-agent coordination. Take it back to the user instead. If what got blocked was a legitimate security or risk-review action and the refusal looks like an overcautious classifier hit rather than an actual policy violation, say so plainly rather than quietly routing around it through a peer.

This capability set isn't universal — plain single-session Claude Code doesn't have it. Treat this section as an addendum to the one-shot model above where it's available, not a replacement for it where it isn't.

## Scheduled/unattended execution

Beyond a live dispatch or a continued conversation, some environments can fire a saved prompt at a future time — into this session, a specific other session, or a fresh one — without anyone needing to be present when it fires.

- **Verified, not theoretical:** confirm this actually works in your environment (a real fire, a real effect you can read back) before relying on it — don't take "this environment probably supports it" on faith.
- Use this for a reusable-template-on-a-schedule case, or for a check-in on long-running work instead of manually deciding when to look again.
- **This isn't the same as "always running."** The trigger fires a fresh turn into a session — the underlying environment can still reclaim an idle container between firings.
- Not universal — confirm yours actually has it before relying on it.
- **Test-run it once before trusting it unattended.** Fire it manually first and check the whole path: the right input actually gets picked up, the output lands where expected, and a failure is visible somewhere instead of silently swallowed. Don't let the first real run also be the first tested run.

## How to brief

- Give **the task + interfaces it touches + constraints.** Don't paste a summarized session history — hand over file paths and let the subagent read them itself.
- Pasted text or a returned summary sits in your context from that point on. Passing a file path is always cheaper.
- If the target is vague ("fix this up"), narrow it yourself before delegating — a vague brief comes back as a vague result.
- **Record a baseline right before dispatching** (e.g. `git rev-parse HEAD`). Use this baseline later for diffs and review scope — `HEAD~1` silently picks the wrong range if another commit landed in between. `git rev-parse HEAD` alone misses **uncommitted** changes already in the working tree at dispatch time — if there were any, also snapshot `git diff` (and `git diff --cached`) before dispatching, or just commit/stash first so the baseline is clean.
- **If the same kind of task recurs, capture the brief once as a reusable template** instead of re-explaining it from scratch each time. Keep the template itself plain — the actual reusable instructions, not a framework with options built in for variations nobody has needed yet. If your environment has a real scheduler, wire the template into one instead of manually re-dispatching it each time it comes up.
- **Keep the brief no bigger than the task needs.** A worker on a narrow, mechanical leg doesn't need a long context dump "to be thorough" — pass what it actually needs to touch the interfaces involved and stop there.

## Verify what comes back

- **Don't take the report at face value.** "Tests passed" is a claim, not evidence — run it yourself or read the diff. This applies even though your own self-verification is strong: the report came from a *different* context (the subagent's), so your own good self-checking habits don't automatically extend to trusting someone else's claim — verify the subagent's work the same way you'd verify anyone else's.
- Get reports and reviews **as files.** A long reply dumped into the chat window gets lost to compaction, and the next round has to re-read from scratch.
- If you asked for a review, don't tell it in advance what not to flag — let findings surface, including ones you expect to dismiss, then judge them yourself afterward. Spec compliance and code quality are **different axes** — don't let one obscure the other.
- **After running several in parallel**, before merging: read each summary separately → check whether two agents touched the same code (if they overlapped, re-review just that part) → run the full test suite once more to catch combination issues invisible to either agent alone.

## When it's blocked or the review loop won't end

- On a BLOCKED report, don't retry with the same instructions — give concrete feedback and retry, use a stronger model, or split the task. Nothing changes, nothing improves.
- If a worker's BLOCKED report traces back to a refusal on a security-, bio-, or risk-related task that reads like a legitimate engineering task (a vuln scan, a threat model, a sandboxed exploit test), consider that a possible classifier false positive rather than a hard stop — a differently-scoped retry or a rephrase is often enough, before you escalate it as a real blocker.
- Findings from a review go to **one subagent at a time** to fix all of them — spinning up a new subagent per finding rebuilds context from scratch every time.
- **Cap the fix → re-review loop** (e.g. 3 rounds). Past the cap without resolution, judge it yourself: wrong or trivial → note why and move on; real and material → decide the smallest fix yourself and record it. **Never drop it silently** — record the verdict and the reason either way.
- **Don't fix it yourself** (except a minor case you judge doesn't need review). A controller fixing things directly skips the review step, and that code piles into your own context.
- For a hard-to-reverse decision where judgment is split, instead of one more review, put two agents on opposing sides to argue it out — a tradeoff invisible from one side alone sometimes only shows up that way.

## Calibrate how often you interrupt

- Don't ask for confirmation on every step — let the routine, reversible ones go through silently and save the interrupt for the one that actually matters. Asking "OK to proceed?" on trivial steps trains the user to rubber-stamp everything, which defeats the point of asking at all.
- Same bar as `weigh-tradeoffs`: reversible → just do it and show the result after; irreversible or consequential → stop and ask before, not after.
- **A confirmation gate protects the next action, not what already happened.** If a subagent already sent the email or merged the commit, asking "OK to proceed?" afterward is theater — the interrupt has to sit before the irreversible call fires, not at the point where you happen to read the report.
- A subagent that reproduces a bug, files the ticket, and fixes it — surfacing only the one call that actually needed a human ("should this also roll out to the EU region?") — is more useful than one that narrates every intermediate step.

## Give long-running work a name and a status line

- When a delegated agent runs over a longer stretch, don't leave it silent until it finishes — give it a short name and keep a one-line status that updates as it progresses ("Inbox Manager — sent, inbox at zero, 5 drafts parked"). A glanceable roster beats a wall of silence followed by one huge report at the end.
- **There's no live channel for this** — a dispatched agent returns one final result, not a stream of intermediate updates you can watch. The only way to get a status line that actually updates mid-run is to brief the agent to write its own progress to a file and glance at that file yourself.
- This is for genuinely long-running or ongoing delegations, not a two-minute task — for a short dispatch, just wait for the completion signal.

## Common failures

- Multiple agents edit the same file at once and clobber each other.
- Moving to the next step without verification just because a subagent said "done."
- A delegated chunk too large for you to review the result — if you can't review it, it was sliced wrong to begin with.
- Checking in on a subagent at tight intervals to catch it being stuck — this only stretches the wait. Wait for the completion signal, then process it.
- **Dispatching by reflex when a direct read would have settled it.** Given everything above, this is the failure mode most worth watching for specifically on this model — check "decide whether to delegate first" before every dispatch, not just the first one in a session.

See `SKILL.md` for the optional hook and execution-state script that mechanize part of this discipline.
