> Tuned for Claude Sonnet 5.5. Source: Anthropic prompting guide (prompting-claude-sonnet-5-5). See SKILL.md for the model index.

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

## Keeping it honest

- **Review it periodically, don't just append.** A memory file that only grows is exactly the kind of unverified, never-re-checked artifact `honest-artifacts` warns about — a correction from six months ago may no longer apply.
- If two entries conflict, that's a signal the situation changed — resolve it, don't leave both standing.
- A memory file that hasn't been touched in a long time and no longer matches how the task is actually done is worse than no file — it actively misleads the next read. Delete it or update it; don't let it fossilize.

## Calibration notes

- The trigger conditions above ("the same correction has come up more than once," "starting a task type you expect to repeat") are the actual criteria — apply them as written rather than waiting for an explicit "remember this for next time." An underspecified moment (a correction given once, without being told to persist it) still counts if it matches the pattern; don't read the absence of an explicit instruction as permission to skip writing it down.

## Calibration (Anthropic official prompting guide, Sonnet 5.5)

- **Effort**: default is `high` on the Claude API. Levels are recalibrated from Sonnet 5, so re-run an effort sweep rather than carrying over the old setting. Start at `medium` for agentic coding and well-specified multistep tool use; `medium` or `low` for chat.
- **Low effort skips verification and stops early**: at `low`, the model may skip checks and, at `low`/`medium` on long agentic tasks, check in before finishing. Add an explicit "keep working until done, stop only before a risky step" line rather than assuming it will carry work through.
- **Thinking off**: send `thinking: {type: "between_tools"}` at `high` effort or below. `{type: "disabled"}` is a 400. Per-message effort changes need adaptive thinking.
- **Structured JSON on multistep reasoning**: prefer structured outputs; otherwise ask the model to think first and parse the last JSON value, treating `stop_reason: "max_tokens"` as failure.
- **Progress visibility**: set `display: "updates"` to surface between-tool-call notes.
- **Search**: tell it to check specifics that may have changed (what is allowed, required, or charged), even when confident.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn. Keep harness reminders in a separate system message, so the model doesn't mistake real user input for injection.
- **Verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Safeguard refusals**: categories `cyber`, `bio`, `frontier_llm`, `reasoning_extraction`, `general_harms`. Remove prompt instructions that ask it to reproduce its reasoning in the reply.
