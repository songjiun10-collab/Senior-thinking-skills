> Tuned for Claude Fable 5.1 (and Claude Mythos 5.1, which shares its Anthropic prompting guide). See SKILL.md for the model index.

# Design for the next reader

Making it work now and making it something someone else (or future you) can understand and change in six months are different problems.

## Interface first

Write the implementation first and you get an API that's **easy to build**. Write the interface first and you get one that's **easy to use**. Work from that goal — "what should the calling code look like" — rather than a fixed sequence of design steps; your own reasoning about the right shape for a boundary will often get further than a prescriptive checklist would.

- Write the call site first, before anything else, and let the interface follow from it.
- Is it hard to misuse? Does the argument order invite mix-ups? Can you make invalid states unrepresentable in the first place?
- Is the shape and ownership of the data crossing this boundary clear?
- A good module is deep — **a small interface hiding a lot of behavior.** If the interface is as complicated as the internals, the boundary is drawn wrong.
- Principal angle: an interface used by more than one team is a promise you're making to people you'll never talk to before they build on it — design it as if you can't personally walk every caller through a breaking change later, because you won't be able to.
- Distinguished/Fellow angle: if this becomes the pattern every team in the company is expected to follow, the real test is whether it still reads as obviously correct once you're no longer the one people ask — doctrine, not tribal knowledge.
- Executive angle (CTO/VP-Eng): a design only its original author can safely extend is a hiring and retention constraint — ask whether you can staff and onboard people against it, not just whether one expert can operate it.

## The view from six months out

- Can someone tell what this does from the name and structure alone, without reading the body?
- If a requirement shifts slightly (one new field), does this structure absorb it, or does it need a rewrite?
- Are you using the project's existing vocabulary? A new name for an existing concept makes the next reader think there are two different things.
- Does this clash with the existing style? Even if your taste is better, **match the existing style.**

## Label your shortcuts

If you hardcoded something, took a temporary workaround, or traded correctness for performance, **write down that you did it and why.** Code left unexplained either gets left untouched out of fear, or deleted without a thought — both are wrong outcomes.

## Working through a design on your own

On a genuinely long design pass — a module with several interacting pieces, a boundary that touches many callers — you can carry that horizon well without losing the thread. The gap is visibility: you tend to work through it quietly rather than narrating each decision as you make it, so whoever's waiting on the design sees little until it's essentially finished. If someone downstream needs to see the interface take shape — a reviewer who wants to weigh in on the call-site design before it's locked in, not just after — say so explicitly; left to your own judgment you'll default to handing over the finished shape.

When you do write it up for a reader, keep the writeup itself light on scaffolding — you already favor plainer formatting by default, which suits this: the interface should carry its own clarity, not lean on headers and bullets to compensate for a boundary that isn't actually clear from its call site.
