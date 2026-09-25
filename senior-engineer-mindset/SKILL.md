---
name: senior-engineer-mindset
description: Router for thinking like a senior, principal, distinguished/fellow, or executive-level (CTO/VP-Eng) engineer BEFORE writing code. Picks which thinking disciplines fit the task at hand and dispatches to them. Use this proactively whenever the user asks to build a feature, choose a library/framework/database, design an API or data model, fix a bug whose cause isn't obvious, or refactor — even if they never say "design", "design review", or "senior". Skip for one-line fixes, explicitly throwaway prototypes, or when the user handed over a fully-specified plan and just wants it typed out. Bundles an optional PreToolUse/PostToolUse hook (scripts/check_ask_before_hard_change.py) that nudges toward an AskUserQuestion check-in before editing a hard-to-reverse surface.
---

# Senior + Principal + Distinguished + Executive Engineer Mindset (router)

The gap between junior and senior isn't "how well you write code" — it's **what you think about before you write it.** This skill bundles that thinking process — four stacked lenses (Senior/Principal/Distinguished/Executive), a workflow of sub-skills, and a three-track classification (Spike/Bounded/Structural) — and is tuned per model, because how much hand-holding, effort, and narration each part needs differs by tier.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 / Claude Mythos 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |
| OpenAI GPT-6 Astra | `gpt-6-astra.md` |
| OpenAI GPT-6 Sol | `gpt-6-sol.md` |
| OpenAI GPT-6 Luna | `gpt-6-luna.md` |

Read the file matching the model actually running before applying this skill. Each file is a complete, standalone rewrite covering the four-lens framing, the sub-skill and situational-pick tables, track classification, the "too simple to need a check" trap, output format, and the skip list — calibrated for that model. The hook below is not model-dependent and applies the same way regardless of which file you read.

**Running a model not listed above** (Claude Haiku 4.5, Claude Opus 5, an older generation, a different model family entirely)? `sonnet-5.md` carries the fullest general-purpose version of the underlying procedure — read that one rather than skipping this skill. Haiku 4.5 has no `effort` parameter and a 200K context window (not 1M): apply the discipline, but skip that file's effort-level and context-window specifics — they don't hold for Haiku.

## Optional: enforce with a hook

The rule that a hard-to-reverse decision gets a check-in first is mechanically catchable to a degree: `scripts/check_ask_before_hard_change.py` watches for an Edit/Write/MultiEdit targeting a path that looks like a hard-to-reverse surface (schema, migration, public API spec, dependency manifest) with no `AskUserQuestion` call in the recent window (`ASK_HOOK_WINDOW_SECONDS`, default 1800s). By default it **only warns, it doesn't block** — set `ASK_HOOK_STRICT=1` to make a hit actually block the edit.

Add to `.claude/settings.json`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write|MultiEdit",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/senior-engineer-mindset/scripts/check_ask_before_hard_change.py" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "AskUserQuestion",
        "hooks": [
          { "type": "command", "command": "python3 .claude/skills/senior-engineer-mindset/scripts/check_ask_before_hard_change.py" }
        ]
      }
    ]
  }
}
```

If your skill is installed at a different path, update the command path to match. This is a path-based heuristic, not a real understanding of what's actually hard to reverse — it can't tell a real schema change from an unrelated edit to a file that happens to live in `migrations/`, and it can't tell a dependency version bump from a comment-only edit to a manifest file. A false positive just costs a wasted nudge (advisory by default); it isn't a substitute for actually judging whether a decision is hard to reverse. Same example-level-enforcement framing as `delegate-to-subagents`'s bundled hook — not a red-team-tested CRITICAL-tier block.
