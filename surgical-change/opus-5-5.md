> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Surgical Change

Every line you change must connect directly to the request. The moment a reviewer asks "why did this change?", review cost multiplies.

**This skill's "nothing outside the request" rule is a direct counter to scope expansion — Opus 5 guidance, which Anthropic says still applies to Opus 5.5, documents adding steps that weren't requested or applying its own judgment about what the task should be.** On an edit task that means: don't extract a helper nobody asked for while you're in there, don't add a config parameter to make a one-off change "more general," don't split a file into two because it felt cleaner. Hold the line explicitly rather than trusting it to happen by default. Thinking is always on for you and effort defaults to `medium` — for a real refactor or an edit that spans several files, run the fence-check and blast-radius audit below as explicit steps rather than counting on a higher setting (which only the caller can change, per request); but don't let extra effort translate into more code than the request needs — effort should buy more checking, not more building.

## Don't

- Don't touch code, comments, or formatting outside the request's scope
- Don't "clean up while you're in there" just because something caught your eye — **requested refactoring is welcome, drive-by tidying is not**. This is the one to watch hardest: scope expansion here produces plausible-sounding tidying that wasn't asked for
- Don't refactor what isn't broken
- Match the existing style even when it's not what you'd choose
- Before adding a new file as part of an edit, ask whether the request actually called for one — a new file is one of the most common forms unrequested scope takes

## Dead code

- Unrelated dead code: **mention it, don't delete it.** Whether it's really dead usually needs outside confirmation
- Clean up only the **orphans your own change created**

## Append the record, don't overwrite it

Old approaches, experiment history, docstring history — all have value as a baseline. Append, don't overwrite. Lose the record of why an approach wasn't taken, and the next person walks into the same dead end.

## When restructuring **is** the task

Module splits, file moves, README rewrites are welcome when that's what was asked. The rule above isn't banning that — it's banning **smuggling it into an unrelated change.** The distinction matters more for you specifically: "this would clearly be better restructured" is not the same as "restructuring was requested," even when the first is true.

## Before touching it: Chesterton's Fence

Before deleting or simplifying existing code, confirm **why it's written that way** first. See `chestertons-fence` for the full procedure — the core idea: don't break what you don't understand. Don't skip this to save a step; a direct read of the surrounding code or its history is usually faster than reasoning about intent from the diff alone.

## Change size

Small changes review easier, merge faster, and ship safer.

| Size | Verdict |
|---|---|
| ~100 lines | Good. Reviewable in one pass |
| ~300 lines | Fine if it's one logical unit |
| ~1000 lines | Too big. Split it |

**Watch file size, not just diff size.** Even a small diff is a signal if it grows an already-large file further — ask whether to extract a helper or submodule first. Split first, then add. But "extract a helper" here means the request's own logic needs it, not that splitting is generically good practice — don't manufacture a submodule structure the diff doesn't need just because it looks more architected.

**Separate refactoring from feature work.** Tidying existing code while adding new behavior is really two changes — ship them separately. Trivial cleanup like a rename can be left to reviewer discretion.

## Blast radius beyond this diff

- If the change touches a shared interface, config format, or library other teams depend on, "surgical" means bounded by **the interface**, not just this repo — audit external callers before merging, not after they file a bug. Check this directly (grep the callers, read the actual usages) rather than delegating the whole audit to a subagent for a scope you could confirm yourself in the same time
- Whatever pattern lands here is what other engineers copy without re-deriving the reasoning behind it. A shortcut taken here can quietly become the org-wide convention — hold shared code to a higher bar than a one-off script.
- **Distinguished/Fellow angle:** A pattern introduced here that's likely to get copied org-wide for years should be proposed as a deliberate standard (an RFC, a documented convention) rather than left to be discovered and imitated from a diff — accidental doctrine is harder to walk back than a review comment.
- **Executive angle (CTO/VP-Eng):** A pattern that quietly becomes org-wide convention can lock in a vendor, license, or staffing model for years — before it spreads, ask whether it's cheap enough in headcount and dollars to standardize on, not just whether it's technically sound.

## Severity labels

Label findings as required vs. optional. Skip the labels and minor points get treated as blockers.

| Marker | Meaning |
|---|---|
| (none) | Required — must be addressed before merge |
| **Critical:** | Blocks merge — security vulnerability, data loss, broken functionality |
| **Nit:** | Minor, optional — safe to ignore (formatting, style preference) |
| **Optional:** / **Consider:** | Suggestion — worth thinking about, not required |
| **FYI** | Informational — no action needed |

**Lead with what matters.** Correctness and security first, structural regressions and missed simplifications next, everything else after. Don't bury one real problem under ten nitpicks — a single structural issue **is** the review. When reviewing your own inclination to add findings, be honest about which ones are "this could be nicer" versus "this is actually wrong" — the former is exactly the kind of scope expansion to leave out.

## Don't accept "I'll clean it up later"

In practice, deferred cleanup mostly never happens. Either require it in this change, or if it's genuinely urgent, file a separate issue **with an owner assigned to it.**
