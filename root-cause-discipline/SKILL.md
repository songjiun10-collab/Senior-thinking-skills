---
name: root-cause-discipline
description: Find the actual cause instead of suppressing the symptom. Use when fixing any bug whose cause isn't immediately obvious, investigating a performance regression, or about to add a defensive check (null guard, retry, try/except) to make an error go away. Starts by checking whether the problem is already solved somewhere before digging.
---

# Root Cause Discipline

## Iron rule

```
Never propose a fix without a root-cause investigation.
```

Just suppressing the symptom is a failure. **The more urgent it feels, the more this discipline matters** — systematic digging is actually faster than guess-and-revert.

## 0. First: is this already solved

The most expensive code is code that re-implements something that already exists. **The moment right before you dig deep is the moment to check.**

- Has this already been fixed on another branch or in a recent commit? (`git log <path>`)
- Does a similar function or module already exist in the codebase?
- Does the standard library or an existing dependency already provide this?
- The instant you're about to reinstall packages, A/B a library version, or start walking back through commit history — spend one minute first. Spending hours reinventing an answer that already exists is common, and the reinvented version is usually explained less accurately than the original.

## 1. Cause, not symptom — investigation phase

**Read first.** Read the error message and stack trace all the way through. The answer is often right there. Don't skip past line numbers, file paths, error codes.

**Reproduce it.** Does it reproduce reliably? What's the exact procedure? Every time? If it doesn't reproduce, **gather more data — don't guess.**

**Look at recent changes.** What changed that could cause this? Diff, recent commits, new dependencies, config changes, environment differences.

**If multiple layers are involved, instrument first.** (structures like CI → build → signing, or API → service → DB)

```
At each component boundary:
  - Log what comes in
  - Log what goes out
  - Confirm environment/config is actually being passed through

Run it once to get evidence of "which layer breaks"
→ Then dig into only that layer
```

Start fixing without knowing where it breaks, and you end up fixing three layers that were never broken.

## 1-2. Pattern analysis — before fixing

- **Find a working example.** Is there similar code in the same codebase that works fine?
- If a reference implementation exists, **read it in full — don't skim.**
- **List every difference**, no matter how trivial it looks. The thing dismissed as "shouldn't matter" is often the cause.

## 1-3. One hypothesis at a time

- State it **explicitly**: "X is the cause, because Y." A vague hypothesis can't be tested.
- Make the **smallest possible change** to test the hypothesis. One variable at a time.
- Doesn't work → form a new hypothesis. **Don't stack another fix on top of the last one.**
- Don't know something → say "I don't know X." Don't fake understanding.

## 1-4. Cause, not symptom

The most common failure is suppressing the symptom. Before adding a null check, ask **where the null came from** in the first place.

- **Where** was this value created in a bad state? Trace back to that point.
- Could the same root cause be producing **other latent bugs** already?
- Defensive code is sometimes the right call — but only as a decision made **after** you know the cause.

## 2. Evidence, not assumption

Assumptions about codebase behavior, library behavior, or an error's cause are frequently wrong. If confirming is cheap, confirm it.

- Did you **confirm** this function/library actually behaves this way, or did you **assume** it does?
- Did you actually read the file, or guess its contents from the name?
- Did you actually run it before saying "fixed" or "works"?
- **Make every claim checkable**: name the file, show the number, quote the command you actually ran. A claim you can't back is worse than saying you don't know.

## 3. After the fix

- Write the failing reproduction test **first**; prove the fix by making it pass.
- **One fix at a time.** Don't slip in "while I'm here" improvements or refactors.
- Confirm no other tests broke.

## 4. Three failures means suspect the structure

Count your attempts when a fix doesn't land.

- **Under 3** → go back to step 1, re-analyze with what you just learned.
- **3 or more** → stop. Don't attempt a fourth fix.

Past three failures, it's likely not the hypothesis that's wrong — it's the **structure**. Signs:

- Each fix pops up a new problem somewhere else
- Fixing it properly would need a "large refactor"
- A fix creates new symptoms elsewhere

At this point, ask the root question: is this structure even right to begin with? Are you holding onto it out of inertia? **Talk to a person before** attempting the next fix. Principal angle: if the root cause lives in shared or upstream code, other teams may be hitting the same bug blind — fixing it once at the shared layer is worth more than patching every call site that happened to notice.

**Distinguished/Fellow angle:** if the root cause lives in a dependency or pattern used company-wide (or upstream in an open-source project), fixing and publishing it there prevents the next org — not just the next team — from rediscovering it after the people who understood it have moved on.

**Executive angle (CTO/VP-Eng):** if three teams have independently hit the same root cause, that's a signal the org is understaffed or misstructured for that layer, not just a bug to fix — worth a headcount or ownership conversation, not another patch.

## Warning signs — any of these means go back to step 1

- "Let's just fix it fast and investigate later"
- "Let's just try changing X and see"
- "Change a few things and run the tests"
- "Skip the test, just check it manually"
- "It's probably X, let's fix that"
- "I don't fully understand it, but this should work"
- Listing solutions before tracing the data flow
- **Already failed twice, and thinking "just once more"**

## Signals from the person you're working with

These phrases mean the approach is wrong. Stop and go back to step 1.

- "Is that actually true?" → you assumed without confirming
- "Can you show me that?" → you should have been collecting evidence
- "Stop guessing" → you're proposing fixes without understanding
- "Think again" → you need to ask about the cause, not the symptom
- "Are you stuck?" (frustrated) → the current approach isn't working

## Blocking rationalizations

| Excuse | Reality |
|---|---|
| "It's a simple problem, skip the process" | Simple bugs have root causes too. If it's simple, the process finishes fast |
| "No time for process, this is urgent" | Systematic debugging is **faster** than guess-and-check |
| "Let's try this first, investigate after" | The first fix sets the pattern. Do it right from the start |
