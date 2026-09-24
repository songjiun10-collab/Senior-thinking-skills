> Tuned for Claude Fable 5.1. See SKILL.md for the model index.

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

**Ask explicitly for narration during a long review.** This model writes noticeably fewer user-facing updates between tool calls by default, which is easy to mistake for stalling during a review that walks a large diff surface by surface. A security review specifically benefits from visible reasoning — which endpoint is being checked, what payload is being tried, why a given path was ruled safe — both so the reviewer can be followed in real time and so the trail itself is auditable. If that visibility matters, ask for it up front rather than assuming it'll appear on its own; this model handles the long autonomous review itself well, it just narrates less unless asked.

## Warning signs

| Thought | Reality |
|---|---|
| "Tests pass, so it's fine" | Tests pass because nobody tried to break in |
| "It's an internal endpoint" | Internal becomes public; the check is cheap now |
| "I'll sanitize the input later" | "Later" is the vulnerability |
| "The framework handles it" | Only if you didn't bypass it |
