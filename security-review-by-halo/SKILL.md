---
name: security-review-by-halo
description: Review security-sensitive code as HALO treats an untrusted model — the reviewer is a fallible monitor, so demand independent evidence, re-verify stale verdicts, check the worst case, and fail closed. Use when reviewing auth, permission, sandbox, or containment code, when trusting a verification verdict (a test pass, scanner report, or probe result), or when judging whether multiple reviews actually add assurance. Skip for ordinary feature diffs with no security surface — use security-review for the OWASP checklist pass.
---

This skill has a full, standalone version tuned for each current model line. Pick the file matching the model actually running this review.

| Model | File |
|---|---|
| Claude Opus 5.5 | opus-5-5.md |
| Claude Fable 5.1 | fable-5-1.md |
| Claude Sonnet 5 | sonnet-5.md |

Read the file matching the model actually running before applying this skill.

**Running something else** (Haiku, an older Opus/Sonnet/Fable generation, or a non-Claude agent that installed this skill bundle)? None of the three files above is tuned for you, but `sonnet-5.md` carries the full underlying procedure with the fewest model-specific assumptions layered on — read that one as the general-purpose default rather than skipping this skill.
