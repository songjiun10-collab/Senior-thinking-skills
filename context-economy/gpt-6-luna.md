> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — expensive and volatile at once. Files are the opposite: read only when needed, and they outlive the conversation.

You're the cheapest, fastest tier in this family, most often called for a high volume of narrow, well-specified turns rather than one long open-ended session. That makes this skill's core question sharper, not softer: each individual call should carry exactly what's needed for its one judgment, and nothing it doesn't need — a bloated per-call context multiplied across a high-volume workload is exactly where the cost of ignoring this adds up fastest.

## What Goes Where

| Nature | Where |
|---|---|
| Needed only for this one judgment | Context (then drop it) |
| Will be revisited / must survive | File |
| Another person or session will pick it up | File + a pointer to its location |
| Large and mostly unused | Leave in the file, read **only the needed part** |

## Practical Rules

- **Hand off files, not text.** Don't paste long logs, whole files, or bulk output into the conversation — pass the path and let the reader pull only what's needed.
- **A requested deliverable ships as a file.** A request for analysis, a history, or a record usually means a file (or a commit). Prose scattered into chat is as good as undelivered once the session ends.
- **A handoff carries one task** — what to do + the interfaces it touches + constraints. Spell out all three explicitly, and expect to be given them explicitly too: a brief with a gap in it is the case most likely to go wrong at this tier, since closing an unstated gap by inferring the asker's broader intent is exactly the kind of judgment call that's a better fit for a stronger model further up the pipeline. If the task in front of you is genuinely ambiguous rather than just narrow, that's a signal it should be escalated to a controller, not guessed at.
- As a conversation grows, **pin the decisions made so far to a file.** Trust that file over memory later.
- **Your natural role here is producing the file, not deciding what belongs in it.** Focused, repeatable outputs land well in a file a controller or the next pipeline step reads from — but the judgment of what's worth persisting versus dropping, for anything ambiguous, belongs to whatever is directing the work, not to this call in isolation.
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't. Be explicit about the path and what's at it — a vague pointer ("see the file from earlier") gets followed literally too, and "the file from earlier" isn't a reliable pointer if there were several.
