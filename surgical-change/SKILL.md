---
name: surgical-change
description: Keep every changed line traceable to the request. Use when editing existing code, especially code you didn't write; when tempted to clean up something you noticed while reading; when a diff is growing beyond the ask; or when deciding whether to delete code that looks dead.
---

# Surgical Change

Every line you change must connect directly to the request. The moment a reviewer asks "why did this change?", review cost multiplies.

## Don't

- Don't touch code, comments, or formatting outside the request's scope
- Don't "clean up while you're in there" just because something caught your eye — **requested refactoring is welcome, drive-by tidying is not**
- Don't refactor what isn't broken
- Match the existing style even when it's not what you'd choose

## Dead code

- Unrelated dead code: **mention it, don't delete it.** Whether it's really dead usually needs outside confirmation
- Clean up only the **orphans your own change created**

## Append the record, don't overwrite it

Old approaches, experiment history, docstring history — all have value as a baseline. Append, don't overwrite. Lose the record of why an approach wasn't taken, and the next person walks into the same dead end.

## When restructuring **is** the task

Module splits, file moves, README rewrites are welcome when that's what was asked. The rule above isn't banning that — it's banning **smuggling it into an unrelated change.**

## Before touching it: Chesterton's Fence

Before deleting or simplifying existing code, confirm **why it's written that way** first. See `chestertons-fence` for the full procedure — the core idea: don't break what you don't understand.

## Change size

Small changes review easier, merge faster, and ship safer.

| Size | Verdict |
|---|---|
| ~100 lines | Good. Reviewable in one pass |
| ~300 lines | Fine if it's one logical unit |
| ~1000 lines | Too big. Split it |

**Watch file size, not just diff size.** Even a small diff is a signal if it grows an already-large file further — ask whether to extract a helper or submodule first. Split first, then add.

**Separate refactoring from feature work.** Tidying existing code while adding new behavior is really two changes — ship them separately. Trivial cleanup like a rename can be left to reviewer discretion.

## Blast radius beyond this diff

- If the change touches a shared interface, config format, or library other teams depend on, "surgical" means bounded by **the interface**, not just this repo — audit external callers before merging, not after they file a bug.
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

**Lead with what matters.** Correctness and security first, structural regressions and missed simplifications next, everything else after. Don't bury one real problem under ten nitpicks — a single structural issue **is** the review.

## Don't accept "I'll clean it up later"

In practice, deferred cleanup mostly never happens. Either require it in this change, or if it's genuinely urgent, file a separate issue **with an owner assigned to it.**
