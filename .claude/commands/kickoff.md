---
description: Build your experience database, live (one question at a time) or by extracting from transcripts in me/raw/
argument-hint: "[session N | extract]"
---

Run the kickoff. Arguments: $ARGUMENTS

Read first: `kickoff/README.md`, the matching `kickoff/session-*.md` guide, and the current files in `me/`. Use the `kickoff` skill.

## No argument, or `session N`: live kickoff
- Follow `kickoff/live-kickoff-prompt.md`. If no session is given, pick the first one the coverage map shows as Missing or Thin (start at session 1 if `me/` is still the template).
- Ask ONE question at a time from the session guide, then wait. Relaxed tone, like a curious friend.
- Follow up on anything vague or missing a number: "roughly how many?", "what changed after that?", "what did you do yourself?"
- Don't score or coach during the kickoff. Just draw the stories out.
- "pause" means stop and wait. "next area" means move on. "build it" means write the files now.
- Only ask session 5 questions if the candidate is a manager or interviewing for one.

## `extract`: from transcripts
- Read every `me/raw/*.md` (and `.txt`). If there are none, say so and point to Option A in `kickoff/README.md`.
- Apply `kickoff/extraction-prompt.md` exactly.

## Write the results (both paths)
- `me/experience-db.md`: story cards in the extraction format. Add new cards; update existing ones; never delete the candidate's words.
- `me/numbers-card.md`: 8 to 12 numbers with one line of context each.
- `me/coverage-map.md`: common questions for the four rounds, marked Strong, Thin, or Missing, with the story that covers each.
- `me/story-matrix.md`: one row per story, marked against the question themes.
- `me/gaps.md`: every `[NEED NUMBER]` and `[NEED DETAIL]`, plus the follow-up questions.

Never invent a fact. Mark anything you composed as `(suggested)`. No em dashes.

Finish with: what you added, the 3 biggest gaps, and "Say go and I'll ask the first follow-up."
