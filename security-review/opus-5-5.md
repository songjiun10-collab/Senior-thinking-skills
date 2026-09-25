> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

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

Opus 5 guidance (carried over to 5.5) says the model verifies its own work unprompted — once a finding is confirmed by actually running the exploit path, a second "are you sure this is really exploitable" pass on top just burns latency without turning up anything new. Put the saved budget into running more exploit paths, not re-checking the ones already confirmed. Set effort explicitly for a real review, too: thinking is always on, but effort is the actual depth control and defaults to `medium` — a full OWASP walk against a nontrivial diff needs more than default.

**A refusal mid-review is not automatically a finding.** This model runs safety classifiers for biology, cybersecurity, and reasoning extraction (finding vulnerabilities in source code is explicitly allowed; high-risk dual-use cyber activity is not), and a legitimate security review — writing an injection payload to prove exploitability, describing an attack path in a writeup — can trip a false positive. If a refusal shows up while doing exactly the exploit-path verification this skill calls for, treat it as a possible classifier false positive worth a second attempt (e.g. rephrasing, or narrowing to a smaller reproduction) before concluding the underlying code is actually unsafe.

## Warning signs

| Thought | Reality |
|---|---|
| "Tests pass, so it's fine" | Tests pass because nobody tried to break in |
| "It's an internal endpoint" | Internal becomes public; the check is cheap now |
| "I'll sanitize the input later" | "Later" is the vulnerability |
| "The framework handles it" | Only if you didn't bypass it |
