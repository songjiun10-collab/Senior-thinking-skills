---
name: honest-artifacts
description: Make outputs honest and re-derivable. Use when committing constants, thresholds, or tuned parameters; when reporting a number or a benchmark result; when a result came from a manual one-off process; or when optimizing against a metric. Also use when tempted to present an estimate as if it were verified.
---

# Honest Artifacts

This skill's guidance is calibrated per model. Read the file matching the model you're running as before applying it.

| Model | File |
|---|---|
| Claude Opus 5.5 | `opus-5-5.md` |
| Claude Fable 5.1 | `fable-5-1.md` |
| Claude Sonnet 5 | `sonnet-5.md` |

Read whichever file matches the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
