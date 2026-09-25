---
name: verifiability-first
description: Turn the task into something verifiable and declare the success criterion before seeing results. Use when the request is vague about "done" ("make it work", "improve this"), when writing tests, when fixing a bug (write the failing reproduction first), or when comparing two approaches. Critical before any measurement or benchmark, where deciding the bar after seeing the numbers guarantees a "success".
---

This skill has a full, standalone version tuned for each current model line. Pick the file matching the model actually running.

| Model | File |
|---|---|
| Claude Opus 5.5 | opus-5-5.md |
| Claude Fable 5.1 | fable-5-1.md |
| Claude Sonnet 5 | sonnet-5.md |

Read the file matching the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
