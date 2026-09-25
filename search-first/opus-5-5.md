> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Search First

Assume API knowledge from training data is **stale.** Libraries change signatures, flags disappear, recommended patterns flip. Code pulled from memory is the hardest kind of wrong, because it looks plausible.

## When to Always Verify

- Writing code that calls an external library, SDK, or API
- Using a CLI flag, a config file format, or an environment variable name
- Behavior tied to a version number ("since 3.11," "in v5")
- You think "this should work" but have **never actually verified it**
- An error message doesn't match the docs — usually your memory is stale, not the docs

## Verification Order

1. **Official docs and release notes** — the primary source. Blog posts and Stack Overflow come after.
2. **The actually installed version** — check `package.json`, `requirements.txt`, the lockfile. The latest docs are useless if they don't match the version in use.
3. **Existing usage in the codebase** — if the same library is already used here, that pattern is the answer for this project.
4. **Run it for real if needed** — one REPL line is cheaper than ten lines of guessing.

Do steps 2-4 directly rather than reaching for a subagent — a grep of the lockfile or a quick fetch of the release notes is faster inline than a delegation round-trip. This model delegates more eagerly than earlier ones by default, including for checks that a direct read settles immediately; reserve dispatch for genuinely large or parallel verification sweeps (e.g. auditing a dozen dependencies at once), not a single flag lookup.

## Cost Sense

Verify when the cost of checking is **cheaper than the cost of being wrong** — usually it is, by a lot. Conversely, re-checking a stable API on a well-known standard library every single time is waste.

Thinking is always on for this model, but effort is the actual depth control, and it defaults to `medium`. For anything beyond a well-known, stable API, set effort explicitly — at default effort a verification pass can come out shallow (surface-checking the doc title without confirming the signature actually matches the installed version). This model also already self-verifies its findings well once it's gathered them; don't add a redundant "are you sure the docs say that" re-check on top — that's wasted latency, not a stronger answer.

- **Principal-level angle:** if the library or version choice becomes a dependency other teams or services will inherit (a shared build, a common base image, an org-wide pin), verify against the org's approved/reviewed version too — not just "does it run here." A bad pick here becomes the default everyone else copies.
- **Distinguished/Fellow-level angle:** if the verified choice is about to become the company's default (the pin every new service inherits, or a pattern written up for others to follow), the real test is whether the rationale is documented well enough that a team five years from now can trust it without tracking down whoever originally verified it.
- **Executive angle (CTO/VP-Eng):** if the choice becomes the org-wide default, weigh license terms, vendor lock-in, and EOL/support timeline against staying flexible — a dependency the vendor could deprecate or reprice is a budget and continuity risk, not just an engineering pick.

If what you found differs from memory, **record that fact** — the next person would otherwise make the same mistake. Keep that record to the actual correction; don't turn a one-line "the flag was renamed" fact into an unrequested writeup — brevity doesn't happen automatically at lower effort, so say what scope you want.
