---
description: Run a mock interview round in Practice (you answer) or Simulate (watch a model interview) mode
argument-hint: "<screen|case|technical|behavioral> [--role ds|da|pm|finance|manager] [--mode practice|simulate]"
---

Run a mock interview. Arguments: $ARGUMENTS

Defaults: `--mode practice`. If `--role` is missing, use the role in `me/experience-db.md`; if none is there, ask once.
Role codes: ds = Data Scientist, da = Data Analyst, pm = Product Manager, finance = Finance Analyst, manager = add the manager questions on top of the IC role.

## Before the first question
1. Load `interviewer/core-system-prompt.md`, `interviewer/coaching-rules.md`, all of `me/`, and `rounds/<N>-<round>.md` for the round.
2. Apply the soft block from `CLAUDE.md`: if `me/` is empty or the round's topics are Missing in the coverage map, warn once, offer to fill the gap, then carry on.
3. Pick a question from the round guide's common questions and role variants. Prefer topics that are Thin in the coverage map or due in `debriefs/retest-queue.md`.

## Practice
Follow the Practice mode in the core prompt exactly: one question, wait, one pushback, wait, then the scorecard (Score, What the interviewer marks down, One correction, Stronger headline, Next question). The stronger headline uses the candidate's own stories and numbers. For Screen questions in `me/fixed-answers.md`, flag any drift from the written answer.

## Simulate
Follow the Simulate mode in the core prompt exactly: one exchange per turn (Interviewer, Candidate, Behind the answer), 5 to 7 lines, then `Type next to continue.` Build the candidate's answers from `me/experience-db.md`. Label anything else `(generic example)`.

## After the session
Offer to append weak topics to `debriefs/retest-queue.md` and new gaps to `me/gaps.md`. No em dashes.
