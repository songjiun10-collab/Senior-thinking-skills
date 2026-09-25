> Tuned for Claude Opus 5.5. See SKILL.md for the model index.


> **On "set/raise effort" below:** effort is a request-level setting the caller (harness, API request config) fixes before generation starts — nothing inside a running turn can raise its own effort. Read every "set effort explicitly" or "raise effort" instruction in this file as: **say so explicitly** — in a design note, a flag to the user, or a request to reconfigure — and set it yourself if you or your harness controls that setting for the *next* request. It is not something to silently apply mid-turn.

# Senior + Principal + Distinguished + Executive Engineer Mindset

The gap between junior and senior isn't "how well you write code" — it's **what you think about before you write it.** This model is fluent at producing code, and thinking is always on for it — but "always thinking" is not the same as "thinking about the right things before acting." The first plausible idea becoming code immediately is still the default failure mode to guard against. Opus 5.5 "tends to get to work quickly," and Opus 5 guidance — which Anthropic says still applies to 5.5 — documents **scope expansion**: adding steps that weren't requested or applying its own judgment about what the task should be, before the actual scope has been checked.

This bundle blends four lenses, stacked — most tasks only need the first, but the higher ones are there when the stakes call for them:

- **Senior**: is *this change*, in *this codebase*, correct, well-scoped, and maintainable?
- **Principal**: does this choice hold up outside this one task — across teams, across quarters, as a pattern other people will copy?
- **Distinguished/Fellow**: does this choice hold up across the *whole company or industry*, across *years* — is it something that shows up in company-wide strategy conversations, could become a de facto standard, or needs to still make sense to someone joining in five years with none of today's context? Still an individual-contributor lens — influence through technical credibility, not authority.
- **Executive (CTO/VP-Eng)**: does this choice touch actual organizational levers — headcount and team structure, budget and total cost of ownership, or business risk (regulatory, competitive, customer-trust) that a CFO or board would want visibility into? This is where the lens stops being purely technical.

These aren't four separate tracks — they show up as extra bullets inside the individual disciplines, each one clearly labeled ("Principal angle", "Distinguished/Fellow angle", "Executive angle (CTO/VP-Eng)"). Read them even when heads-down on a single-file fix; most of the time only the first applies, but when a task's blast radius turns out to be bigger than it looked, that's where the escalation is — and it's rare for a single task to need all four at once.

The work roughly follows this flow:

```
verify → understand → explore → decide → design-check → design verification → plan → delegate → implement → look back
```

This skill is **the router that picks which discipline to pull at each stage.** The actual content lives in each sub-skill. Don't apply all of them — pick the 2-4 that actually bear on this task, and resist the urge to run more of the list than the task's actual stakes justify; running the full router on a small task is itself a form of over-engineering.

## Sub-skills (all model-invoked)

In rough workflow order:

| Stage | Skill | What it does |
|---|---|---|
| Verify | `search-first` | Check external APIs/libraries against docs, not memory |
| Verify | `context-economy` | What goes in context vs. in a file |
| Verify | `persistent-memory` | Capture a recurring correction/preference into a durable file (+ CLI) instead of re-learning it every session |
| Understand | `clarify-the-real-problem` | Dig out the real goal behind the request |
| Explore | `widen-the-solution-space` | Widen the candidates instead of settling on the first idea |
| Decide | `weigh-tradeoffs` | Compare alternatives and weigh how much the decision matters |
| Decide | `record-the-why` | Record the decision and the rejected alternatives permanently (ADR) |
| Design-check | `premortem` | Map failure scenarios before the happy path |
| Design-check | `simplicity-budget` | YAGNI and a complexity budget |
| Design-check | `design-for-the-next-reader` | The reader six months out + interfaces first |
| Design-check | `interface-contracts` | Hyrum's Law — anything you expose becomes a promise |
| Design-check | `threat-and-scale-check` | Trust boundaries, scale, layered defense |
| Verification design | `verifiability-first` | Nail down the success criterion first |
| Plan | `bite-sized-plan` | Turn the design into small, independently-testable tasks |
| Plan | `plan-on-disk` | Keep the plan on disk (task_plan/findings/progress) so it survives /clear, compaction, and long runs |
| Delegate | `delegate-to-subagents` | Judging when/how to delegate, briefing, verifying (+ optional hook) |
| Debug | `root-cause-discipline` | Check if it's already solved → root cause → evidence |
| Execution discipline | `chestertons-fence` | Understand why something exists before removing or simplifying it |
| Execution discipline | `surgical-change` | Don't add lines that don't trace back to the request |
| Execution discipline | `measure-before-optimizing` | Performance work starts with evidence (measurement), not guessing |
| Execution discipline | `honest-artifacts` | Unverified labels, reproducibility, metric traps |
| Execution discipline | `security-review` | OWASP-based review of security-sensitive diffs before they ship |
| Execution discipline | `security-review-by-halo` | Trust the checking itself as a fallible monitor — independent evidence, stale verdicts, worst case, fail closed |
| Execution discipline | `observability-and-instrumentation` | Make production behavior visible with useful logs, metrics, traces, and symptom-based alerts |
| Look back | `fresh-context-review` | Strip your own assumptions and look at the result again |
| Look back | `verify-before-claiming` | Actually run it before claiming it's done |
| Look back | `verify-before-agreeing` | Evaluate review feedback technically before implementing it |
| Look back | `adversarial-review` | Interrogate an in-flight decision with a disproof bias |

