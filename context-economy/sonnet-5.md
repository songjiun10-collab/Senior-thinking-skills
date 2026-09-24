> Tuned for Claude Sonnet 5. See SKILL.md for the model index.

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — the worst combination: expensive and volatile. Files are the opposite: read only when needed, and they outlive the conversation.

You track your own remaining budget as you go — use that. When you can see the window filling up, that's the signal to pin decisions to a file now rather than waiting for a natural stopping point that might arrive too late.

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
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't. Be explicit about the path and what's at it — a vague pointer ("see the file from earlier") gets followed literally too, and "the file from earlier" isn't a reliable pointer if there were several.
