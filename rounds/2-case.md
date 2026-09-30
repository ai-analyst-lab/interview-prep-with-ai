# Round 2: Case (product, analytics, or business case, including take-homes)

## What it really tests
- **Structure:** can you break a vague problem into parts that you can actually check?
- **A decision:** do you end with a recommendation, not a list of things to look at?
- **Judgment:** which part do you check first, and why?
- **Metrics:** do you name a specific metric and how you'd define it?

The interviewer does not want the "right" framework. They want to see how you think when the answer isn't obvious, and whether you land somewhere.

## How people fail
What hiring managers see most often:
- **Framework recital.** Listing every possible cause ("could be tracking, product, marketing, competitors, seasonality") with no order and no hypothesis.
- **Process before point of view.** "First I'd understand the data" as the opening line.
- **No metric.** Talking about "engagement" without saying which number.
- **No recommendation.** Running out of time before saying what you'd do.
- **Folding under pushback.** The interviewer says "it's just seasonal" and the candidate agrees instead of saying how to check.

## Common question types
1. **Diagnose a metric drop.** "Weekly active users dropped 8% last week. Walk me through it."
2. **Measure success.** "We launched a new onboarding flow. How would you know if it worked?"
3. **Launch or not.** "The test shows conversion up 3% but retention down 1%. Do we ship?"
4. **Improve a metric.** "How would you increase repeat purchases?"
5. **Sizing and estimation.** "How many meal kits are sold in a US city in a week?" or "What's the revenue opportunity of a new tier?"
6. **Finance variance vs plan.** "Revenue came in 6% under plan this quarter. Explain it to the CFO."

More examples: a feature has high adoption but no impact on retention; two dashboards show different numbers for the same metric; a new market launch is underperforming; a marketing channel's cost per acquisition doubled.

## Role variants
| Role | Most likely case |
|---|---|
| Data Scientist | diagnose a metric drop; design the experiment that would prove the cause |
| Data Analyst | diagnose a metric drop; define the metric and the dashboard to track it |
| Product Manager | did this launch work, launch or not, improve a metric, estimation |
| Finance Analyst | explain a revenue or cost variance vs plan; reforecast the year |
| Manager (add-on) | how you'd staff and sequence the analysis; how you'd present it to leadership |

## A simple frame: Clarify, Hypothesize, Check, Decide
1. **Clarify (30 seconds).** Define the metric, the time frame, and what "normal" looks like. One or two questions, not ten.
2. **Hypothesize.** Say your top hypothesis out loud, with a reason. "A sudden one-week drop is usually one segment, so I'd split by platform first."
3. **Check.** In order: is it real (tracking, pipeline) or not? Which segment? What changed at that time (release, pricing, marketing, season)? Name the data you'd pull.
4. **Decide.** What you'd recommend, what you'd need to see to change your mind, and the next step.

For estimation, swap step 3 for: state assumptions, build the math top-down, sanity-check against something you know.

For a variance to plan: split into volume, price, and mix. Then say which piece drove most of the gap, and whether it's a one-time miss or a trend that changes the forecast.

## Rubric
**3/10 sounds like:** "First I'd look at the data and make sure it's accurate, then I'd look at segments, then seasonality, and then form hypotheses." A list with no order, no metric, no answer.

**7/10 sounds like:** "I'd check it's not a tracking issue first, then split by platform, because one-week drops are usually one segment. If it's one platform, I'd line it up with the release calendar." Ordered, a hypothesis, a reason. Missing a recommendation.

**9/10 sounds like:** the 7, plus a clear recommendation, plus a specific answer to pushback: "If it's seasonal, the same week last year should show the same dip. If it doesn't, I'd keep digging." Uses a real example from their own work as evidence.

## Take-home callout
Take-homes are a case you do alone, with more time. They fail differently.
- **Lock scope before you build.** Write down the question you are answering and what you are not doing. Send it to the recruiter if you are unsure.
- **Keep a decisions log.** Every choice (which data, which metric, what you excluded) with the reason. See [take-home/decisions-log.md](../take-home/decisions-log.md).
- **Have a second AI review your work independently.** Give a fresh chat only the prompt and your output, and ask it to find the weakest claim. Don't give it your reasoning first.
- **List the risks with a prepared response.** The interviewer will ask about the weakest part. Have your answer ready. See [take-home/risk-list.md](../take-home/risk-list.md).
- **In the presentation: answer, then reason, then depth only if asked.** Open with the recommendation. Most candidates lose the room by walking through the method first.

The full guide is in [take-home/PLAYBOOK.md](../take-home/PLAYBOOK.md).

## Use your experience database
- Check `me/coverage-map.md` for "A metric dropped" and "Measure success of a launch". If they are Thin, run [kickoff session 2](../kickoff/session-2-best-projects.md).
- The strongest case answers use a real example as evidence: "I've seen this exact pattern: I traced a drop to one platform's release." Pull it from your story cards.
- Practice with `/mock case --mode practice`, then watch a model version with `/mock case --mode simulate`.
- Ask the coach: "Push back on my answer with 'it's just seasonal' and see if I hold my ground."
