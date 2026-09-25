> Tuned for Claude Opus 5.5. See SKILL.md for the model index.

# Design for the next reader

Making it work now and making it something someone else (or future you) can understand and change in six months are different problems.

## Interface first

Write the implementation first and you get an API that's **easy to build**. Write the interface first and you get one that's **easy to use**.

- What should the calling code look like? **Write that call site first, before anything else.**
- Is it hard to misuse? Does the argument order invite mix-ups? Can you make invalid states unrepresentable in the first place?
- Is the shape and ownership of the data crossing this boundary clear?
- A good module is deep — **a small interface hiding a lot of behavior.** If the interface is as complicated as the internals, the boundary is drawn wrong.
- **Hold this bar strictly.** Opus 5 guidance (still applicable to 5.5) notes a tendency to expand scope beyond the request; in interface design that shows up as extra flexibility, extra configuration knobs, or extra abstraction layers nobody asked for — options params "in case it's needed later," a base class for a thing that has exactly one implementation, a plugin system for two call sites. None of that makes the interface easier to use; it makes it wider than the problem. Default to the plainest shape that covers today's actual callers, not the shape that anticipates every hypothetical one.
- Principal angle: an interface used by more than one team is a promise you're making to people you'll never talk to before they build on it — design it as if you can't personally walk every caller through a breaking change later, because you won't be able to.
- Distinguished/Fellow angle: if this becomes the pattern every team in the company is expected to follow, the real test is whether it still reads as obviously correct once you're no longer the one people ask — doctrine, not tribal knowledge.
- Executive angle (CTO/VP-Eng): a design only its original author can safely extend is a hiring and retention constraint — ask whether you can staff and onboard people against it, not just whether one expert can operate it.

## The view from six months out

- Can someone tell what this does from the name and structure alone, without reading the body?
- If a requirement shifts slightly (one new field), does this structure absorb it, or does it need a rewrite? Note the difference between *this* (a structure that happens to absorb a plausible future change) and building in speculative extensibility for changes nobody has asked for yet — the first is good design, the second is scope the request didn't ask for.
- Are you using the project's existing vocabulary? A new name for an existing concept makes the next reader think there are two different things.
- Does this clash with the existing style? Even if your taste is better, **match the existing style.** Introducing a "better" pattern alongside the existing one is itself a case of adding structure nobody asked for — it leaves two ways to do the same thing instead of one.

## Label your shortcuts

If you hardcoded something, took a temporary workaround, or traded correctness for performance, **write down that you did it and why.** Code left unexplained either gets left untouched out of fear, or deleted without a thought — both are wrong outcomes. Keep the label itself plain — a short comment at the point of the shortcut, not a design-doc-length justification. The label needs to survive; it doesn't need to be built out.

## A gut check before finishing a design

If you notice yourself adding a file, a layer, a config option, or a flexibility knob that no current call site uses — stop and ask whether the six-months-out reader benefits from it, or whether it's just more surface for them to have to understand. When in doubt, cut it; it's easier to add a knob later when a second real caller shows up than to remove one that's already load-bearing for someone.
