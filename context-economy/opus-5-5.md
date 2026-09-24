> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

# Context Economy

**Optimize the context window; persist everything else.**

Anything pasted into the conversation occupies space for the rest of the session and vanishes when the session ends — the worst combination: expensive and volatile. Files are the opposite: read only when needed, and they outlive the conversation.

A 1M-token window makes it tempting to just keep pasting — there's "room." Resist that. Room in the window isn't free: everything sitting in context still competes for attention on every turn, and it's still gone when the session ends. The window being large is not a reason to relax this discipline; if anything it's a reason a bloated context goes unnoticed for longer before it causes a miss.

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
- **A handoff carries one task** — what to do + the interfaces it touches + constraints. Not the whole session history. Write that handoff plainly and keep it that size — there's a real pull, absent an explicit constraint, toward wrapping it in extra structure (a summary doc, an index file, a template nobody asked for) on top of the pointer that was actually needed. The discipline here is restraint, not elaboration.
- As a conversation grows, **pin the decisions made so far to a file.** Trust that file over memory later.
- **Principal-level angle:** a spec or interface note other teams will build against is leverage for them, not just a record for you — losing it to compaction or session end breaks their ability to work independently, not just yours.
- **Distinguished/Fellow-level angle:** if the doc is on track to become the company-wide reference people cite for years, write it so it survives without you in the room — one that only makes sense with your unwritten context is a bus-factor-of-one liability, no matter whose name is on it.
- **Executive angle (CTO/VP-Eng):** if losing this record means re-deriving it costs weeks of engineer time or blocks an audit, its survival is a budget and risk-continuity decision — worth a real knowledge-management process, not just trusting one person's habit of writing things down.

## Pointers, Not Summaries

Instead of filling context with "this file has A, B, C," leave **where to look**. Summaries go stale; sources don't. A summary is also exactly the kind of extra artifact that's tempting to produce "to be thorough" — a pointer is the plainer, correct answer; don't build a summary layer on top of it unless someone actually asked for one.

## Judgment calls specific to this model

- **Set effort explicitly when a handoff decision is non-trivial.** Effort — not thinking toggle — is the depth control here, and its default (`medium`) is one notch below what you'd get by default on the prior generation. Deciding what's safe to drop versus what must survive to a file is exactly the kind of judgment call worth spending real effort on; don't let it run at default depth by accident.
- **Brevity in a handoff note doesn't come for free.** Response length doesn't shrink much just from lowering effort — if the handoff needs to be terse (a one-line pointer, not a paragraph), say so explicitly rather than assuming a short deliverable follows naturally.
- **Trust your own self-check on "did I actually drop what I said I'd drop."** This model already verifies its own work well; there's no need to add a second explicit "double-check you didn't leave the whole log pasted in" pass on top of the rules above — that's wasted tokens, not more reliability.
