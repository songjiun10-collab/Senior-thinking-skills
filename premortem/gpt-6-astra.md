> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Premortem

Ask **"when does this break"** before asking "does this work." Do it after the fact and defensive code gets bolted on piecemeal; do it up front and the structure itself changes.

State completion criteria for the premortem up front: what counts as "done" is walking the categories that actually apply and writing a decision (defend or skip) for each, not just producing a plausible-looking list and stopping. Also state the exploration scope — which parts of the system the premortem covers and where it stops — since this model tends to under-delegate and under-scope on its own rather than asking to expand it.

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

## Acting on the list

You test and verify automatically once you've made a change — that part doesn't need a reminder here. What needs stating explicitly is scope and stopping point: work through the failure categories that apply, write your defend-or-skip call for each, and treat that as done — don't pause partway to ask whether you should keep going. If a failure mode surfaces work worth checking (an existing retry path, a similar handler elsewhere), go check it directly before reporting back, rather than flagging it as a question. Trust your own judgment on which categories are relevant; you don't need permission to widen the sweep across a large diff or subsystem when the blast radius calls for it — with 1.05M context there's room to do that in one pass.

Keep the writeup itself plain: state the failure mode and the decision, skip hedging language and skip framing anything as "X, not Y" — just say what you're defending against and what you're deliberately leaving alone.
