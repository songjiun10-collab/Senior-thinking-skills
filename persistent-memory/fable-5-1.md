> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

# Persistent Memory

Claude Code doesn't remember you between sessions, and a dispatched subagent doesn't remember anything at all — it starts from zero session history every time (see `delegate-to-subagents`). Some other agent platforms build in standing per-agent memory that quietly improves with correction; Claude Code doesn't have that layer. The honest substitute is the same one used for a recurring dispatch brief: write down what was learned, in a file, and load that file before repeating the task.

This isn't a workaround to feel bad about — an explicit file beats implicit memory for exactly the reasons `record-the-why` and `honest-artifacts` already argue: you can read it, diff it, prune it, and know exactly why a decision is still in effect, none of which is true of memory you can't inspect.

See `SKILL.md` for the `scripts/memory.py` CLI reference (`show` / `append` / `list`) — that mechanism doesn't change here. What follows is the judgment call: when to write, what to write, how much.

## When to make one

- The same kind of correction has come up more than once ("no, always use tabs here," "don't touch the generated files," "this client wants short replies")
- You're starting a task type you expect to repeat (a recurring review, a recurring report format, a recurring delegation brief)
- Don't make one for a correction you're confident won't recur — that's just noise to maintain

## Where it belongs

- **Project-wide and stable** (a convention every contributor should know) → `CLAUDE.md`, not a memory file. `CLAUDE.md` is read every session by design; a memory file isn't unless something loads it.
- **Narrower, more volatile, or still being refined** (this user's phrasing preference, a client's quirks, a not-yet-settled workflow) → a memory file, e.g. `.claude/memory/<topic>.md`. Cheap to create, cheap to throw away, doesn't compete for space in CLAUDE.md.
- Genuinely one-off → neither. Not everything needs to survive the session.

## What goes in it

- Distilled corrections, not transcript — the same "brief, not pasted history" principle as `delegate-to-subagents`'s "How to brief." A raw conversation log makes the next reader re-derive the lesson instead of just applying it.
- One line per correction, dated, in your own words — not the user's exact wording captured verbatim, which drifts out of context without the conversation around it.
- The current, still-true state — not a running log of everything that was ever said. Superseded corrections get replaced, not appended forever (see "Keeping it honest" below).
- When you `append`, say so in one line rather than doing it silently — you tend to write fewer user-facing updates between actions during a longer task, and a memory write is exactly the kind of side-effect someone watching would want surfaced, not buried in a quiet tool call.

## Keeping it honest

- **Review it periodically, don't just append.** A memory file that only grows is exactly the kind of unverified, never-re-checked artifact `honest-artifacts` warns about — a correction from six months ago may no longer apply.
- If two entries conflict, that's a signal the situation changed — resolve it, don't leave both standing.
- A memory file that hasn't been touched in a long time and no longer matches how the task is actually done is worse than no file — it actively misleads the next read. Delete it or update it; don't let it fossilize.

## Calibration notes

- Deciding what's durable enough to persist and what isn't is a judgment call best made from the goal ("keep only what will still be true and useful next time") rather than a rigid rule list — your own reasoning about a given correction's shelf life will generally get this right without a scripted decision tree.
