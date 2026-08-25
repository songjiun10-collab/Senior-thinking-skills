---
name: context-economy
description: Decide what information goes where — in context, in a file, or dropped. Use when handing work off (to another session, agent, or person), when a task involves large files or long outputs, when writing a plan or spec that must outlive the conversation, or when the conversation is getting long enough that earlier details are at risk. Also use when deciding whether an answer should be chat text or a durable artifact.
---

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — the worst combination: expensive and volatile. Files are the opposite: read only when needed, and they outlive the conversation.

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
- **A handoff carries one task** — what to do + the interfaces it touches + constraints. Not the whole session history.
- As a conversation grows, **pin the decisions made so far to a file.** Trust that file over memory later.
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't.
