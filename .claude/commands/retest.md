---
description: Cold retest on topics due in the retest queue; 3 correct on 3 separate days marks a topic learned
argument-hint: "[--n 3]"
---

Run a cold retest. Arguments: $ARGUMENTS

1. Read `debriefs/retest-queue.md`. A topic is due if its count is under 3/3 and it was not already asked today. Oldest "last asked" first, blanks first of all. Default 3 topics.
2. If nothing is due, say so and suggest `/mock` on a Thin topic from `me/coverage-map.md`.
3. For each due topic, ask ONE question cold. No reminder of the answer, no hints, no reading the old debrief aloud. Wait.
4. Score it with the five dimensions. Correct means a 7/10 or better with the key point right.
5. Update the row:
   - Correct: add 1 to the count (for example `1/3` to `2/3`) and set "last asked" to today.
   - Not correct: set the count back to `0/3` and set "last asked" to today. Give the one-line fix.
   - Only one correct answer per topic per day counts. Same-day repeats don't move the count.
6. At `3/3` (three correct answers on three different days), move the row to the Learned section at the bottom of the file.
7. End with: topics asked, results, what's due next time.

Never mark a topic learned because you explained it. No em dashes.
