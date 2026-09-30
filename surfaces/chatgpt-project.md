# Set up in ChatGPT (Project or custom GPT)

Either option keeps your coach instructions and files attached. A Project is simpler. A custom GPT is handy if you want a single coach you can open from anywhere. What's available depends on your ChatGPT plan.

## Option A: a Project
1. **Create the Project.** In the ChatGPT sidebar, create a new Project called "Interview prep".
2. **Add the instructions.** Open the Project's settings and paste everything below the line in [interviewer/core-system-prompt.md](../interviewer/core-system-prompt.md) into its instructions. Fill in your target role and level.
3. **Add files.** Upload `interviewer/coaching-rules.md`, the files in `me/` (`experience-db.md`, `numbers-card.md`, `coverage-map.md`, `fixed-answers.md`, `story-matrix.md`), and the `rounds/` guides you need.
4. **Start a chat in the Project** and type `Practice screen`, `Simulate case`, `Coach technical`, or `Debrief` with a pasted practice mock transcript.
5. **Keep it current.** Replace the uploaded files when your experience database or gaps change.

## Option B: a custom GPT
1. Open the GPT builder (Explore GPTs, then Create) and switch to the Configure view.
2. Name it "Interview coach". Paste the core system prompt into the Instructions box.
3. Upload the same files as Option A under Knowledge.
4. Keep it private (only you), since the files are about you.
5. Open the GPT and type a mode to start. Update the Knowledge files when they change.

**Tip:** paste `me/gaps.md` and `debriefs/retest-queue.md` at the start of a chat session so it picks up where you left off.

**Heads-up:** ChatGPT can't edit your files. Copy new story cards, gaps, and retest items back into your repo yourself.
