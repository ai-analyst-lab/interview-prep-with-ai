-- Model answers for drills.md
-- Try each drill cold first. Then compare. There is usually more than one correct query;
-- what matters is that yours returns the same result and you can explain every line.
-- verify_sql.py runs every block below (split on the "-- @drill" markers) and checks the results.


-- @drill 1
-- Trap: putting o.status = 'completed' in WHERE turns the LEFT JOIN into an INNER JOIN
-- and silently drops users with no orders from the denominator.
SELECT u.acquisition_channel,
       COUNT(DISTINCT u.user_id)                                         AS users,
       COUNT(DISTINCT o.user_id)                                         AS ordering_users,
       ROUND(COALESCE(SUM(o.amount), 0), 2)                              AS revenue,
       ROUND(COALESCE(SUM(o.amount), 0) / COUNT(DISTINCT u.user_id), 2)  AS revenue_per_user
FROM users u
LEFT JOIN orders o
       ON o.user_id = u.user_id
      AND o.status = 'completed'
GROUP BY 1
ORDER BY revenue DESC;


-- @drill 2
SELECT u.platform,
       COUNT(*)                                              AS users,
       COUNT(*) FILTER (WHERE o.user_id IS NULL)             AS never_ordered,
       ROUND(100.0 * COUNT(*) FILTER (WHERE o.user_id IS NULL) / COUNT(*), 1) AS pct_never_ordered
FROM users u
LEFT JOIN (SELECT DISTINCT user_id FROM orders WHERE status = 'completed') o
       ON o.user_id = u.user_id
GROUP BY 1
ORDER BY 1;


-- @drill 3
WITH ranked AS (
    SELECT o.user_id, o.order_date,
           ROW_NUMBER() OVER (PARTITION BY o.user_id ORDER BY o.order_date, o.order_id) AS rn
    FROM orders o
    WHERE o.status = 'completed'
)
SELECT u.acquisition_channel,
       COUNT(*)                                                    AS ordering_users,
       ROUND(AVG(date_diff('day', u.signup_date, r.order_date)), 1) AS avg_days_to_first_order
FROM ranked r
JOIN users u ON u.user_id = r.user_id
WHERE r.rn = 1
GROUP BY 1
ORDER BY 1;


-- @drill 4
WITH seq AS (
    SELECT user_id, platform, order_date,
           ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date, order_id) AS rn,
           LEAD(order_date) OVER (PARTITION BY user_id ORDER BY order_date, order_id) AS next_order_date
    FROM orders
    WHERE status = 'completed'
)
SELECT platform,
       COUNT(*)                                                           AS first_time_buyers,
       COUNT(next_order_date)                                             AS repeat_buyers,
       ROUND(100.0 * COUNT(next_order_date) / COUNT(*), 1)                AS repeat_rate_pct,
       ROUND(MEDIAN(date_diff('day', order_date, next_order_date)), 1)    AS median_days_to_second
FROM seq
WHERE rn = 1
GROUP BY 1
ORDER BY 1;


-- @drill 5
WITH weekly AS (
    SELECT date_trunc('week', order_date) AS week, platform, COUNT(*) AS orders
    FROM orders
    WHERE status = 'completed'
    GROUP BY 1, 2
),
wow AS (
    SELECT week, platform, orders,
           LAG(orders) OVER (PARTITION BY platform ORDER BY week) AS prev_orders
    FROM weekly
)
SELECT week, platform, orders, prev_orders,
       ROUND(100.0 * (orders - prev_orders) / prev_orders, 1) AS pct_change
FROM wow
WHERE prev_orders >= 30
ORDER BY pct_change
LIMIT 3;


-- @drill 6
WITH cohort AS (
    SELECT user_id, date_trunc('month', signup_date) AS cohort_month
    FROM users
    WHERE signup_date < DATE '2026-04-01'
),
activity AS (
    SELECT DISTINCT o.user_id,
           date_diff('month', c.cohort_month, date_trunc('month', o.order_date)) AS month_offset
    FROM orders o
    JOIN cohort c ON c.user_id = o.user_id
    WHERE o.status = 'completed'
)
SELECT c.cohort_month,
       COUNT(DISTINCT c.user_id) AS cohort_users,
       ROUND(100.0 * COUNT(DISTINCT a.user_id) FILTER (WHERE a.month_offset = 1) / COUNT(DISTINCT c.user_id), 1) AS m1_pct,
       ROUND(100.0 * COUNT(DISTINCT a.user_id) FILTER (WHERE a.month_offset = 2) / COUNT(DISTINCT c.user_id), 1) AS m2_pct,
       ROUND(100.0 * COUNT(DISTINCT a.user_id) FILTER (WHERE a.month_offset = 3) / COUNT(DISTINCT c.user_id), 1) AS m3_pct
