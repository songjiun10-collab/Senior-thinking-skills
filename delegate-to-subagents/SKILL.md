---
name: delegate-to-subagents
description: >-
  Decide when to hand work to a subagent instead of doing it yourself, how to brief it, how to run the fix/review loop when something comes back wrong, and how to verify what comes back. Use when a task is big enough to delegate (independent research, a parallelizable slice, a second opinion, a review pass), when running more than one agent, when a subagent's report claims something is finished, or when a review comes back with findings that need fixing. Skip for single-step edits or when no subagent tooling is available. Bundles an optional PreToolUse/PostToolUse hook (scripts/check_dispatch_brief.py) that nudges on two of the mistakes this skill warns about.
---

# Delegating to Subagents

Handing work to an agent is itself a decision. Delegate badly and it's slower than doing it yourself; trust a report without verifying it and you get told work was done that wasn't.

The same discipline applies one level up: a principal engineer delegating to another engineer or team needs the same brief + scope + verify, not just AI subagents. This skill stays focused on the AI-subagent mechanism, since that's what the hook below actually wires up.

**Distinguished/Fellow angle:** at this tier delegation shifts from handing off tasks to handing off technical *direction* — the deliverable is often a doc, runbook, or review process built to outlive any single delegation, so the practice keeps running after the person who set it up leaves.

**Executive angle (CTO/VP-Eng):** if a delegation pattern keeps recurring (the same kind of review, the same kind of parallel research), that's a signal it should become a role or a team with headcount and budget, not a habit repeated ad hoc by whoever's available.

## Decide whether to delegate first

- Is this an independently investigable/executable chunk, or does every step depend on the last result? The latter is faster done directly, one step at a time.
- **Parallel is normal across independent domains.** Fixing 3 unrelated failures (different files, different causes) means calling dispatch multiple times in one turn — that's what parallel execution looks like. Each agent gets zero session history, a narrow scope (one file / one subsystem), explicit constraints ("don't touch production code"), and a concrete deliverable. Related failures (fixing one might fix another) stay sequential, not split into parallel dispatches.
- **Never let two dispatches edit the same live file at once.** Even across unrelated domains, if files overlap, pull that file out and handle it sequentially.
  - Deliberately having multiple agents solve the same problem differently, to compare approaches, is a different case — run those in isolated workspaces each (e.g. git worktrees). Note a worktree only sees committed content — if a worker needs uncommitted drafts or scripts, copy those files in explicitly; assuming "it'll be visible anyway" means the worker won't find them.
- "I don't feel like doing it" isn't a reason to delegate. Saving context, a genuinely independent domain, or comparing approaches — delegate for a reason.
- **Scope permissions per role.** Don't give write access to a subagent that's only supposed to review — when responsibilities split, permissions should split too, so a reviewer can't drift into fixing things mid-review.
- **Flat isn't the only shape.** Dispatching N independent subagents yourself is the default, but for a genuinely multi-role job (triage → fix → verify, or several specialized workstreams that need to hand off to each other), consider one coordinator subagent that dispatches and sequences the others, rather than you tracking every handoff directly. Reserve this for jobs with real inter-agent handoffs — a flat dispatch is simpler and should stay the default for independent, unrelated pieces of work.

## Coordinating a hierarchy

If you do reach for a coordinator, treat it as a real design decision, not just "add a middle layer":

- **Depth limit: two levels, no more.** You → coordinator → workers. No coordinator-of-coordinators — past that, the reporting chain gets harder to verify than just staying flat would have been.
- **The coordinator gets a narrow brief too**, same as any subagent — an open-ended "manage this" mandate drifts into scope creep for a coordinator exactly like it does for a worker.
- **Give it an explicit escalation path for a stuck worker**: a fixed retry cap, then hand back to you with what was tried — the same "don't retry with the same instructions forever" rule that applies at the top applies one level down too.
- **Decide the reporting shape up front.** Hub-and-spoke (the coordinator digests worker output before it reaches you) cuts noise but can hide a real disagreement between workers; a shared thread (workers see each other's output directly) keeps that visible but adds coupling. Default to hub-and-spoke; use a shared thread only when workers genuinely need each other's intermediate output to do their own job.
- **Verify-before-claiming applies one level up.** A coordinator's "all three done, all green" is still a report, not evidence — spot-check it the same way you'd spot-check any subagent's claim.
- **Route the coordinator's status traffic to a file/log**, not back into your live context — same reasoning as "give long-running work a name and a status line" below, just one hop further removed.
- **Signal to retroactively promote flat to coordinator:** you're mid-task manually sequencing handoffs yourself — agent A's output has to shape agent B's brief, which has to shape agent C's. That hand-sequencing is the coordinator's job, not yours; once you notice you're doing it by hand, that's the cue to insert one.

## How to brief

- Give **the task + interfaces it touches + constraints.** Don't paste a summarized session history — hand over file paths and let the subagent read them itself.
- Pasted text or a returned summary sits in your context from that point on. Passing a file path is always cheaper.
- If the target is vague ("fix this up"), narrow it yourself before delegating — a vague brief comes back as a vague result.
- **Record a baseline right before dispatching** (e.g. `git rev-parse HEAD`). Use this baseline later for diffs and review scope — `HEAD~1` silently picks the wrong range if another commit landed in between. `git rev-parse HEAD` alone misses **uncommitted** changes already in the working tree at dispatch time — if there were any, also snapshot `git diff` (and `git diff --cached`) before dispatching, or just commit/stash first so the baseline is clean. Otherwise a later "what changed" diff mixes the subagent's work with whatever was already sitting there.
- **If the same kind of task recurs, capture the brief once as a reusable template** instead of re-explaining it from scratch each time — and fold in corrections as they come up, so the template actually improves with use instead of staying a stale first draft.

## Verify what comes back

- **Don't take the report at face value.** "Tests passed" is a claim, not evidence — run it yourself or read the diff (same principle as `verify-before-claiming`; delegating doesn't exempt you).
- Get reports and reviews **as files.** A long reply dumped into the chat window gets lost to compaction, and the next round has to re-read from scratch.
- If you asked for a review, don't tell it in advance what not to flag — let findings surface, including ones you expect to dismiss, then judge them yourself afterward. Spec compliance and code quality are **different axes** — don't let one obscure the other.
- **After running several in parallel**, before merging: read each summary separately → check whether two agents touched the same code (if they overlapped, re-review just that part) → run the full test suite once more to catch combination issues invisible to either agent alone.

