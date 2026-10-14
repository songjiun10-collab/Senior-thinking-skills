# Office Hours: partner test

Goal: check whether a teammate can run the `office-hours` skill on a real idea and end with a design doc, without help from the author.

## Setup (5 min)

1. Clone the repo and check out `claude/model-characteristics-tuning-7jo32o`.
2. Open the project in Claude Code.
3. Start a fresh session. Don't pre-load other skills.

## Run it

Pick one idea you actually have (a tool for your team, a process change, a small product). Say: **"office hours: <your idea>"**.

Work through the phases. Answer honestly, including "I don't know". Stop when the skill saves a design doc under `docs/design/`.

Time box: 30 minutes. If it stalls, note where and stop.

## Watch for

- **Hard gate**: did it write any code or edit files outside `docs/design/`? (It shouldn't.)
- **STOP points**: did it wait for an answer at each STOP, or skip ahead?
- **Premises**: did it list 3-5 premises and let you disagree, or just accept your framing?
- **Alternatives**: did it give 2-3 real options with effort and risk, or one option dressed up as three?
- **Decision briefs**: is the `D<N>` format clear enough to answer without re-reading?
- **Design doc**: does it contain the sections in the skill, and are the open questions yours to answer?

## Feedback (copy and fill in)

```
Idea:
Total time:
Finished with a design doc? yes / no. If no, which phase stopped it:
Did it write code or touch files outside docs/design/? yes / no
Phase that felt most useful:
Phase that felt pointless or wrong:
Did it ever accept a claim you didn't make? quote it:
Did a question make you think of something new? quote it:
Would you use it again for a real decision? yes / no / with changes:
Anything unclear in the instructions:
```

Send the filled-in form to the author.