FROM cohort c
LEFT JOIN activity a ON a.user_id = c.user_id
GROUP BY 1
ORDER BY 1;


-- @drill 7
WITH may AS (
    SELECT platform, event_name, COUNT(DISTINCT user_id) AS users
    FROM events
    WHERE event_ts >= TIMESTAMP '2026-05-01' AND event_ts < TIMESTAMP '2026-06-01'
    GROUP BY 1, 2
)
SELECT platform,
       MAX(users) FILTER (WHERE event_name = 'view_menu')      AS view_menu,
       MAX(users) FILTER (WHERE event_name = 'add_to_cart')    AS add_to_cart,
       MAX(users) FILTER (WHERE event_name = 'checkout_start') AS checkout_start,
       MAX(users) FILTER (WHERE event_name = 'payment_submit') AS payment_submit,
       MAX(users) FILTER (WHERE event_name = 'order_complete') AS order_complete,
       ROUND(100.0 * MAX(users) FILTER (WHERE event_name = 'order_complete')
                   / MAX(users) FILTER (WHERE event_name = 'payment_submit'), 1) AS payment_to_complete_pct
FROM may
GROUP BY 1
ORDER BY 1;


-- @drill 8
WITH first_assignment AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY experiment_id, user_id ORDER BY assigned_at) AS rn
    FROM assignments
    WHERE experiment_id = 1
)
SELECT variant,
       COUNT(*)                                          AS users,
       ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 1) AS pct_of_users
FROM first_assignment
WHERE rn = 1
GROUP BY 1
ORDER BY 1;


-- @drill 8b
SELECT COUNT(*) AS users_with_duplicate_rows,
       COUNT(*) FILTER (WHERE n_variants > 1) AS users_with_conflicting_variants
FROM (
    SELECT user_id, COUNT(*) AS n_rows, COUNT(DISTINCT variant) AS n_variants
    FROM assignments
    WHERE experiment_id = 1
    GROUP BY 1
    HAVING COUNT(*) > 1
);


-- @drill 9
-- Denominator is everyone assigned, not only people who subscribed.
WITH a AS (
    SELECT user_id, variant, assigned_at
    FROM assignments
    WHERE experiment_id = 1
    QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY assigned_at) = 1
),
first_sub AS (
    SELECT user_id, plan, start_date
    FROM subscriptions
    QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY start_date, subscription_id) = 1
)
SELECT a.variant,
       COUNT(*) AS users,
       COUNT(*) FILTER (WHERE s.plan = 'annual'
                          AND s.start_date <= CAST(a.assigned_at AS DATE) + INTERVAL 7 DAY) AS annual_users,
       ROUND(100.0 * COUNT(*) FILTER (WHERE s.plan = 'annual'
                          AND s.start_date <= CAST(a.assigned_at AS DATE) + INTERVAL 7 DAY) / COUNT(*), 1) AS uptake_pct
FROM a
LEFT JOIN first_sub s ON s.user_id = a.user_id
GROUP BY 1
ORDER BY 1;


-- @drill 10
-- Trap: joining orders straight to subscriptions repeats every order once per
-- subscription row, so users who switched plans get counted twice.
WITH current_plan AS (
    SELECT user_id, plan
    FROM subscriptions
    QUALIFY ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY start_date DESC, subscription_id DESC) = 1
),
user_revenue AS (
    SELECT user_id, SUM(amount) AS revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY 1
)
SELECT COALESCE(cp.plan, 'none')          AS current_plan,
       COUNT(*)                            AS users,
       ROUND(COALESCE(SUM(ur.revenue), 0), 2) AS revenue
FROM users u
LEFT JOIN current_plan cp ON cp.user_id = u.user_id
LEFT JOIN user_revenue ur ON ur.user_id = u.user_id
GROUP BY 1
ORDER BY 1;
