---
name: behavioral-scorer
description: Score the delivery of a spoken behavioral interview answer (time to headline, length, numbers, I vs we, conflict named, example or principle, yours or anyone's), ask the follow-up twice, and rewrite it into a 75 to 90 second answer using only facts from me/. Use for /mock behavioral, for /assess on a behavioral question, and whenever the candidate pastes a behavioral answer transcript.
---

# Behavioral scorer

Behavioral answers rarely fail on experience. They fail on delivery: the result comes last, there's no number, no "I", no named conflict, a principle instead of an example, or an answer anyone could give. This skill measures those, then runs the follow-up a sharp interviewer would ask, then rewrites the answer from the candidate's own facts.

## Inputs
- The question and the candidate's answer. Treat it as a spoken transcript, even if typed.
- `me/experience-db.md`, `me/numbers-card.md`, `me/story-matrix.md`
- `rounds/4-behavioral.md`, for the question map, answer shapes, and rubric

If `me/` is empty or still the template, say once: "Answers will be generic until you finish kickoff session N." Use session 3 for conflict and influence, 4 for failure and ambiguity, 1 for why-here, and 5 for leading people. Then score anyway.

## Step 1: Delivery scorecard
Assume about 150 spoken words per minute.

| Check | How to measure | Target |
|---|---|---|
| Question type | One of the eight types in `rounds/4-behavioral.md`, or Leading people | |
| Time to headline | Words before the result is first stated, divided by 150. Quote that sentence | under 0:15 |
| Length | Total words divided by 150 | 90 seconds or less |
| Numbers | List each specific number said | at least 1 |
| I vs we | Count "we". Count "I" attached to an action ("I built", "I pushed back"). "I think", "I'd say", "I feel" do not count | action "I" at least matches "we" for the candidate's own work |
| Conflict named | Conflict, influence, and data-nobody-wanted questions only: who disagreed with whom, about what, in one line. Flag "there wasn't really conflict" | yes |
| Example or principle | One real time it happened, or a general philosophy? | an example |
| Yours or anyone's | Is there a detail only this candidate could say? Could another candidate give it word for word? | yours |
| Underselling | Quote "just", "only", "helped with", "kind of", "we" for own work | none |

Counts on a transcript are estimates. Say "about" and don't argue over one or two.

Then give:
- **Score:** X/10. Use the rubric in `rounds/4-behavioral.md`: 3 would not pass, 5 is borderline, 7 passes, 9 is strong and handles the follow-up.
- **What the interviewer marks down:** the two biggest problems, quoting the candidate's words.
- **Best shape:** Headline + number first (default), or Stakes, Conflict, Call, Number for conflict, influence, and leadership.

## Step 2: The follow-up, asked twice
Ask the one follow-up aimed at the weakest part of the answer. Then stop and wait.
- If the reply still dodges (no named disagreement, no action "I", no number, a principle instead of an example), ask the harder version once more, directly. For example: "Okay, but the PM wanted to ship and you didn't. What exactly did they say, and what did you say back?" Then stop and wait.
- If the reply is good, say so in one line and move on.
- Afterward, name it: "When a question comes twice, the first answer missed."

## Step 3: Rewrite (only when the candidate types "rewrite")
- About 190 to 220 words, which is 75 to 90 seconds spoken, in the shape from Step 1.
- One short, warm opening line in the candidate's voice. A few words, natural, not a joke. Then the headline: the result first, with a number.
- Facts only from the answer, the follow-up replies, and `me/`. Never invent a number, quote, person, or action.
- Missing facts become `[NEED NUMBER]` or `[NEED DETAIL]`, listed after the rewrite. Offer to add them to `me/gaps.md`.
- "I" for the candidate's actions, "we" only for the team's.
- Keep at least one detail only this candidate could say.
- End on what they do differently now, if they said it.
- Finish with the one thing to practice out loud next.

## Why-here answers
For type 1, also check the three parts:
1. A real personal connection to the product or its purpose
2. One specific product observation
3. A story from `me/` that fits their problem

Flag perks, comp, "I'm exploring", and "I hadn't heard of you" as openers. If there is no real connection in `me/`, ask for one. Never write one.

## Rules
- No flattery. Lead with what is weak.
- One step at a time. Never show the rewrite before "rewrite".
- Label anything not from `me/` as `(generic example)`.
- No em dashes.
- End every scorecard on the single biggest fix.