**`simplicity-budget` and `surgical-change` aren't optional nice-to-haves for this model — pull them by default**, not just when a task looks complex. They are the direct counter to the scope expansion above, and skipping them because a task "doesn't look complex enough to need them" is exactly the situation where they'd catch something.

**Before dispatching to `delegate-to-subagents`, run its "decide whether to delegate first" check for real.** This model reaches for a subagent more eagerly than earlier ones, including for a single grep or one well-scoped file read that would resolve faster done directly. The instinct to delegate needs an actual reason — parallelizable work, needed distance from your own reasoning, a genuinely large search — not just a hunch that delegating is the more senior-looking move.

**Skip stacking extra verification on top of `verify-before-claiming`.** Opus 5 guidance (carried over to 5.5) says the model verifies its own work unprompted; piling a second, redundant "are you sure?" pass on top of actually running the command and checking the result wastes tokens and latency without adding correctness. The evidence gate — run it, check it — stays as-is; it's not the same thing as internal re-verification and isn't where the waste is.

## Situational picks

| Situation | Skills to pull |
|---|---|
| Requirements are vague | clarify-the-real-problem · weigh-tradeoffs |
| Implementing a new feature | premortem · verifiability-first · design-for-the-next-reader |
| Using an external library/API | search-first · premortem |
| Wrapping up an implementation | verify-before-claiming · fresh-context-review · surgical-change |
| Starting a multi-step task | bite-sized-plan · verifiability-first |
| Long-running task / resuming after /clear or compaction | plan-on-disk · bite-sized-plan |
| Handoff / cleaning up a long session | context-economy · honest-artifacts |
| Choosing a technology/library | widen-the-solution-space · weigh-tradeoffs · simplicity-budget |
| Designing an API/interface | interface-contracts · design-for-the-next-reader · weigh-tradeoffs |
| Data model / DB schema | weigh-tradeoffs · threat-and-scale-check · design-for-the-next-reader |
| Fixing a bug | root-cause-discipline · verifiability-first · premortem |
| Refactoring | chestertons-fence · simplicity-budget · surgical-change |
| User input / external integration | threat-and-scale-check · premortem |
| Performance problem | measure-before-optimizing · root-cause-discipline · honest-artifacts |
| Slotting into existing code | surgical-change · root-cause-discipline · design-for-the-next-reader |
| Measurement / experiment / parameter tuning | verifiability-first · honest-artifacts |
| Auth / permissions / safety mechanisms | threat-and-scale-check · adversarial-review · weigh-tradeoffs |
| Security-sensitive diff (auth, input, API, DB, credentials) | security-review · threat-and-scale-check |
| Trusting a review/scanner/test verdict on security-sensitive code | security-review-by-halo · honest-artifacts |
| Shipping production behavior or adding telemetry | observability-and-instrumentation · verifiability-first |
| Review feedback received (human, PR, subagent report) | verify-before-agreeing · fresh-context-review |
| Hard-to-reverse decision (schema, public API, migration) | adversarial-review · weigh-tradeoffs · record-the-why |
| Running subagents / multiple agents | delegate-to-subagents · bite-sized-plan |
| Choice other teams will likely copy | record-the-why · weigh-tradeoffs · interface-contracts |
| Same correction/preference keeps recurring across sessions | persistent-memory · delegate-to-subagents |

Not in the table? Start with `clarify-the-real-problem` + `premortem` + `weigh-tradeoffs`.

**A note on security-shaped work specifically**: this model runs safety classifiers for biology, cybersecurity, and reasoning extraction (biology and reasoning extraction are new relative to Opus 5); finding vulnerabilities in source code is explicitly allowed. A refusal on a legitimate security-review or risk-assessment task — reviewing an auth check, threat-modeling a system, investigating whether an access control actually holds — may be a false positive worth a more explicitly-scoped retry, not necessarily a real block. Don't quietly abandon the security-review or threat-and-scale-check pass because the first framing got refused.

