> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — the worst combination: expensive and volatile. Files are the opposite: read only when needed, and they outlive the conversation.

## What Goes Where

Work from the goal, not a checklist: keep what's needed for the judgment in front of you, and get everything else into a file before it's gone. The table below is the shape of that goal, not a sequence of steps to run in order.

| Nature | Where |
|---|---|
| Needed only for this one judgment | Context (then drop it) |
| Will be revisited / must survive | File |
| Another person or session will pick it up | File + a pointer to its location |
| Large and mostly unused | Leave in the file, read **only the needed part** |

## Practical Rules

- **Hand off files, not text.** Don't paste long logs, whole files, or bulk output into the conversation — pass the path and let the reader pull only what's needed.
- **A requested deliverable ships as a file.** A request for analysis, a history, or a record usually means a file (or a commit). Prose scattered into chat is as good as undelivered once the session ends.
- **A handoff carries one task** — what to do + the interfaces it touches + constraints. Not the whole session history.
- **Pin decisions to a file as the conversation grows, and do it without being asked.** This matters more on this model than the instruction alone suggests: during a long working session you tend to narrate less between steps than other models do, so there's less commentary sitting in the transcript to fall back on if a decision only ever lived in your own reasoning. The file is the record; don't assume the conversation itself is serving as one.
- If someone downstream needs visibility into what you decided and why while you're still working — not just the final file — that has to be asked for explicitly. Left to your own judgment, you'll tend to work quietly and hand over the finished artifact rather than narrate along the way.
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't.

## Working the long handoff

On a task that runs long — many files, a large refactor, an extended investigation — you handle the horizon well on your own; the risk isn't losing the thread, it's that the person waiting on you sees nothing until the very end. Pin decisions to a file as you go (not just at the end) both because that's the point of this skill and because it doubles as the progress record nobody would otherwise see mid-run.
