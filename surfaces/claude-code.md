# Set up in Claude Code (terminal or desktop app)

Claude Code reads the repo directly, so there's nothing to upload. It loads the coach through `CLAUDE.md` and updates your `me/` and `debriefs/` files for you. The slash commands are the same in the terminal and in the desktop app.

1. **Get the repo.** Your `me/` files will hold your real experience, so keep your copy private.
   - On GitHub: click **Use this template**, then **Create a new repository**, and set it to **Private**.
   - Or clone it locally: `git clone https://github.com/ai-analyst-lab/interview-prep-with-ai.git`
2. **Open it in Claude Code.**
   - Terminal: `cd` into the repo folder and run `claude`.
   - Desktop app: open Claude Code and choose this folder as the project.
3. **Run the kickoff.** `/kickoff` for a live one-question-at-a-time session, or save talk-through transcripts in `me/raw/` and run `/kickoff extract`.
4. **Practice.** The commands:
   | Command | What it does |
   |---|---|
   | `/mock case --role pm` | a Practice mock (add `--mode simulate` to watch a model interview) |
   | `/drill sql windows` | short cold questions on one topic |
   | `/assess` | score one answer you paste |
   | `/debrief debriefs/inbox/<file>.md` | debrief a practice mock transcript and update the retest queue |
   | `/retest` | cold retest on what's due |
5. **Optional: SQL practice.** Follow the setup in [practice/sql/drills.md](../practice/sql/drills.md). It needs Python 3.

Try it on the example first: `/debrief examples/priya-mock-transcript.md`.

**Tip:** Claude Code reads `me/gaps.md` and `debriefs/retest-queue.md` for you. In a chat app, paste them at the start of a chat session so it picks up where you left off.

If `me/` is still the template, every command still runs, but warns that answers will be generic until you finish a kickoff session.
