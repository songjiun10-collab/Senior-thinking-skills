> Tuned for Claude Sonnet 5.5. Source: Anthropic prompting guide (prompting-claude-sonnet-5-5). See SKILL.md for the model index.

# Security Review

`threat-and-scale-check` designs the trust boundary before code exists; this skill reviews the code that touches it, before it ships. Security defects aren't ordinary bugs — they're invisible in tests (the suite passes precisely because nobody tried to break in), cheap to exploit, and expensive to clean up after.

## Trigger

The review is mandatory when the diff touches any of these — not because the paths are magic, but because this is where user-controlled input meets privileged execution:

| Surface | Examples |
|---|---|
| Auth / session | login flows, session handling, token issuance and validation |
| Input → execution | query params, form data, file uploads, shell/template interpolation |
| APIs | new endpoints, changed authorization checks, CORS |
| Database | raw queries, migrations touching permissions or PII |
| Credentials | anything reading or writing keys, tokens, connection strings |

## The checklist

Walk the diff against the recurring failure classes (OWASP Top 10, condensed to the ones code review can actually catch):

- **Injection** — user input reaching a query, shell command, template, or path? Parameterized statements; no string-built commands
- **Broken auth** — passwords hashed (bcrypt/argon2, not MD5/SHA1); sessions and tokens signed, validated, expiring; rate limiting on auth endpoints
- **Broken access control** — every new endpoint checks authorization server-side, not just the UI hiding the button; object-level checks (can this user read THIS record?), not just role-level
- **Secrets** — no hardcoded keys, tokens, or connection strings; no secrets in logs, error messages, or responses
- **Data exposure** — sensitive data encrypted in transit and at rest; error responses don't leak stack traces or internals
- **Supply chain** — new dependencies checked for known CVEs and maintenance status, not added on trust

- **Principal angle:** an auth or input-handling pattern ships to other teams the moment it merges — a weak default (an unparameterized query helper, a missing object-level check) gets copied everywhere it's imported. The review is precedent-setting, not just this diff.
- **Distinguished/Fellow angle:** would this survive a review from someone joining in five years, or an external audit? A pattern that depends on "nobody notices the endpoint" is a liability with a public incident attached, at company scale.
- **Executive angle (CTO/VP-Eng):** a breach's cost line — regulatory, customer-trust, incident response — dwarfs review time. The review is a risk-continuity decision worth standardizing as a merge gate, not a courtesy pass.

## Verify, don't recite

- Reading the diff isn't enough — **run the exploit path** where feasible (the injection payload, the unauthorized request), the same evidence bar as `verify-before-claiming`
- Automated scanners (SAST, dependency CVE checks) complement, not replace — they catch known patterns; the review catches the ones specific to this codebase

This model follows instructions more literally than the prior generation, so if the full checklist applies — not just "check for injection" — name the categories that matter for this diff explicitly (auth, access control, secrets, etc.) rather than assuming a short prompt will expand into the full OWASP walk on its own. With 1M context, a large diff plus its full surrounding call graph can be reviewed in one pass rather than file by file — useful for tracing an object-level access-control gap across many endpoints at once.

## Warning signs

| Thought | Reality |
|---|---|
| "Tests pass, so it's fine" | Tests pass because nobody tried to break in |
| "It's an internal endpoint" | Internal becomes public; the check is cheap now |
| "I'll sanitize the input later" | "Later" is the vulnerability |
| "The framework handles it" | Only if you didn't bypass it |

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
