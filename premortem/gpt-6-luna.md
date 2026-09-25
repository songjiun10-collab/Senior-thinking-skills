> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

This tier is built for high-volume, narrow, well-specified work — a premortem on a small, bounded piece (one endpoint, one function, one config change) is a good fit. A premortem on a large or ambiguous surface (a whole subsystem, a foundational piece with company-wide blast radius) is Structural, judgment-heavy work this tier isn't the right fit for — escalate that one to a stronger tier rather than running it here at high effort and hoping the extra effort closes the gap; effort past a certain point doesn't reliably buy a better list on this model family.

## Where it breaks

- Input empty, null, or 100x larger than expected?
- Network, file, or external API fails — or responds **slowly**? (a timeout is harder to handle than an outright failure)
- The same code runs twice concurrently? A duplicate request arrives?
- The process dies mid-operation — does data end up **half-written**?
- Encoding, timezone, floating point — anything that drifts silently?
- Principal angle: if this fails, does the blast radius stay inside this codebase, or does it corrupt shared state, a downstream team's data, or a contract another service depends on? Scope the premortem to the actual blast radius, not just the local function.
- Distinguished/Fellow angle: for a foundational piece, run the premortem against company-wide scale two or three years out, not next quarter's traffic — a failure mode that's rare today becomes routine once every team is running on it.
- Executive angle (CTO/VP-Eng): does the failure mode carry regulatory exposure, customer-trust damage, or competitive fallout beyond an engineering incident — the kind of risk a board or investor would ask about — and does containing it require more on-call headcount than you currently have?

For a bounded piece of work, pick the categories from the list above that actually apply — usually a small, obvious subset — and decide whether to defend against each or deliberately skip it. **If you skip one, say so in writing.** If the surface is large enough that most of the list plausibly applies, that's itself a signal this task has outgrown a narrow pass.

## How would you notice a failure

Code that fails silently is far more dangerous than code that fails loudly.

- If this fails in production, **who** finds out, and **how**?
- Are you swallowing exceptions? (`except: pass`, an empty catch block)
- Does the error message actually help find the cause? Does it include **which value** was the problem?
- Is there a path that fails but looks like success? (partial success, an empty result returned as if complete)

## Working the list

Keep each check concrete and checkable — for a narrow, well-specified leg, that's this tier's strength. State completion criteria explicitly (which categories checked, a defend-or-skip line for each) since a short prompt here tends to get read narrowly. Effort level is tunable (none through max) and can be toggled off for latency; a routine premortem on a small piece rarely needs more than low or medium — save higher effort for the rare bounded task with real edge-case density, and hand anything ambiguous or wide in scope to a stronger tier rather than pushing this one past what it's suited for.
