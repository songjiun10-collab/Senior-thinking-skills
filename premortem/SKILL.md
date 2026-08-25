---
name: premortem
description: Map the failure scenarios before writing the happy path. Use before implementing any feature that touches I/O, user input, external services, concurrency, or persisted state. Also use when adding error handling, when a bug report suggests an unhandled edge case, or when reviewing whether a design is production-ready. Covers both "what breaks" and "how would we even find out".
---

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

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
