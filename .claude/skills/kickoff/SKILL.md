---
name: kickoff
description: Build the candidate's experience database (story cards, numbers card, coverage map, story matrix, gaps) from a live one-question-at-a-time conversation or from talk-through transcripts in me/raw/. Use for /kickoff and whenever the coverage map shows a gap to fill.
---

# Kickoff: build the experience database

People recall more and undersell less when they talk casually. Your job is to draw the stories out, then do the structuring yourself.

## Sources
- Question guides: `kickoff/session-1-work-and-scope.md` through `kickoff/session-5-managers.md` (session 5 only for managers)
- Live mode rules: `kickoff/live-kickoff-prompt.md`
- Extraction rules and output format: `kickoff/extraction-prompt.md`
- Worked example: `examples/priya-kickoff-transcript.md` to `examples/priya-experience-db.md`

## Live mode
1. Ask ONE question at a time. Wait.
2. Relaxed tone. Follow up on anything vague or missing a number: "roughly how many?", "what did you do yourself?", "what changed after that?"
3. Don't score, coach, or correct during the kickoff.
4. Respect "pause", "next area", and "build it".

## Extract mode
1. Read `me/raw/*`. Treat it as private: don't quote long passages back.
2. Apply `kickoff/extraction-prompt.md` exactly.

## Output files
| File | Contents |
|---|---|
| `me/experience-db.md` | Story cards: Title, Situation, What I did, Result, Headline, Answers questions like, Likely follow-ups, Undersold (if any) |
| `me/numbers-card.md` | 8 to 12 numbers with one line of context |
| `me/coverage-map.md` | Common questions per round, Strong / Thin / Missing, with the covering story |
| `me/story-matrix.md` | Stories as rows, question themes as columns |
| `me/gaps.md` | Every `[NEED NUMBER]` and `[NEED DETAIL]`, plus follow-up questions, most important first |

Merge into existing files. Never delete the candidate's words.

## Rules
- Use only facts the candidate gave. Never invent a project, number, title, team size, or result.
- Missing facts are `[NEED NUMBER]` or `[NEED DETAIL]`. Anything you composed is marked `(suggested)`.
- Flag underselling ("just", "only", "helped with", "small project") and show the stronger, still-true version.
- Remind the candidate to use ranges for confidential numbers.
- No em dashes.
- End with the 3 biggest gaps and offer to ask the first follow-up.
