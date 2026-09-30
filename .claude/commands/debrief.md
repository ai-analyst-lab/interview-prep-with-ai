---
description: Debrief a practice mock transcript, save the result, and update the retest queue and gaps
argument-hint: "<path to practice mock transcript, e.g. debriefs/inbox/2026-10-01-case.md>"
---

Debrief a practice mock. File: $ARGUMENTS

1. Read the transcript. If no file is given, list `debriefs/inbox/` and ask which one. This is for practice mocks only (a friend, peer, coach, or AI voice mode).
2. Load the coach files and all of `me/`. Apply the soft block from `CLAUDE.md`.
3. Run Debrief mode from `interviewer/core-system-prompt.md`, using `debriefs/TEMPLATE.md` as the layout:
   - Verdict, with a score out of 10 per question
   - Up to 3 weak lines, quoted exactly as said, each with a fixed version built from `me/`
   - Patterns (buried result, no number, "we" not "I", underselling, rambling, folding under pushback)
   - Answers to fix
   - Add to retest queue
   - Single biggest fix
4. Save it to `debriefs/YYYY-MM-DD-<slug>.md` (today's date, slug from the round or topic).
5. Append each retest topic as a new row in `debriefs/retest-queue.md`: topic, source (the debrief file), date added (today), correct cold count `0/3`, last asked blank.
6. Append new gaps to `me/gaps.md` (missing numbers, stories that didn't hold up on a follow-up).
7. If a pattern repeats across debriefs, suggest a new line for "My own rules" in `interviewer/coaching-rules.md`. Don't add it without asking.

Show the debrief in chat, then list the files you changed. See `examples/priya-mock-debrief.md` for the expected result. No em dashes.
