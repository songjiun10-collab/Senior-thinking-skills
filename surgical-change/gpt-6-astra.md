> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Surgical Change

Every line you change must connect directly to the request. The moment a reviewer asks "why did this change?", review cost multiplies.

You're documented to be more tentative than prior models about declaring a task complete, and to ask clarifying questions more often than your predecessors — on an edit task, state the scope up front (which files, which function, where the change stops) so that instinct resolves as "confirm the boundary once, then finish," not as ongoing uncertainty that gets filled in by touching more than was asked. You're also documented to verify and test your own changes without being told to, so drop any leftover "you must test this before finishing" instruction from an older prompt — it's redundant on you and just adds noise. One more thing worth naming: you delegate to subagents less than expected by default. Where this skill's blast-radius audit or a Chesterton's-Fence investigation genuinely benefits from a separate look (grepping every caller of a shared interface, reading the git history behind a suspicious block), say explicitly that a subagent should do it and how much — don't quietly fold it into your own pass just because that's your default.

## Don't

- Don't touch code, comments, or formatting outside the request's scope
- Don't "clean up while you're in there" just because something caught your eye — **requested refactoring is welcome, drive-by tidying is not**
- Don't refactor what isn't broken
- Match the existing style even when it's not what you'd choose

Read the request's scope literally rather than generously — if it names one function or one bug, that's the boundary, not an invitation to also fix the file's broader style.

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

- If the change touches a shared interface, config format, or library other teams depend on, "surgical" means bounded by **the interface**, not just this repo — audit external callers before merging, not after they file a bug. This is a case where explicitly delegating the caller audit to a subagent (or running it yourself as a distinct, named step) is worth doing rather than skipping for scope
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

**Lead with what matters.** Correctness and security first, structural regressions and missed simplifications next, everything else after. Don't bury one real problem under ten nitpicks — a single structural issue **is** the review. Prefer plain, direct statements of the finding over hedged or padded phrasing — say what's wrong and why, skip filler like "it's worth noting" or "you may want to consider."

## Don't accept "I'll clean it up later"

In practice, deferred cleanup mostly never happens. Either require it in this change, or if it's genuinely urgent, file a separate issue **with an owner assigned to it.**
