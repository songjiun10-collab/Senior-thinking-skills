> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — expensive and volatile at once. Files are the opposite: read only when needed, and they outlive the conversation.

The 1.05M-token window makes it tempting to just keep pasting — there's room. Resist that. Room in the window isn't free: everything sitting in context still competes for attention on every turn, and it's still gone when the session ends. A large window is not a reason to relax this discipline; if anything it's a reason a bloated context goes unnoticed for longer before it causes a miss. One concrete cost changed for the better this generation: switching reasoning effort or tool set mid-conversation no longer invalidates the prompt cache the way it used to — that makes it cheaper to adjust effort as a task develops, but it doesn't change the underlying rule about what belongs in context versus in a file.

## What Goes Where

| Nature | Where |
|---|---|
| Needed only for this one judgment | Context (then drop it) |
| Will be revisited / must survive | File |
| Another person or session will pick it up | File + a pointer to its location |
| Large and mostly unused | Leave in the file, read **only the needed part** |

## Practical Rules

- **Hand off files, not text.** Don't paste long logs, whole files, or bulk output into the conversation — pass the path and let the reader pull only what's needed.
- **A requested deliverable ships as a file.** A request for analysis, a history, or a record usually means a file (or a commit). Prose left in chat is as good as undelivered once the session ends.
- **State completion criteria and scope for the handoff task up front, not just the task itself.** What to do + the interfaces it touches + constraints, plus what "done" looks like and where the work should stop. Spell out all of it explicitly — an underspecified handoff doesn't get generously filled in by whoever reads it next; it gets followed exactly as literally written, gaps and all, so close the gaps yourself before writing it, not after.
- As a conversation grows, **pin the decisions made so far to a file.** Trust that file over memory later — use your own sense of the remaining budget to decide when, rather than waiting to be asked.
- **Default to doing this, not asking whether to.** Whether to write the handoff file now or later is your call to make from the state of the task, not a question to put back to the user — infer intent from context and act, then say what you did.
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't. Be explicit about the path and what's at it — a vague pointer ("see the file from earlier") gets followed literally too, and "the file from earlier" isn't a reliable pointer if there were several.

## Writing the handoff itself

A handoff note is a deliverable, so hold it to the same bar as any other piece of writing: clear, concise, active voice. Skip a bulleted list unless the items are genuinely parallel, sequential, or worth comparing side by side — a wall of loosely-related bullets is harder to act on than two direct sentences. Say the constraint or the decision directly rather than through a contrastive frame ("write the interface as X" beats "not Y, but X"), and skip filler like "it's worth noting" or "leverage" — say the thing itself.
