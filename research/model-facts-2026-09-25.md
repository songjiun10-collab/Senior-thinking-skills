# Model facts the per-model files may rely on (verified 2026-09-25)

Every per-model file (`opus-5-5.md`, `fable-5-1.md`, `sonnet-5.md`, `gpt-6-astra.md`, `gpt-6-sol.md`, `gpt-6-luna.md`) may state a model behavior **only if it traces to a row below**, attributed the way the row attributes it. Anything else is this bundle's own guidance and must be written as guidance ("do X"), not as a claim about the model ("you tend to X" / "documented").

Re-verify when a new model ships: these are per-generation vendor notes, not fixed properties of a brand name.

## Sources (fetched 2026-09-25)

| Key | Source |
|---|---|
| A-BP | Anthropic, [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) |
| A-O55 | Anthropic, [Prompting Claude Opus 5.5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5) |
| A-O5 | Anthropic, [Prompting Claude Opus 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5) |
| A-F51 | Anthropic, [Prompting Claude Fable 5.1](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1) (covers Fable 5.1 **and Mythos 5.1**) |
| A-F5 | Anthropic, [Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5) |
| A-S5 | Anthropic, [Prompting Claude Sonnet 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5) |
| A-MO | Anthropic, [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) |
| A-SK | Anthropic, [Skill authoring best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) |
| O-G6 | OpenAI, [Using GPT-6](https://developers.openai.com/api/docs/guides/latest-model) (prompting guidance "addresses behavior observed with GPT-6 Astra; evaluate with your chosen model") |
| O-AB | OpenAI, [Rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra) |
| O-SC | OpenAI, [GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra), Appendix A "GPT-6 Sol, GPT-6 Luna" (added 2026-09-22) |
| O-M | OpenAI model pages: [gpt-6-sol](https://developers.openai.com/api/docs/models/gpt-6-sol), [gpt-6-luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [gpt-6-astra](https://developers.openai.com/api/docs/models/gpt-6-astra) |

## Specs

| Model | Thinking | Default effort | Context | Max output | Source |
|---|---|---|---|---|---|
| Claude Fable 5.1 / Mythos 5.1 | Adaptive, always on | `high` | 1M | 128K | A-MO |
| Claude Opus 5.5 | Adaptive, always on | `medium` (Opus 5 was `high`) | 1M | 128K | A-MO, A-O55 |
| Claude Sonnet 5 | Adaptive, on by default (can be disabled) | `high` | 1M | 128K | A-MO, A-S5 |
| GPT-6 Astra | reasoning; no `none` effort | — | 1.05M | 128K | O-M, O-G6 |
| GPT-6 Sol | reasoning; `none`…`max`, default `medium` | `medium` | 1.05M | 128K | O-M |
| GPT-6 Luna | reasoning; `none`…`max`, default `medium` | `medium` | 1.05M | 128K | O-M |

Effort is set by the caller per request (or per message via a beta / `configuration_update`); a running turn cannot raise its own effort.

## Claude Opus 5.5

A-O55 says existing Opus 5 prompts "should perform well without changes, and the patterns in Prompting Claude Opus 5 remain a reasonable starting point." So Opus 5 rows below may be applied to Opus 5.5 **labeled as inherited from Opus 5 guidance**, never as "documented for Opus 5.5".

Documented for Opus 5.5 itself (A-O55):
- Thinking always on; effort is "the main control"; lowering effort reduces thinking "more reliably than prompt instructions do"; thinks more per turn than Opus 5 at a given level.
- On long multi-part tasks it keeps the user updated, and **some updates end the turn with text (`end_turn`) while work remains** — "treat a text-only end of turn as a report rather than as proof the task is done"; keep parts in a checklist the model updates.
- Named early-stop patterns: a summary that announces the next step with no tool call; offering to continue unless told otherwise; listing non-blocking decisions for the user; stopping to report because a milestone is done.
- "Tends to get to work quickly"; on loosely specified multi-app tasks, telling it to explore relevant sources first improved results.
- Pays close attention to elapsed-time signals; in multiagent setups a time budget speeds work, "might search and verify a little less" under time pressure.
- In multi-turn chat it sometimes re-examines earlier answers while thinking about a new message.
- Resists indirect prompt injection better than any earlier Opus; pasted text should be marked.
- Strongest on multistep repository work and code review ("more bugs caught … fewer false alarms"); sustains long autonomous work with parallel subagents.
- `reasoning_extraction` refusal category: prompts that push it to reproduce internal reasoning in the response can be declined.

## Claude Opus 5 (inheritable by Opus 5.5, see above)

A-O5:
- Verifies its own work without being told; explicit verification instructions ("include a final verification step", "use a subagent to verify") **cause over-verification** — remove them.
- "Can also expand the scope of a task, adding steps that weren't requested or applying its own judgment about what the task should be."
- "Delegates to subagents more readily than prior models"; don't delegate work finishable in a handful of tool calls, and don't use subagents to verify own work.
- Catches and fixes own mistakes well; avoid "double-check your answer" instructions.
- Review prompts saying "only report high-severity issues" get followed literally → report everything, filter separately.
- Default responses and written deliverables run longer.

## Opus 4.x only — do NOT attribute to Opus 5.5

A-BP: "Claude Opus 4.5 and Claude Opus 4.6 have a tendency to overengineer by creating extra files, adding unnecessary abstractions, or building in flexibility that wasn't requested." Also Opus 4.6's "strong predilection for subagents" and heavy upfront exploration. The closest Opus 5-line fact is A-O5's scope expansion above.

## Claude Fable 5.1 / Mythos 5.1

A-F51 (Fable 5 prompts "should perform well … without changes"):
- Writes **fewer user-facing updates** during long tool-calling turns than Fable 5; more pronounced at higher effort.
- Sometimes ends a turn before the work is done: describes the next step instead of doing it, or asks permission for a step the request already covered.
- On open-ended features, "delivers what's asked for and sometimes more": fixes nearby code, extends unmentioned behavior, commits more test files than warranted.
- At `low` effort calls search/retrieval less and answers from memory more.
- More likely to reproduce source passages without marking them as quotations.
- More likely than Fable 5 to rewrite whole files for small changes.
- Prose can be denser (longer sentences, fewer breaks); uses less formatting in chat.
- At `xhigh`/`max` can think long before writing a long deliverable, sometimes drafting it in thinking first.
- Responds well to explicit instructions on what compaction summaries must preserve.
- Lead agent often waits for subagents even when it could keep working.

Inheritable from Fable 5 (A-F5), labeled as such:
- Long-horizon autonomy; longer turns by default; can overplan when a task is ambiguous.
- At higher effort on routine work, can gather context and deliberate beyond what the task needs; can elaborate beyond need (surveying options it won't pursue, long root-cause explanations, heavily structured PR descriptions, comments narrating the next line).
- Strong instruction following: a brief instruction steers most behaviors.
- Instruct it to audit progress claims against actual tool results on long runs ("nearly eliminated fabricated status reports").
- Occasionally takes unrequested actions (e.g. drafting an unasked email, defensive git-branch backups) → state boundaries.
- Dispatches parallel subagents more readily; prefers async orchestration.
- "Separate, fresh-context verifier subagents tend to outperform self-critique."
- **"Skills developed for prior models are often too prescriptive for Claude Fable 5 and can degrade output quality."**
- Don't instruct it to reproduce its reasoning in the response (`reasoning_extraction`).
- In very long sessions may suggest a new session or trim its work when shown a token countdown.

## Claude Sonnet 5

A-S5:
- Calibrates response length to task complexity.
- Effort default `high`; **respects effort strictly**: at `low`/`medium` it scopes to what was asked; risk of under-thinking on moderately complex tasks at `low`.
- More agentic than Sonnet 4.6: reaches for tools and runs self-verification loops more readily; with thinking disabled, less likely to use tools or search.
- **Literal instruction following**, especially at lower effort: doesn't generalize an instruction from one item to another or infer unmade requests — state scope explicitly.
- Regular, higher-quality progress updates on long traces.
- Review prompts with a severity bar are followed faithfully → lower recall; make coverage the finding-stage job.
- Tracks its remaining context window ("context awareness"; A-BP: Sonnet 5, Sonnet 4.6/4.5, Haiku 4.5) and "may sometimes naturally try to wrap up work as it approaches the context limit" — in a compacting harness, tell it to save state and continue.

## GPT-6 Astra

O-G6, O-AB:
- More likely to ask a clarifying question when input could materially change the result; can stop where the user expected reasonable assumptions; "likes to ask non-blocking questions as it's working by default."
- Can feel "more tentative about when to stop"; "may reach a first implementation and come back for your review while there's still work to do" → define completion up front.
- **More sensitive to instructions in skills and AGENTS.md**; "unclear or conflicting guidance in a skill file may cause the model to pause and block work early"; OpenAI "strongly recommend[s] auditing skills".
- Strong boundary language written for earlier models may be taken "too seriously" and stop work early.
- Runs tests and checks its work on its own; thorough testing "can result in broader tests than the task requires" for small tasks.
- May delegate to subagents less often than desired.
- Tends toward detailed, formatted responses (lists, tables) and recurring phrases.
- Can work out what to read without being pushed to review the whole project.
- O-SC Respecting Warnings: GPT-6 Astra worked around an environment barrier in 19% of rollouts vs 64% for GPT-5.6 Sol (low-stakes settings, no system-level controls). Much better than its predecessor; not zero. "Lowest in the family" is not established — Sol/Luna figures are only in a chart.
- Skill guidance: short descriptions, minimal router root, avoid "elaborate itineraries"; "Guidance that helps Sol or Luna may overconstrain GPT-6 Astra."

## GPT-6 Sol

O-M, O-SC, Codex docs:
- "Highly capable, lower-cost alternative to Astra"; "built for complex coding and agentic workflows"; Codex suggests Sol Medium for everyday and complex coding.
- O-G6 prompting guidance was written from Astra behavior; OpenAI says to evaluate it on Sol/Luna. **No Sol-specific prompting behaviors are documented.**
- O-SC safety/alignment (evaluation conditions, not production rates):
  - Respecting warnings: GPT-6 Sol shows "a modest reduction in failures" vs GPT-5.6 Sol (Luna "a much larger reduction").
  - Unintended engagement with external agent messages: among samples that found the board, Sol attempted communication in 26% and performed the specified unauthorized action in 11% (Astra 27% / 0%, Luna 0% / 0%).
  - Respecting auto-review: no bypass attempts by GPT-6 Sol.
  - Coding deception and broken-search-tool failures: large improvements over GPT-5.6 Sol.
  - Default answers ~45% shorter than GPT-5.6 Sol on HealthBench.
- Not documented anywhere checked: "weak resistance to a wrong-but-plausible safety justification".
- Not documented anywhere checked: "effort peaks below the top setting", "follows instructions fairly literally" (that is a Sonnet 5 fact).

## GPT-6 Luna

O-M, O-SC:
- "Our most efficient model for focused, high-volume tasks"; OpenAI guide: "efficient, repeatable work at scale"; Codex: "Luna High for focused, repeatable tasks".
- Some higher jailbreak-defense scores "may reflect a broader tendency to refuse requests, including legitimate ones."
- Attempted (never succeeded) to bypass an auto-review monitor in the evaluation; no honeypot exploitation; no engagement with external agent messages.
- Default answers ~35% shorter than GPT-5.6 Luna on HealthBench.
- Not documented: the "classification, extraction, routing, structured summarization" task list, or literal instruction following — use OpenAI's own wording.
- No Luna-specific prompting behaviors are documented.

## Models without a file

Claude Mythos 5.1 shares A-F51 with Fable 5.1 → use `fable-5-1.md`. Claude Haiku 4.5 (no effort support, 200K context), Opus 5, and other families → `sonnet-5.md` (router fallback).

## User-reported corroboration (2026-09-25, independent of vendor docs)

Vendor prompting guides are the model-behavior source of record above. These are user/community reports checked against them — cited only where they either **corroborate** a vendor claim with an independent real-world instance, or surface a **gap the vendor docs don't cover**. Not used to override a vendor claim. Each is a single or small number of reports, not a benchmark — cite as "reported," never as "documented."

- **Corroborates Opus 5's over-verification/scope-expansion docs:** community threads on Opus 5's verbosity and unrequested scope ("won't shut up," over-engineering reactions) match what Anthropic's own Opus 5 guide names as needing a damping prompt. No new claim, just independent confirmation the pattern shows up in practice.
- **Corroborates Fable 5.1's "writes less user-facing text between tool calls":** an independent long-form review (Zvi Mowshowitz, Sept 2026) describes exactly this — "silence during long tasks is ambiguous — you do not know whether the model is thinking, executing, stuck, or quietly repeating the same failed approach" — while noting the model "remains readable over long, multi-step tasks" once it does report. Matches `plan-on-disk`/`delegate-to-subagents`'s existing narration guidance; no file changed, since the guidance already covers it.
- **Gap for Sonnet 5, not covered by the vendor prompting guide:** [anthropics/claude-code#83085](https://github.com/anthropics/claude-code/issues/83085) (closed, not planned, no maintainer response) reports Sonnet 5 "running `git reset --hard` without even asking and without any indication to do so" and "constantly ignoring rules in Claude.md, other files or even rules explicitly said in the chat." This is one user's report, not a documented vendor fact, and it sits in tension with Anthropic's own "follows instructions more literally" framing — literal instruction-following is not the same guarantee as respecting a stated boundary. Added as a caution, not a documented tendency, to files where a Sonnet 5 destructive-action or CLAUDE.md-compliance gap actually matters.
- **Gap for GPT-6 Astra, not covered by the system card:** [openai/codex#46700](https://github.com/openai/codex/issues/46700) (open, no OpenAI response as of this check) reports GPT-6 Astra at `xhigh`/`max` effort "repeatedly reverted and rewrote its own earlier changes, contradicting decisions it had already made. Completed phases were never treated as done," "ignored explicit instructions from the plan and from AGENTS.md," "created files and changes nobody requested," and wrote close to 1TB to `/tmp` over a full day without completing ~30% of a plan. One report, not a documented rate — but it names a concrete failure mode (a phase marked done doesn't stay done; unattended runs can blow through disk/usage budgets) that the vendor docs' "more tentative about stopping" framing doesn't warn against. Added as a caution to `plan-on-disk` and `verify-before-claiming` for `gpt-6-astra.md`.
- Separately, a viral r/codex thread (relayed via a secondary blog, not verified against the original thread) describes GPT-6 Astra building "multiple layers of verification, smoke tests, and SHA256 hash checks" for small requests — this corroborates the system card's own "broader tests than the task requires" note already cited in `verify-before-claiming/gpt-6-astra.md`; no file change needed.
