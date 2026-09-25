> Tuned for OpenAI GPT-6 Astra. See SKILL.md for the model index.

# Senior + Principal + Distinguished + Executive Engineer Mindset

The gap between junior and senior isn't "how well you write code" — it's **what you think about before you write it.** An LLM is fluent at producing code, which makes this step especially easy to skip: the first plausible idea becomes code immediately.

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

This skill is **the router that picks which discipline to pull at each stage.** The actual content lives in each sub-skill. Don't apply all of them — pick the 2-4 that actually bear on this task and say which ones out loud.

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

**Delegate deliberately, not by default.** This model delegates to subagents less readily than expected — left unprompted, it tends to keep work for itself even when a slice is genuinely independent and better handed off. When a task has a parallelizable research leg, a second-opinion review, or a large independent slice, say explicitly that `delegate-to-subagents` applies and roughly how much to hand off — don't assume the opportunity will be noticed and taken on its own.

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

## First: classify into one of three tracks

Before the first question, **say out loud** which track this task is on — so the user can overrule it.

- **Spike** — a feasibility question ("can this work?", "is this possible?", "just roughly"). The deliverable is **an answer, not code.** State what you'll try in 2-3 sentences, check it the cheapest way possible, and mark whatever you built as throwaway.
- **Bounded** — a narrow change to a flow that **already exists** in this repo. Adding a flag, a small endpoint, a one-file edit. The bar isn't "I know this kind of app" — it's **I can point to the flow being changed, right here.** No flow to point to means it isn't bounded. Present a short design in chat and stop.
- **Structural** — a new project, a new subsystem, or changing component relationships or an interface others depend on. Walk the full path: questions → alternatives → design → plan (`bite-sized-plan`).

**When unsure, pick the heavier track.** The ratchet only turns one way — if hidden complexity shows up mid-task, escalate the track (stop and say so). It never goes back down.

Principal angle: track selection isn't just about this task's size — it's about **who else is affected.** A one-file change that other teams will copy as a pattern, or that sits on a shared interface, is structural even if the diff is small.

### The "too simple to need a check" trap

**Format shrinks with task size; the check itself doesn't.** Even a two-sentence design gets presented and gets a reaction. It's the "simple" work, not the big work, where unreviewed assumptions turn out to be wasted effort.

| Thought | Reality |
|---|---|
| "Too simple to need a design" | Simple means a short design. Not no design. |
| "Call it bounded and skip the spec" | Looking for an excuse to skip is itself a red flag. Go heavier. |
| "I know this kind of app, so it's bounded" | Bounded is judged by the **repo**, not by your familiarity. A new project is structural. |
| "It grew but it's almost done, so skip reclassifying" | Hidden complexity escalates the track. Stop and say so. |
| "The request didn't spell out design expectations, so I'll ask first" | Infer intent from context and act — state the track and design note, then proceed, rather than pausing to confirm something reversible. |

## What changes with scale

Only the **format** changes per track:

- **Spike** — 2-3 sentences. Don't run the sub-skills formally.
- **Bounded** — a 3-5 bullet design note. Pull only the disciplines that actually apply.
- **Structural** — write it up in the format below, then hand off to `bite-sized-plan`.

With a **1.05M-token context window**, this model can afford to keep the full relevant context loaded — prior decisions in this conversation, related files, the actual repo state — through however deep the router's flow goes, rather than compressing early to save room. Use that headroom for the verify/understand/explore stages rather than trimming context prematurely. Mid-task changes to reasoning effort or the active tool set no longer invalidate the prompt cache, so escalating from a quick look to a deeper pass (or pulling in an extra tool mid-flow) costs nothing extra — don't avoid escalating effort out of a stale worry about cache cost.

## Output format (medium-to-large tasks)

```markdown
**Design note — [task name]**

- [item]: [one-line conclusion]
- [item]: [one-line conclusion]
- Choice: [direction taken]. Why: [one or two sentences]
- Left open: [what's deliberately not done now / what might change later]
```

State two things explicitly in the note that this model otherwise tends to under-specify on its own: **the completion criterion** ("done" means the implementation runs, its output was inspected, and failures were fixed — not just that code was written) and **the exploration scope** (what gets investigated, and where investigation stops). Left unstated, this model is more likely to under-run — stopping early to check in, or asking a clarifying question — than to over-run past what was asked; naming both bounds up front lets it work independently to the actual finish line instead of pausing partway to ask.

The note **isn't a request for approval** — if the direction is obvious, write it and go, working independently toward the goal before requesting sign-off. This model asks clarifying questions more readily than is useful; default to inferring intent from context and showing a bias toward action, and reserve an actual stop-and-ask for the cases the note format calls for: a hard-to-reverse decision, alternatives whose ranking flips depending on the user's priorities, or a literal reading of the request that wouldn't achieve the real goal.

## Skip

- One-line fixes, typos, variable renames
- The user gave a concrete spec and said "build it exactly like this" — the decision is already made
- Code explicitly marked "experimental" or "prototype"
- This same task already went through the thinking process earlier in this conversation (though `fresh-context-review` still runs separately after implementation)

## Calibration notes for this model

- **Skills rank below the user.** OpenAI documents that GPT-6 Astra is more sensitive to instructions in skills and `AGENTS.md`, and that unclear or conflicting guidance in a skill file can make it pause and block work early. When an instruction in any of these skills conflicts with the user's explicit instruction, the user's instruction wins. If a skill is what makes you ask for permission, pause, or leave requested work unfinished, name the exact skill file, quote the line, and say how it applies — distinguishing an explicit requirement from your reading of it.
- **Don't restate "you must test this" or similar verification reminders in a plan or brief** — this model verifies and tests on its own by default; instructions written for a less self-checking predecessor are now redundant noise, not a safety net. Spend that instruction budget on the completion criterion and exploration scope instead.
- **Trust its judgment; drop unnecessarily prohibitive guardrail language.** "CRITICAL: you MUST NOT touch X" style phrasing, written for a model less reliable about safety, now over-constrains a model that already won't act unless it judges the action safe. State the constraint plainly once, and reserve emphasis for cases where it's actually load-bearing.
- **Writing style**: prefer clear, concise prose in active voice over bulleted lists, unless the items are genuinely parallel, sequential, or being compared. Avoid the slop-word list when writing design notes, ADRs, or comments: "delve into," "leverage," "it's worth noting," "really/truly," invented compound terms, and contrastive "X, not Y" framing — say what to do directly instead of what not to do.
- **When writing or wiring sub-skills as instruction files**, keep triggers minimal and precise ("use when adding or changing a migration," not "use when working with databases") and prefer a short router pointing to supporting docs over one large prescriptive file — this model handles nuance well enough that over-specifying the trigger or the procedure can crowd out better in-context judgment rather than help it.
