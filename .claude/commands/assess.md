---
description: Score one answer (pasted or from a file) on the 5 dimensions and return the fixed scorecard
argument-hint: "<paste the question and your answer, or a file path> [--round screen|case|technical|behavioral]"
---

Assess an answer. Input: $ARGUMENTS

Use the `interview-assessor` skill.

1. If the input is a file path, read it. If the question is missing, ask for it once.
2. Load `me/` and the matching `rounds/` guide. Apply the soft block from `CLAUDE.md`.
3. Score on the five dimensions from the core prompt: correct, headline first, quantified, applied, crisp.
4. Return the fixed scorecard from `interviewer/core-system-prompt.md`: Score, What the interviewer marks down, One correction, Stronger headline, Next question.
5. The stronger headline must use the candidate's own stories and numbers from `me/`. If the needed number is missing, write `[NEED NUMBER]` and add it to `me/gaps.md`.

No flattery. No em dashes.
