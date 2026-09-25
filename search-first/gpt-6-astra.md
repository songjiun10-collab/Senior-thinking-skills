> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

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

Just verify it — don't ask whether you should check the docs first. When the situation above applies (external library, version-tied behavior, an unverified "should work"), that's the trigger to look it up directly, not a decision to bring back as a question. Asking "should I check the docs for this?" is itself the failure mode to catch here: infer that verification is wanted from the fact that the task touches a third-party surface, and go do it.

## Cost Sense

Verify when the cost of checking is **cheaper than the cost of being wrong** — usually it is, by a lot. Conversely, re-checking a stable API on a well-known standard library every single time is waste.

- **Principal-level angle:** if the library or version choice becomes a dependency other teams or services will inherit (a shared build, a common base image, an org-wide pin), verify against the org's approved/reviewed version too — not just "does it run here." A bad pick here becomes the default everyone else copies.
- **Distinguished/Fellow-level angle:** if the verified choice is about to become the company's default (the pin every new service inherits, or a pattern written up for others to follow), the real test is whether the rationale is documented well enough that a team five years from now can trust it without tracking down whoever originally verified it.
- **Executive angle (CTO/VP-Eng):** if the choice becomes the org-wide default, weigh license terms, vendor lock-in, and EOL/support timeline against staying flexible — a dependency the vendor could deprecate or reprice is a budget and continuity risk, not just an engineering pick.

If what you found differs from memory, **record that fact** — the next person would otherwise make the same mistake. With 1.05M context, a whole dependency tree's docs and changelogs can be pulled into one pass and cross-checked together rather than verified one library at a time — do this yourself for a broad audit rather than waiting to be asked to widen scope; state the scope you covered so the next reader knows what was and wasn't checked.
