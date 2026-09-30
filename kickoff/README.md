# Kickoff: build your experience database

Generic AI gives generic answers. Before your first mock, spend about two hours talking through your own experience. The AI turns what you say into an **experience database**: your stories, your numbers, and a map of which interview questions you can already answer well.

After that, every mock question, model answer, and score is built from your real work instead of a textbook.

## Why talk instead of write
- You remember more when you talk casually than when you try to write a polished answer.
- You undersell less. People describe their work as bigger and more accurately when they are just explaining it to someone, not "interviewing".
- You don't need to structure anything. Ramble. Go on tangents. The AI does the structuring afterward.

## The sessions (about 30 minutes each)
| Session | Topic | Guide |
|---|---|---|
| 1 | Your work and scope | [session-1-work-and-scope.md](session-1-work-and-scope.md) |
| 2 | Your best projects | [session-2-best-projects.md](session-2-best-projects.md) |
| 3 | Working with people | [session-3-working-with-people.md](session-3-working-with-people.md) |
| 4 | Mistakes and growth | [session-4-mistakes-and-growth.md](session-4-mistakes-and-growth.md) |
| 5 (managers only) | Leading a team | [session-5-managers.md](session-5-managers.md) |

Do one session a day, or all four in a weekend. Order doesn't matter much, but session 2 gives you the most material.

## Two ways to do it

**Option A: talk to yourself with a note taker (recommended)**
1. Open any note taker or recorder: Otter, Wispr Flow, Granola, your phone's voice memos, or the voice mode in ChatGPT or Claude.
2. Read each question in the session guide out loud, then just talk. Aim for 3 to 5 minutes per question.
3. Export the transcript and save it as `me/raw/session-N.md` (or paste it into your chat app).
4. Run the extraction: `/kickoff extract` in Claude Code, or paste the [extraction prompt](extraction-prompt.md) into any chat app along with your transcript.

**Option B: let the AI interview you**
Run `/kickoff` in Claude Code, or paste the [live kickoff prompt](live-kickoff-prompt.md) into any chat app. The AI asks one question at a time, in a relaxed tone, follows up on the interesting parts, and builds the database as you go.

## What you get
- `me/experience-db.md`: one story card per project or situation, with the facts, numbers, and which questions it answers
- `me/numbers-card.md`: the 8 to 12 numbers you should be able to say without thinking
- `me/coverage-map.md`: the common questions for each round, marked strong, thin, or missing
- A short list of follow-up questions for the gaps

## Rules the AI follows
- It never invents a detail. Missing facts show up as `[NEED NUMBER]` or `[NEED DETAIL]`.
- It keeps your words where they are good, and marks anything it composed as a suggestion.
- Your raw transcripts stay in `me/raw/`, which is gitignored so they never get pushed.

## Keep it safe
- Use ranges or percentages for numbers your employer would consider confidential ("grew conversion by about 15%" rather than exact revenue).
- Never paste confidential documents, customer data, or anything under NDA.
