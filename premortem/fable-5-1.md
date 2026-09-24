> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

Treat the failure categories below as the goal and boundaries of the premortem, not a checklist to fill in a fixed order. This model's own reasoning about failure modes tends to cover more ground, and find less obvious ones, than a prescriptive script would — state what the premortem needs to cover and let it work the problem.

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

This model writes fewer running updates by default during a long agentic pass. If a thorough premortem is going to take a while — walking multiple subsystems, cross-referencing failure modes against a large codebase — ask explicitly for visibility into progress as it goes, otherwise expect a quiet stretch followed by the finished list.

## How would you notice a failure

Code that fails silently is far more dangerous than code that fails loudly.

- If this fails in production, **who** finds out, and **how**?
- Are you swallowing exceptions? (`except: pass`, an empty catch block)
- Does the error message actually help find the cause? Does it include **which value** was the problem?
- Is there a path that fails but looks like success? (partial success, an empty result returned as if complete)
