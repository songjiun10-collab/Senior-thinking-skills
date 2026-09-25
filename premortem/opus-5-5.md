> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

Thinking is always on for this model, but **effort is the only depth control, and the default is `medium`.** A premortem on I/O, concurrency, or persisted state needs more than the default gives it — set effort explicitly before running this skill on anything nontrivial. Don't rely on thinking being "on" to substitute for that.

## Where it breaks

- Input empty, null, or 100x larger than expected?
- Network, file, or external API fails — or responds **slowly**? (a timeout is harder to handle than an outright failure)
- The same code runs twice concurrently? A duplicate request arrives?
- The process dies mid-operation — does data end up **half-written**?
- Encoding, timezone, floating point — anything that drifts silently?
- Principal angle: if this fails, does the blast radius stay inside this codebase, or does it corrupt shared state, a downstream team's data, or a contract another service depends on? Scope the premortem to the actual blast radius, not just the local function.
- Distinguished/Fellow angle: for a foundational piece, run the premortem against company-wide scale two or three years out, not next quarter's traffic — a failure mode that's rare today becomes routine once every team is running on it.
- Executive angle (CTO/VP-Eng): does the failure mode carry regulatory exposure, customer-trust damage, or competitive fallout beyond an engineering incident — the kind of risk a board or investor would ask about — and does containing it require more on-call headcount than you currently have?

You don't have to answer every question. Pick the ones that actually apply to this piece of work, and decide whether to defend against each or deliberately skip it. **If you skip one, say so in writing.**

Left unconstrained, this model tends to over-engineer the response to a premortem — adding defensive layers, config knobs, or abstractions nobody asked for. Match the fix to the actual failure mode identified, not to every failure mode that's theoretically possible. If brevity matters, say so — response length doesn't shrink much just from lowering effort.

## How would you notice a failure

Code that fails silently is far more dangerous than code that fails loudly.

- If this fails in production, **who** finds out, and **how**?
- Are you swallowing exceptions? (`except: pass`, an empty catch block)
- Does the error message actually help find the cause? Does it include **which value** was the problem?
- Is there a path that fails but looks like success? (partial success, an empty result returned as if complete)

## Working the list

This model already self-verifies well — once you've walked the failure list, don't pile on a second "double-check this list" pass; that's wasted tokens and latency without turning up more real findings. Spend the effort on actually working through the failure categories thoroughly the first time, not on re-verifying afterward.

If the premortem surfaces work worth investigating separately (e.g., "check whether the existing retry logic actually handles this"), don't reflexively spin up a subagent for it — a direct grep or file read is often faster than a delegation round-trip. Reserve delegation for genuinely separable, larger investigations.
