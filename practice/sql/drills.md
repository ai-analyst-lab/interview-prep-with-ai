# SQL drills: Fernly practice database

Ten drills in the style of an analyst or data science SQL round. The data is a synthetic version of Fernly, a fictional meal-kit subscription app.

## Setup (once)
```bash
cd practice/sql
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python seed_db.py                # creates fernly.duckdb
python q.py --schema             # see the tables
```

## How to practice
1. Read the drill. Say out loud what the grain of the output is (one row per what?).
2. Write the query in a plain text file without running it. Interviews are usually in a shared doc.
3. Run it: `python q.py -f my_answer.sql`
4. Compare with `answers.sql`. If yours differs, find the line that caused it.
5. Explain your query to the AI coach in two sentences, headline first. Ask it to push back once.

`python verify_sql.py` checks that every model answer matches an independent calculation.

## Tables
| Table | Grain | Watch out for |
|---|---|---|
| `users` | one row per user | every user, including ones who never ordered |
| `subscriptions` | one row per subscription period | a user who switched plans has two rows |
| `orders` | one row per order | `status` is completed, cancelled, or refunded |
| `events` | one row per app event | funnel steps: view_menu, add_to_cart, checkout_start, payment_submit, order_complete |
| `experiments` | one row per test | |
| `assignments` | should be one row per user per test | it isn't: some users are logged twice |

Unless a drill says otherwise, "orders" and "revenue" mean completed orders only.

## Drills

**1. Revenue by channel (joins).** For each acquisition channel: total users, users with at least one completed order, completed revenue, and revenue per user (divided by all users in the channel). Sort by revenue.
*Trap:* where you put the status filter decides whether users with no orders count.

**2. Never ordered (anti-join).** For each platform: users, users who never placed a completed order, and that share as a percent.

**3. Time to first order (window function).** For each acquisition channel: number of users with a completed order, and the average days from signup to their first completed order. Use `ROW_NUMBER`.

**4. Repeat buyers (LEAD).** For each platform, among users with at least one completed order: how many placed a second one, the repeat rate, and the median days between the first and second order.

**5. Week-over-week drop (LAG).** Count completed orders per platform per week (weeks start Monday). Compute the week-over-week percent change. Return the 3 worst drops where the prior week had at least 30 orders.
*Follow-up to expect:* "Why the 30-order floor?" and "What would you check next?"

**6. Retention cohorts.** For users who signed up in January, February, or March 2026, group by signup month. For each cohort: cohort size, and the percent of the cohort with a completed order 1, 2, and 3 calendar months after their signup month.

**7. Funnel (conditional aggregation).** For May 2026, by platform: distinct users at each funnel step (view_menu, add_to_cart, checkout_start, payment_submit, order_complete), and the payment_submit to order_complete conversion rate. Which platform looks broken?

**8. Dedupe assignments.** For experiment 1, keep each user's earliest assignment. Return users and percent of users per variant.
**8b.** How many users in experiment 1 have duplicate rows, and how many of those have two different variants?
*Follow-up to expect:* "Is this split a sample ratio mismatch?" (Run a chi-square test on the counts outside SQL, or ask the coach to walk you through it.)

**9. Experiment readout.** Experiment 1 tested an annual plan discount. Using deduplicated assignments, compute per variant: assigned users, users whose first subscription was annual and started within 7 days of assignment, and the uptake percent. The denominator is everyone assigned.
*Follow-up to expect:* "Would you ship it?" Look at the sample size before you answer.

**10. Revenue by current plan (grain trap).** Total completed revenue by each user's current plan (their latest subscription), with users who never subscribed as `none`. Your total must equal total completed revenue across all orders.
*Trap:* joining `orders` straight to `subscriptions` counts plan switchers twice.

## After each drill
Add any drill you got wrong to `debriefs/retest-queue.md`. It's learned when you get it right cold, on 3 different days.
