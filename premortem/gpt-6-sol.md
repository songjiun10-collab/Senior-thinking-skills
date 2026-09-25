> Tuned for OpenAI GPT-6 Sol. See SKILL.md for the model index.

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

This is the workhorse tier for agentic and multi-step work — well suited to running a premortem as one step in a larger pipeline. Reasoning effort is tunable per call (none/low/medium/high/xhigh/max, default medium). For a routine premortem, medium is often enough; reserve high/xhigh for a piece with real blast radius (shared state, external contracts, persisted data) — a higher setting costs more without a guaranteed matching gain, so tune by result rather than defaulting to max.

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

## How would you notice a failure

Code that fails silently is far more dangerous than code that fails loudly.

- If this fails in production, **who** finds out, and **how**?
- Are you swallowing exceptions? (`except: pass`, an empty catch block)
- Does the error message actually help find the cause? Does it include **which value** was the problem?
- Is there a path that fails but looks like success? (partial success, an empty result returned as if complete)

## Working the list

When this skill runs as one leg of a longer agent pipeline, name the completion bar for the premortem step explicitly (which categories, defend-or-skip for each) so a mid-pipeline effort or tool-set change — now cheap, since it no longer breaks the prompt cache — doesn't quietly reset how thorough the pass is. If the premortem is being run as part of an autonomous flow with no human checking the output before it ships, keep an independent pass verifying the "defend" decisions actually got implemented — this tier is not the one to trust near a guardrail or safety-relevant judgment call without that check. With 1.05M context, a broad sweep across a whole subsystem is affordable in one pass; state that scope explicitly rather than assuming it.
