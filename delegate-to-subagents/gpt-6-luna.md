> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Delegating to Subagents

Handing work to an agent is itself a decision. Delegate badly and it's slower than doing it yourself; trust a report without verifying it and you get told work was done that wasn't.

The same discipline applies one level up: a principal engineer delegating to another engineer or team needs the same brief + scope + verify, not just AI subagents. This skill stays focused on the AI-subagent mechanism.

**You're built for the leaf, not the trunk.** This tier is the cheapest, fastest one in this family, and it's aimed at high-volume, narrow tasks — classification, extraction, routing, structured summarization — not the demanding or ambiguous work a controller has to be able to judge. The practical read for this skill: you're almost always the *worker* being dispatched, not the one doing the dispatching. Read the rest of this file with that in mind — most of it describes decisions a controller makes about you, not decisions you make about other agents.

## When you might legitimately act as a controller

Occasionally a task handed to you is itself a small fan-out of equally narrow, well-specified sub-legs (route these 40 tickets to the right queue, each independently) where dispatching several identical, narrow workers is genuinely cheaper and faster than doing all 40 yourself in sequence. That's the one shape where acting as a controller fits your tier:

- Every sub-leg must be independently well-specified — no leg should require judgment calls the brief doesn't already resolve. If any leg is ambiguous, that's a sign the overall task needed a stronger controller, not that you should resolve the ambiguity yourself mid-dispatch.
- Keep the fan-out flat. You are not the tier to run a multi-level coordinator hierarchy (triage → fix → verify, or workers reporting to a sub-coordinator) — that kind of structure needs judgment about escalation and reporting shape that belongs with a stronger model.
- Don't take on a review or verification role over another agent's substantive, ambiguous work — spot-checking a narrow, mechanical claim ("does this file exist," "does this number match") is fine; judging whether a design decision or a piece of reasoning holds up is not the fit for this tier.

Outside that shape, if you're asked to design a delegation plan, arbitrate between subagents, or judge whether a blocked report needs escalation, escalate the decision itself rather than making the call — say plainly that this is a judgment call better suited to a stronger model or a human, and hand back what you found.

**If you do dispatch a flat fan-out, the mechanics still apply even at this narrow scale — this tier doesn't get a lighter version of them:**

- **Never let two of your dispatched legs edit the same file.** Even 40 narrow tickets can collide if two land in the same file; check for overlap before dispatching, not after.
- **Scope each worker's permissions to what its leg actually needs** — a routing/classification leg doesn't need write access to anything it isn't updating.
- **Record a baseline right before dispatching** (e.g. `git rev-parse HEAD`, or a snapshot of the state each leg will modify) so you have something to diff against afterward.
- **A worker's "done" report is a claim, not evidence.** Spot-check a sample of the returned results against the actual state before rolling all 40 up into your own summary — the same rule this skill applies to any subagent's report applies to yours as a coordinator too.

If any of this feels like more structure than the task needs, that's a signal the fan-out wasn't as narrow as it looked — hand it to a stronger controller instead of skipping the checklist.

## As a worker: what a good brief looks like, and what to do if you don't get one

Since you'll usually be on the receiving end of a dispatch rather than the one sending it, the most useful thing this skill can do for you is describe what a well-formed brief looks like, so you can flag it when yours isn't one:

- **A good brief gives you the task + the interfaces it touches + constraints, explicitly.** If yours is missing one of those — if it says "fix this up" or "handle the routing" without saying which file, which criteria, or what's out of scope — don't fill the gap with your best guess and proceed as if it were resolved. Report back that the brief is underspecified and say exactly what's missing, rather than picking the loosest reading and calling the result done. Guessing generously on an ambiguous brief is a worse outcome at this tier than asking, because a wrong guess on an ambiguous case is exactly the kind of error a narrow, cheap worker is least equipped to catch in itself.
- **Do the narrow thing asked, and stop there.** Don't expand a well-specified extraction or classification task into an open-ended review of the surrounding code "while you're in there" — scope creep from a worker is as much a problem as scope creep from a coordinator, and it's harder for whoever dispatched you to catch since they weren't expecting it.
- **Report as a file when the output is long or structured**, and say plainly what you checked and what you didn't — "classified all 40 tickets; 3 were ambiguous between two categories, flagged separately" is a more useful report than a confident single pass over all 40.

## Common failures (from the worker's seat)

- Accepting a vague brief and filling the gap with a guess instead of flagging it.
- Expanding scope beyond what was actually asked because the surrounding context looked relevant.
- Reporting a narrow, low-confidence call as settled instead of flagging it as uncertain.
- Trying to act as a coordinator over genuinely ambiguous or judgment-heavy sub-work — that's a controller's job, not this tier's.

See `SKILL.md` for the optional hook and execution-state script that mechanize part of this discipline.