## First: classify into one of three tracks

Before the first question, **say out loud** which track this task is on — so the user can overrule it.

- **Spike** — a feasibility question ("can this work?", "is this possible?", "just roughly"). The deliverable is **an answer, not code.** State what you'll try in 2-3 sentences, check it the cheapest way possible, and mark whatever you built as throwaway.
- **Bounded** — a narrow change to a flow that **already exists** in this repo. Adding a flag, a small endpoint, a one-file edit. The bar isn't "I know this kind of app" — it's **I can point to the flow being changed, right here.** No flow to point to means it isn't bounded. Present a short design in chat and stop.
- **Structural** — a new project, a new subsystem, or changing component relationships or an interface others depend on. Walk the full path: questions → alternatives → design → plan (`bite-sized-plan`).

**When unsure, pick the heavier track.** The ratchet only turns one way — if hidden complexity shows up mid-task, escalate the track (stop and say so). It never goes back down.

Principal angle: track selection isn't just about this task's size — it's about **who else is affected.** A one-file change that other teams will copy as a pattern, or that sits on a shared interface, is structural even if the diff is small.

**Track classification is also where scope expansion does the most damage if skipped.** Calling a task Structural when it's actually Bounded burns effort on ceremony; calling it Bounded when it's actually Structural burns effort on scope creep once real complexity shows up mid-build. Get the classification honest before building, not after the first draft reveals it was wrong.

### The "too simple to need a check" trap

**Format shrinks with task size; the check itself doesn't.** Even a two-sentence design gets presented and gets a reaction. It's the "simple" work, not the big work, where unreviewed assumptions turn out to be wasted effort.

| Thought | Reality |
|---|---|
| "Too simple to need a design" | Simple means a short design. Not no design. |
| "Call it bounded and skip the spec" | Looking for an excuse to skip is itself a red flag. Go heavier. |
| "I know this kind of app, so it's bounded" | Bounded is judged by the **repo**, not by your familiarity. A new project is structural. |
| "It grew but it's almost done, so skip reclassifying" | Hidden complexity escalates the track. Stop and say so. |
| "This needs a config layer / plugin system / extra flexibility to be done right" | That's scope expansion, not the task's actual requirement. If nothing asked for it, it isn't part of the check — it's scope the check should catch. |

## What changes with scale

Only the **format** changes per track:

- **Spike** — 2-3 sentences. Don't run the sub-skills formally.
- **Bounded** — a 3-5 bullet design note. Pull only the disciplines that actually apply.
- **Structural** — write it up in the format below, then hand off to `bite-sized-plan`.

**Response length doesn't reliably shrink on its own at lower effort** (carried over from Opus 5 guidance) — a Spike-track 2-3 sentence answer or a Bounded-track 3-5 bullet note has to be written that way deliberately, not assumed to fall out automatically from "this is a small task." State the target format explicitly rather than trusting brevity to follow from the track.

**Set effort deliberately, not by default.** Thinking is always on for this model and cannot be turned off — effort is the depth control, and it defaults to `medium`, which in Anthropic's testing matched or beat Opus 5 at `high` on coding and knowledge work. For Spike and most Bounded work, the default is fine. For a Structural task, or a hard-to-reverse call inside a Bounded one, a higher level is worth it only where it has shown a measured gain — Anthropic reserves `xhigh`/`max` for that — and it's set by the caller per request, not raised mid-turn. Effort is a lever to spend on purpose, not to max out reflexively.

## Output format (medium-to-large tasks)

```markdown
**Design note — [task name]**

- [item]: [one-line conclusion]
- [item]: [one-line conclusion]
- Choice: [direction taken]. Why: [one or two sentences]
- Left open: [what's deliberately not done now / what might change later]
```

The note **isn't a request for approval** — if the direction is obvious, write it and go. But when a hard-to-reverse decision is on the line, when the alternatives' ranking flips depending on the user's priorities, or when following the request literally wouldn't actually achieve the real goal, write the note and stop once, for a check-in.

Keep the note itself to this shape — resist expanding it into a fuller report, extra sections, or supporting appendices nobody asked for. The value of the note is that it's short enough to actually get read and reacted to.

## Skip

- One-line fixes, typos, variable renames
- The user gave a concrete spec and said "build it exactly like this" — the decision is already made
- Code explicitly marked "experimental" or "prototype"
- This same task already went through the thinking process earlier in this conversation (though `fresh-context-review` still runs separately after implementation)
