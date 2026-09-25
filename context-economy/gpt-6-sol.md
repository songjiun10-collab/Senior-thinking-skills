> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — expensive and volatile at once. Files are the opposite: read only when needed, and they outlive the conversation.

The 1.05M-token window makes it tempting to just keep pasting — there's room. Resist that. Room in the window isn't free: everything sitting in context still competes for attention on every turn, and it's still gone when the session ends. Changing reasoning effort or tool set mid-conversation no longer invalidates the prompt cache, so adjusting effort as a task develops is cheap now — but that's a cost change, not a reason to keep more in context than the current judgment needs.

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
- **A handoff carries one task** — what to do + the interfaces it touches + constraints. Spell out all three explicitly. An underspecified handoff doesn't get generously filled in by whoever reads it next (agent or person) — expect it to be followed exactly as literally written, gaps and all, so the gaps have to be closed by you, up front, not left implicit and hoped-for.
- As a conversation grows, **pin the decisions made so far to a file.** Trust that file over memory later — and don't wait to be told; use your own sense of the remaining budget to decide when.
- You're the tier most likely to be run as the workhorse in an agent pipeline — many short turns, each reading and writing files rather than carrying everything forward in one long conversation. Make each handoff file self-contained enough that the next step in the pipeline doesn't need anything from earlier turns that wasn't written down.
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't. Be explicit about the path and what's at it — a vague pointer ("see the file from earlier") gets followed literally too, and "the file from earlier" isn't a reliable pointer if there were several.

## Reasoning effort isn't free, tune it

Don't assume the highest reasoning effort (default `medium`; `none` through `max` available) is always better — measure it on your own tasks. That's a separate knob from context economy, but the two interact: don't compensate for an under-specified handoff by cranking effort up on the receiving end and hoping it reasons its way to the missing information. Write the handoff completely; tune effort empirically for the task, not as a substitute for a clear brief.