## When it's blocked or the review loop won't end

- On a BLOCKED report, don't retry with the same instructions — give concrete feedback and retry, use a stronger model, or split the task. Nothing changes, nothing improves.
- Findings from a review go to **one subagent at a time** to fix all of them — spinning up a new subagent per finding rebuilds context from scratch every time.
- **Cap the fix → re-review loop** (e.g. 3 rounds). Past the cap without resolution, judge it yourself: wrong or trivial → note why and move on; real and material → decide the smallest fix yourself and record it. **Never drop it silently** — record the verdict and the reason either way.
- **Don't fix it yourself** (except a minor case you judge doesn't need review). A controller fixing things directly skips the review step, and that code piles into your own context.
- For a hard-to-reverse decision where judgment is split, instead of one more review, put two agents on opposing sides to argue it out — a tradeoff invisible from one side alone sometimes only shows up that way (a heavier tool, for situations like `weigh-tradeoffs` / `adversarial-review`).

## Calibrate how often you interrupt

- Don't ask for confirmation on every step — let the routine, reversible ones go through silently and save the interrupt for the one that actually matters. Asking "OK to proceed?" on trivial steps trains the user to rubber-stamp everything, which defeats the point of asking at all.
- Same bar as `weigh-tradeoffs`: reversible → just do it and show the result after; irreversible or consequential → stop and ask before, not after.
- A subagent that reproduces a bug, files the ticket, and fixes it — surfacing only the one call that actually needed a human ("should this also roll out to the EU region?") — is more useful than one that narrates every intermediate step.

## Give long-running work a name and a status line

- When a delegated agent runs over a longer stretch, don't leave it silent until it finishes — give it a short name and keep a one-line status that updates as it progresses ("Inbox Manager — sent, inbox at zero, 5 drafts parked"). A glanceable roster beats a wall of silence followed by one huge report at the end.
- **There's no live channel for this** — a dispatched agent returns one final result, not a stream of intermediate updates you can watch. The only way to get a status line that actually updates mid-run is to brief the agent to write its own progress to a file (e.g. `.claude/status/<name>.md`) and glance at that file yourself; there's nothing to "watch" otherwise.
- This is for genuinely long-running or ongoing delegations, not a two-minute task — for a short dispatch, just wait for the completion signal (see "Common failures" below).

## Common failures

- Multiple agents edit the same file at once and clobber each other
- Moving to the next step without verification just because a subagent said "done"
- A delegated chunk too large for you to review the result — if you can't review it, it was sliced wrong to begin with
- Checking in on a subagent at tight intervals to catch it being stuck — this only stretches the wait. Wait for the completion signal, then process it.

## Optional: enforce with a hook

Two of these principles are mechanically catchable — **pasting a long conversation summary verbatim**, and **too many concurrent open dispatches** (2-3 is normal, more than that trips it) — `scripts/check_dispatch_brief.py` detects both right before an Agent call (PreToolUse). By default it **only warns, it doesn't block** (a default chosen with the assumption this may get installed into projects that aren't your own). To actually block, add the environment variable `DELEGATE_HOOK_STRICT=1` to the hook command — the script's header comment documents the exact behavior.

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/delegate-to-subagents/scripts/check_dispatch_brief.py" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Agent",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/delegate-to-subagents/scripts/check_dispatch_brief.py" }
        ]
      }
    ]
  }
}
```

`Agent` is the built-in dispatch tool's name (some docs/blogs from older Claude Code versions still say `Task` — if your version predates the rename, use that instead and confirm against your own `tool_name` in a hook payload). Hook the same script into both PreToolUse and PostToolUse — PostToolUse closes out the specific dispatch that finished, keyed by the call's `tool_use_id` (hook only one side and open dispatches never get closed). If your skill is installed at a different path, update the command path to match. By default it only warns quietly (visible only in the human-facing transcript) — to make Claude actually react to it (i.e. actually block), prefix the command with `DELEGATE_HOOK_STRICT=1` (`"command": "DELEGATE_HOOK_STRICT=1 python3 ..."`). This hook is example-level enforcement — not a red-team-tested CRITICAL-tier block like Hncs's `protect_never_touch.py`, just a minimal mechanization of this skill's verbal advice. If you need something stronger, use this script as a starting point and adapt it to your project.

**Limitation:** the hook only counts *how many* dispatches are open, it doesn't know *which files* each one touches — two parallel dispatches editing the same file won't trip anything as long as the total count stays under the threshold. Catching that mechanically would mean parsing each brief for the files it intends to touch and cross-checking against the others' — out of scope for this example script; "never let two dispatches edit the same live file" (above) stays something you enforce by reading the briefs yourself.
