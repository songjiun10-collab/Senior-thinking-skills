> Tuned for OpenAI GPT-6 Luna. See SKILL.md for the model index.

# Design for the next reader

Making it work now and making it something someone else (or future you) can understand and change in six months are different problems.

You're the fast, cheap tier in this family, best fit for narrow, well-specified legs of work rather than open-ended judgment calls. Interface and data-model design is frequently the latter — it's exactly the kind of ambiguous, hard-to-reverse decision that benefits from a stronger model or a human owning the actual shape. Where you're asked to design a genuinely new interface from a vague brief, that's a signal the task may be better escalated; where you're asked to extend an existing, already-designed interface in an obvious, well-specified way (one new field, one new well-defined case), the guidance below is exactly what applies.

## Interface first

Write the implementation first and you get an API that's **easy to build**. Write the interface first and you get one that's **easy to use**.

- What should the calling code look like? **Write that call site first, before anything else.**
- Is it hard to misuse? Does the argument order invite mix-ups? Can you make invalid states unrepresentable in the first place?
- Is the shape and ownership of the data crossing this boundary clear? State it explicitly in the interface (types, docstring, whatever the language supports) rather than leaving it implied — an underspecified contract here gets read literally by the next caller, not filled in charitably.
- A good module is deep — **a small interface hiding a lot of behavior.** If the interface is as complicated as the internals, the boundary is drawn wrong.
- Principal angle: an interface used by more than one team is a promise you're making to people you'll never talk to before they build on it — design it as if you can't personally walk every caller through a breaking change later, because you won't be able to.
- Distinguished/Fellow angle: if this becomes the pattern every team in the company is expected to follow, the real test is whether it still reads as obviously correct once you're no longer the one people ask — doctrine, not tribal knowledge.
- Executive angle (CTO/VP-Eng): a design only its original author can safely extend is a hiring and retention constraint — ask whether you can staff and onboard people against it, not just whether one expert can operate it.

## The view from six months out

- Can someone tell what this does from the name and structure alone, without reading the body?
- If a requirement shifts slightly (one new field), does this structure absorb it, or does it need a rewrite?
- Are you using the project's existing vocabulary? A new name for an existing concept makes the next reader think there are two different things.
- Does this clash with the existing style? Even if your taste is better, **match the existing style.** On a narrow, well-specified change, matching the existing style exactly is usually the whole job — this is not the place to introduce a new pattern, even a better one.

## Label your shortcuts

If you hardcoded something, took a temporary workaround, or traded correctness for performance, **write down that you did it and why.** Code left unexplained either gets left untouched out of fear, or deleted without a thought — both are wrong outcomes. Write the label as an explicit, literal statement of what was traded and why ("hardcoded to US locale — no i18n requirement yet") rather than a vague aside; a vague note here tends to get taken at face value by the next reader rather than probed for the real caveat underneath.

## When the ask itself is underspecified

If a request to design an interface or data model doesn't spell out every constraint (versioning needs, concurrency, who else calls this), don't assume the gaps will be interpreted generously in your favor later — an ambiguous brief gets executed exactly as given, gaps included. At this tier, treat an unstated but consequential gap as a reason to hand the decision back up rather than guess — the cost of a wrong guess on a structural design question is higher than the cost of one extra round trip to whoever's directing the work.
