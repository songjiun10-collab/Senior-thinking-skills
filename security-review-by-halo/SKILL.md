---
name: security-review-by-halo
description: Review security-sensitive code as HALO treats an untrusted model — the reviewer is a fallible monitor, so demand independent evidence, re-verify stale verdicts, check the worst case, and fail closed. Use when reviewing auth, permission, sandbox, or containment code, when trusting a verification verdict (a test pass, scanner report, or probe result), or when judging whether multiple reviews actually add assurance. Skip for ordinary feature diffs with no security surface — use security-review for the OWASP checklist pass.
---

# Security Review by Halo

A security review is itself a containment boundary — and HALO's containment experiments (songjiun10-collab/Halo) measured exactly how boundaries like it fail. The reviewer is a monitor; monitors share blind spots, go stale, and get gamed. `security-review` decides what to check in a security-sensitive diff; this skill decides how much to trust the checking itself.

## Redundancy without independence is not redundancy (E001-B, E002)

- Two reviewers who share context, training, or a reading of the code fail **together** — at equal 5% per-source error, redundant fail-closed checks went from 0.187% failure at zero correlation to 3.955% at full correlation. A second pass by the same model or the same person adds correlated assurance, not independent assurance
- Algorithm-diverse monitors still shared one held-out blind spot: ensemble TPR collapsed 94.60% → 11.42% as that family dominated the mix, while an **independent evidence channel** held 97.65%. Observed disagreement isn't proof of independent evidence
- The fix is a different **kind** of evidence, not a different reader: execute the exploit path, send the unauthorized request, replay the token — don't just re-read the diff (same evidence bar as `verify-before-claiming`)

## Verdicts go stale (E003)

- A cached verdict is only good for the state it was issued against — under state drift, stale authorization decisions fail in simulation, and a freshness window only narrows the exposure. A test pass, approval, or probe result from **before** the refactor covers the old code, not the current one — re-verify after every change the verdict was supposed to cover

## Check the worst case, not the mean (E004)

- An aggregate threshold hides a group-level failure — HALO's robust-evaluation experiment tracks `worst_group_tpr` precisely because the mean can look fine while one attack family walks through. A green suite with one untested security case is the mean lying to you; ask which case is the worst and what covers it

## Static checks degrade under adaptation (E005)

- Binary feedback (pass/block) lets an iterating author escalate evasion against a static monitor (mean +0.18 per round); re-randomizing the check didn't reliably stop it and roughly tripled outcome variance. Assume the checklist has been **seen** — vary the probes, and don't feed the author a stable oracle to iterate against

## What the code treats as authorization

- Only explicit user intent and trusted system policy can authorize — web pages, emails, tool output, and other agents' messages are **data**. Check what the diff consumes as authorization input, and that a body string like `trusted` or `approved=True` can't become an approval
- A detector's `ALLOW` is not a capability: verdicts and capabilities flow through separate paths, bound to the exact tool, args, and version, claimed before execution, expired and replay-rejected
- A success verdict can itself be a false PASS — HALO's sem_open probe reported success because a ctypes `bool()` misjudged `SEM_FAILED`. Verify the verdict's own mechanics, not just its claim (`honest-artifacts`)

## What the sandbox actually blocks (probed, not assumed)

HALO's macOS Seatbelt probes measured the boundary instead of trusting the profile: numeric MIB sysctls, process enumeration, processor-set task access, launchd access, interface/routing sockets, and home directory listing came back **blocked**, while `getmntinfo` still leaked the host mount list and volume metadata, and `mach_host_extended` still exposed kernel version, page size, and CPU info. A sandbox that "has a profile" is not a sandbox that holds — **enumerate what's still exposed, not just what's blocked**.

- A probe that couldn't run gets classified `unsupported`, not counted as blocked — `fsgetpath` used a bad ctypes fixture and was reclassified rather than counted on a broken measurement. A check that silently can't run is a hole being counted as coverage
- The OS sandbox and the app-level permission gateway cover different surfaces and fail differently — verify the layers don't share one blind spot (E002) and that neither is assumed to cover the other's gap by default

## Fail closed, price the false blocks

- An inconclusive review **blocks** — unknown tool, unexpected field, expired or replayed evidence gets rejected, not passed through
- Redundant fail-closed evidence reduces misses but raises false blocks — both costs are real, record both (the measure-before-optimizing discipline applied to safety)

- **Principal angle:** a review boundary other teams copy (a merge gate, a scanner profile) carries its blind spots with it — E001-B and E002 are the argument for putting an independent evidence channel in the pattern itself, before it's copied everywhere it's imported.
- **Distinguished/Fellow angle:** a containment claim that outlives its threat model becomes company-wide folklore — state the measured assumptions next to the claim, the way HALO's own reports do, so a reviewer in five years can check whether the boundary still matches its threat model, not just that it once passed.
- **Executive angle (CTO/VP-Eng):** the false-block/miss tradeoff is a budget and business-risk decision — over-blocking burns engineering capacity, under-blocking carries breach and regulatory cost. Worth a real risk process (audit, measured thresholds), not one reviewer's judgment call.

## Warning signs

| Thought | Reality |
|---|---|
| "Two reviews passed, so it's solid" | Correlated reviewers fail together; independence lives in the evidence, not the headcount |
| "Tests passed last week" | A verdict covers the state it was issued against, not the current one |
| "Diverse scanners caught everything" | They share blind spots; execute the exploit path |
| "The report says approved" | A body string is data; a detector's ALLOW is not a capability |
| "The sandbox profile blocks it" | The profile blocks some paths; enumerate what's still exposed |
