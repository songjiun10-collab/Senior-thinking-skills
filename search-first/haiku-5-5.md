> Tuned for Claude Haiku 5.5. Source: Anthropic prompting guide (prompting-claude-haiku-5-5). Body carried from the Sonnet file; the calibration section is Haiku-specific. See SKILL.md for the model index.

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

This model follows instructions more literally than the prior generation — if "verify this" should mean walking all four steps (not just glancing at a doc page), say so; an underspecified verification request tends to get done narrowly rather than generously expanded to the full check. Tool-use triggering also differs from the prior generation, so if a fetch or search tool should fire for a given check, phrase the trigger explicitly rather than assuming it will be inferred.

## Cost Sense

Verify when the cost of checking is **cheaper than the cost of being wrong** — usually it is, by a lot. Conversely, re-checking a stable API on a well-known standard library every single time is waste.

- **Principal-level angle:** if the library or version choice becomes a dependency other teams or services will inherit (a shared build, a common base image, an org-wide pin), verify against the org's approved/reviewed version too — not just "does it run here." A bad pick here becomes the default everyone else copies.
- **Distinguished/Fellow-level angle:** if the verified choice is about to become the company's default (the pin every new service inherits, or a pattern written up for others to follow), the real test is whether the rationale is documented well enough that a team five years from now can trust it without tracking down whoever originally verified it.
- **Executive angle (CTO/VP-Eng):** if the choice becomes the org-wide default, weigh license terms, vendor lock-in, and EOL/support timeline against staying flexible — a dependency the vendor could deprecate or reprice is a budget and continuity risk, not just an engineering pick.

If what you found differs from memory, **record that fact** — the next person would otherwise make the same mistake. With 1M context, a whole dependency tree's docs and changelogs can be pulled in and cross-checked in one pass rather than verifying one library at a time — useful for a broad audit, if that's the scope actually wanted.

## Calibration (Anthropic official prompting guide, Haiku 5.5)

- **Effort**: `low`, `medium` (default), `high`, `xhigh`, `max`. At `low`, long agent prompts see more skipped searches, early stops, and skipped checks. Thinking can be turned off with `{type: "disabled"}` at `low`/`medium`/`high` only; at `xhigh`/`max` it is a 400.
- **Search**: send today's date, and add a nudge that training data may be stale for records, prices, versions and "latest". Avoid blanket "search for everything" instructions; they cause searches on prompts that need none.
- **JSON output with your own tools**: with thinking off, the model can skip a needed tool call. Use adaptive thinking, drop `output_config.format` on tool-calling requests, or force the call with `tool_choice`.
- **Early stopping** (long agent prompts at `low`): add an explicit keep-working line and a no-extra-scope line.
- **Coding verification**: ask for a real check (tests, type-checker, build) before reporting code done.
- **Mid-turn user messages**: never put user text inside a `tool_result`; append it as a text block in the user turn.
- **Chatbots**: add an explicit rules-hold-for-the-whole-conversation line to resist pressure from users.
- **Safeguard refusals**: categories `cyber`, `frontier_llm`, `bio`, `general_harms`. No server-side fallback, so handle `stop_reason: "refusal"` in the client.
