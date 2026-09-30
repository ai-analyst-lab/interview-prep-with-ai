---
description: Rapid-fire drill on one topic, short questions, scored one at a time
argument-hint: "<topic, e.g. sql windows | power and MDE | metric definition | fixed answers | variance to plan> [--n 5]"
---

Run a drill. Arguments: $ARGUMENTS

A drill is shorter than a mock: quick questions on one topic, answered cold.

1. Load the coach files, `me/`, and the round guide that covers the topic. Apply the soft block from `CLAUDE.md`.
2. Ask ONE short question at a time (default 5 questions). Wait for the answer. No hints.
3. After each answer, give a 3-line score: **Score X/10**, **The miss** (one line), **Say it like this** (one line, headline first, with a number from `me/` where it fits).
4. If the topic is SQL, use `practice/sql/drills.md` and the tables in `practice/sql/seed_db.py`. Ask the candidate to write the query without running it, then check it against `practice/sql/answers.sql`. Suggest `python practice/sql/q.py -f <file>` to run it afterward.
5. If the topic is `fixed answers`, ask the questions in `me/fixed-answers.md` and flag any drift from the written version.
6. At the end: a one-line summary, the single biggest fix, and offer to add any topic scored under 7 to `debriefs/retest-queue.md`.

Never mark a topic learned because you explained it. No em dashes.
