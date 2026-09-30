# Analytics Interview Prep with AI

An AI interview coach for data science, analytics, product, and finance roles. It builds your answers from **your** experience, not from a textbook.

Generic AI gives generic answers. So you start by talking through your own work. The AI turns that into an experience database: your stories, your numbers, and a map of which questions you can already answer. After that, every mock question, model answer, and score is built from your real work.

Works in Claude.ai, ChatGPT, and Claude Code. Nothing to install unless you want the SQL practice.

## The loop
1. **Kickoff (once, about 2 hours).** Talk through your experience in four short sessions. The AI builds `me/experience-db.md`, `me/numbers-card.md`, and `me/coverage-map.md`.
2. **Practice or Simulate (daily).** In Practice, you answer and the AI pushes back once, then scores you. In Simulate, you watch a model interview built from your own stories, one exchange at a time.
3. **Record your practice mocks and debrief them.** Do a practice mock with a friend, a peer, a coach, or AI voice mode. Save the transcript and run Debrief. You get your weak lines quoted, fixed versions, and a retest list.
4. **Cold retest.** A topic is learned when you answer it correctly, cold, 3 times on 3 different days. Not when you've read the answer.

## 5-minute quickstart
1. Open Claude.ai or ChatGPT and start a new chat (or a Project, see below).
2. Paste everything below the line in [interviewer/core-system-prompt.md](interviewer/core-system-prompt.md).
3. Fill in your target role and level when it asks.
4. Type `Practice` and pick a round: Screen, Case, Technical, or Behavioral.
5. Answer the question. Take the pushback. Read the scorecard.

Using Claude Code? Click **Use this template** to make your own private copy (your `me/` files will hold your real experience), or clone it:
```
git clone https://github.com/ai-analyst-lab/interview-prep-with-ai.git
```
Then see [surfaces/claude-code.md](surfaces/claude-code.md).

Your first answers will be generic. That's expected. Run the [kickoff](kickoff/README.md) next, and the coach starts using your real stories.

Want to see what good looks like first? Read the Priya examples in [examples/](examples/). Priya is a fictional senior data analyst at Fernly, a fictional meal-kit app.

## Pick your role
The prompt asks for your role and adjusts the questions. Each round guide in [rounds/](rounds/) has role variants.

| Role | Focus |
|---|---|
| Data Scientist | experiment design, power, metric drops, causal questions, modeling judgment |
| Data Analyst | SQL (joins, windows, grain), metric definitions, dashboards, diagnosing drops |
| Product Manager | success metrics, launch decisions, trade-offs, estimation |
| Finance Analyst | variance to plan, forecast logic, unit economics |
| Manager (add-on) | hiring, team leadership, prioritization, disagreement. Also run kickoff session 5 |

## Pick your app
| App | Best for | Setup |
|---|---|---|
| Claude.ai Project | keeping your files attached to every chat | [surfaces/claude-ai-project.md](surfaces/claude-ai-project.md) |
| ChatGPT Project or custom GPT | same, in ChatGPT | [surfaces/chatgpt-project.md](surfaces/chatgpt-project.md) |
| Claude Code (terminal or desktop app) | slash commands, files updated for you | [surfaces/claude-code.md](surfaces/claude-code.md) |
| Voice mode (ChatGPT or Claude) | spoken practice mocks | [surfaces/voice-mock.md](surfaces/voice-mock.md) |

## What's in here
```
interviewer/     the coach: core system prompt (4 modes) and coaching rules
kickoff/         question guides for the 4 kickoff sessions (+ a manager session)
rounds/          one guide per round: what it tests, common questions, rubric
me/              your files: experience database, numbers card, coverage map, fixed answers, gaps
prompts/         copy-paste prompts for any chat app
surfaces/        setup guides for each app
debriefs/        debrief template, retest queue, inbox/ for practice mock transcripts
practice/sql/    a synthetic practice database and 10 SQL drills with checked answers
take-home/       playbook, decisions log, and risk list for take-home assignments
examples/        Priya: a kickoff transcript, her experience database, a practice mock, its debrief
.claude/         slash commands, an interviewer agent, and skills for Claude Code
```

## Privacy
- Your raw kickoff transcripts go in `me/raw/`, and practice mock transcripts go in `debriefs/inbox/`. Both are gitignored, so they are never pushed.
- If you fork this repo, make it private before you fill in `me/`. Those files are about you.
- Use ranges or percentages for numbers your employer considers confidential. Never paste confidential documents or customer data.
- Record your practice mocks, with the other person's consent.

## License
MIT. See [LICENSE](LICENSE).

From AI Analyst Lab (aianalystlab.ai)
