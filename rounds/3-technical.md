# Round 3: Technical (SQL, Python, stats and A/B testing, metrics, forecasting)

## What it really tests
- **Correct work done cold.** Can you write the query or reason through the test without running anything?
- **Applied over textbook.** Do you know when a method breaks, not just its definition?
- **Talking while you work.** Can you explain what you're doing and catch your own mistakes?

## How people fail
What hiring managers see most often:
- **Can't write it without running it.** Fluent with an editor and autocomplete, stuck in a shared doc.
- **Grain mistakes.** Joining two tables at different grains and double counting, then not noticing the total is too big.
- **Textbook answers.** Defining a p-value perfectly, then not knowing what to do when the test was peeked at.
- **Silent coding.** Ten minutes of typing with no explanation. The interviewer can't give credit for thinking they can't hear.
- **No sanity check.** Never asking "does this number make sense?"

## Tracks and common questions

### SQL (all analyst and DS roles)
1. Revenue by segment, including segments with zero orders (LEFT JOIN, where the filter goes)
2. Users who never did X (anti-join)
3. Each user's first or second purchase (ROW_NUMBER, LEAD)
4. Week-over-week change (LAG)
5. Retention by signup cohort
6. Funnel conversion by step
7. Deduplicate a table and keep the latest or earliest row
8. A join that double counts, and how you'd catch it

Practice all of these on synthetic data in [practice/sql/](../practice/sql/drills.md).

### Python and pandas
1. Group, aggregate, and pivot a DataFrame
2. Merge two DataFrames and check the row count before and after
3. Handle missing values, and say why you chose that approach
4. Write a function that computes a metric from raw events
5. Loop vs vectorized: when does it matter?

### Stats and A/B testing (mostly DS, often DA)
1. How do you size a test? (power, significance level, minimum detectable effect, baseline rate, variance)
2. What's the minimum detectable effect, and what happens if you pick it too small?
3. What's wrong with peeking at results and stopping early?
4. What is a sample ratio mismatch (SRM), and what do you do when you see one?
5. Novelty and primacy effects: why a lift can fade, and how to check
6. Testing many metrics or variants at once: why false positives go up, and what to do
7. CUPED at a high level: using pre-experiment data to reduce variance so tests need fewer users
8. The test is flat. What do you tell the PM?
9. When can't you run an A/B test, and what would you do instead?

### PM metric definition and estimation
1. Define success for a new feature. Primary metric, guardrails, and how you'd count it.
2. What's a good north star metric for this product, and what would game it?
3. Estimate a market or usage number with stated assumptions.

### Finance forecast logic
1. Build a simple revenue forecast from drivers (users, conversion, price, churn).
2. The forecast was 8% too high. How do you find out why?
3. Which assumption in your model would you stress-test first?

## Role variants
| Role | Most likely track |
|---|---|
| Data Scientist | A/B design and power, stats judgment, SQL, some Python |
| Data Analyst | SQL (joins, windows, grain), metric definitions, some stats |
| Product Manager | metric definition, estimation, reading an experiment result |
| Finance Analyst | forecast logic, variance math, spreadsheet or SQL modeling |
| Manager (add-on) | how you review others' work, set quality standards, and catch errors before leadership sees them |

## A simple frame: Grain, Plan, Build, Check
1. **Grain.** Say out loud what one row of the output is. "One row per platform per week."
2. **Plan.** Say the steps before you write: "Filter to completed orders, count by week and platform, then LAG."
3. **Build.** Write it in small pieces. Talk as you go.
4. **Check.** Sanity-check the result: totals reconcile, no impossible values, row count makes sense.

For stats questions: answer in one sentence, then give the practical implication, then the caveat. "Peeking inflates false positives, so a test that looks significant on day 4 often isn't. I fix the length up front with a power calculation, and if the team needs to look early, I use a sequential method."

## Rubric
**3/10 sounds like:** writes a join without checking grain, gets a total that's too big, doesn't notice. Or: "A p-value is the probability the null is true." (It isn't.)

**7/10 sounds like:** correct query, states the grain, checks one sanity number. Stats answer is right and gives one practical implication.

**9/10 sounds like:** the 7, plus names the trap before falling in it ("this join will double count plan switchers, so I'll pick the latest subscription first"), plus ties the stats answer to a real decision they made.

## Use your experience database
- Check `me/coverage-map.md` for "Design an A/B test" and "peeking". A real test you ran beats any textbook example.
- If you've pushed back on stopping a test early, that story answers a stats question and a behavioral question.
- Drill SQL cold: `/drill sql windows`, then run your answer with `python practice/sql/q.py -f my_answer.sql`.
- Ask the coach: "Ask me to size a test for a metric I actually own, using my numbers card."
