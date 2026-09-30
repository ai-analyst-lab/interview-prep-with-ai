# Set up in a Claude.ai Project

A Project keeps your coach instructions and your files attached to every chat, so you don't paste them each time.

1. **Create the Project.** In Claude.ai, open Projects and create a new one. Name it something like "Interview prep".
2. **Add the instructions.** Open the Project's instructions and paste everything below the line in [interviewer/core-system-prompt.md](../interviewer/core-system-prompt.md). Fill in your target role and level at the top.
3. **Upload your files to the Project knowledge.**
   - `interviewer/coaching-rules.md`
   - `me/experience-db.md`, `me/numbers-card.md`, `me/coverage-map.md`, `me/fixed-answers.md`, `me/story-matrix.md`
   - the `rounds/` guide for the round you're practicing (or all four)
   - No experience database yet? Start a chat in the Project and paste [kickoff/live-kickoff-prompt.md](../kickoff/live-kickoff-prompt.md) to build one.
4. **Start a chat in the Project** and type `Practice case` (or `Simulate behavioral`, `Coach technical`, `Debrief` plus a pasted practice mock transcript).
5. **Keep it current.** When your experience database, gaps, or retest queue change, replace the old file in the Project knowledge with the new one. Uploaded files don't update themselves.

**Tip:** paste `me/gaps.md` and `debriefs/retest-queue.md` at the start of a chat session so it picks up where you left off.

**Heads-up:** a chat app can't edit your files. When it gives you new story cards or retest items, copy them into your `me/` and `debriefs/` files yourself.
