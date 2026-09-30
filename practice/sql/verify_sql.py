"""
Check every model answer in answers.sql against the seeded database.

Usage:
    python seed_db.py      # once
    python verify_sql.py

Each drill's SQL result is compared to the same number computed a second,
independent way in pandas. If a drill prints FAIL, the answer or the data is wrong.
"""

import os
import re
import sys

import duckdb
import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "fernly.duckdb")
ANSWERS = os.path.join(HERE, "answers.sql")


def load_answers():
    text = open(ANSWERS).read()
    parts = re.split(r"^-- @drill (\S+)\s*$", text, flags=re.M)
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


def same(sql_df, exp_df, cols):
    a = sql_df[cols].reset_index(drop=True)
    b = exp_df[cols].reset_index(drop=True)
    if len(a) != len(b):
        return False, f"row count {len(a)} vs expected {len(b)}"
    for c in cols:
        x, y = a[c], b[c]
        if pd.api.types.is_numeric_dtype(x) and pd.api.types.is_numeric_dtype(y):
            if not np.allclose(x.astype(float), y.astype(float), atol=0.051, equal_nan=True):
                return False, f"column {c}: {list(x)} vs expected {list(y)}"
        elif list(x.astype(str)) != list(y.astype(str)):
            return False, f"column {c}: {list(x)} vs expected {list(y)}"
    return True, ""


def main():
    if not os.path.exists(DB_PATH):
        sys.exit("No database yet. Run: python seed_db.py")
    con = duckdb.connect(DB_PATH, read_only=True)
    t = {n: con.execute(f"SELECT * FROM {n}").df() for n in
         ["users", "subscriptions", "orders", "events", "assignments"]}
    users, subs, orders, events, asg = (t[k] for k in ["users", "subscriptions", "orders", "events", "assignments"])
    for df, c in [(users, "signup_date"), (orders, "order_date"), (subs, "start_date")]:
        df[c] = pd.to_datetime(df[c])
    done = orders[orders.status == "completed"].copy()
    answers = load_answers()
    exp = {}

    # 1. revenue by channel, all users in the denominator
    g = users.merge(done, on="user_id", how="left", suffixes=("", "_o"))
    e = g.groupby("acquisition_channel").agg(users=("user_id", "nunique"),
                                             ordering_users=("order_id", lambda s: g.loc[s.dropna().index, "user_id"].nunique()),
                                             revenue=("amount", "sum")).reset_index()
    e["revenue_per_user"] = (e.revenue / e.users).round(2)
    e["revenue"] = e.revenue.round(2)
    exp["1"] = (e.sort_values("revenue", ascending=False), ["acquisition_channel", "users", "ordering_users", "revenue", "revenue_per_user"])

    # 2. never ordered
    buyers = set(done.user_id)
    u = users.assign(never=~users.user_id.isin(buyers))
    e = u.groupby("platform").agg(users=("user_id", "count"), never_ordered=("never", "sum")).reset_index()
    e["pct_never_ordered"] = (100 * e.never_ordered / e.users).round(1)
    exp["2"] = (e.sort_values("platform"), ["platform", "users", "never_ordered", "pct_never_ordered"])

    # 3. days to first order
    first = done.sort_values(["order_date", "order_id"]).groupby("user_id").head(1).merge(users, on="user_id", suffixes=("", "_u"))
    first["days"] = (first.order_date - first.signup_date).dt.days
    e = first.groupby("acquisition_channel").agg(ordering_users=("user_id", "count"), avg_days_to_first_order=("days", "mean")).reset_index()
    e["avg_days_to_first_order"] = e.avg_days_to_first_order.round(1)
    exp["3"] = (e.sort_values("acquisition_channel"), ["acquisition_channel", "ordering_users", "avg_days_to_first_order"])

    # 4. repeat rate and median gap
    s = done.sort_values(["user_id", "order_date", "order_id"])
    s["rn"] = s.groupby("user_id").cumcount() + 1
    s["next"] = s.groupby("user_id").order_date.shift(-1)
    f = s[s.rn == 1].copy()
    f["gap"] = (f["next"] - f.order_date).dt.days
    e = f.groupby("platform").agg(first_time_buyers=("user_id", "count"), repeat_buyers=("next", "count"),
                                  median_days_to_second=("gap", "median")).reset_index()
    e["repeat_rate_pct"] = (100 * e.repeat_buyers / e.first_time_buyers).round(1)
    exp["4"] = (e.sort_values("platform"), ["platform", "first_time_buyers", "repeat_buyers", "repeat_rate_pct", "median_days_to_second"])

    # 5. worst week-over-week drops
    w = done.assign(week=done.order_date.dt.to_period("W-SUN").dt.start_time).groupby(["platform", "week"]).size().rename("orders").reset_index()
    w = w.sort_values(["platform", "week"])
    w["prev_orders"] = w.groupby("platform").orders.shift(1)
    w = w[w.prev_orders >= 30].copy()
    w["pct_change"] = (100 * (w.orders - w.prev_orders) / w.prev_orders).round(1)
    exp["5"] = (w.sort_values("pct_change").head(3), ["platform", "orders", "prev_orders", "pct_change"])

    # 6. monthly retention cohorts
    c = users[users.signup_date < "2026-04-01"].assign(cm=lambda d: d.signup_date.dt.to_period("M"))
    a = done.merge(c[["user_id", "cm"]], on="user_id")
    a["off"] = (a.order_date.dt.to_period("M") - a.cm).apply(lambda x: x.n)
    rows = []
    for cm, grp in c.groupby("cm"):
        n = len(grp)
        r = {"cohort_users": n}
        for k in (1, 2, 3):
            r[f"m{k}_pct"] = round(100 * a[(a.cm == cm) & (a.off == k)].user_id.nunique() / n, 1)
        rows.append(r)
    exp["6"] = (pd.DataFrame(rows), ["cohort_users", "m1_pct", "m2_pct", "m3_pct"])

    # 7. May funnel
    m = events[(events.event_ts >= "2026-05-01") & (events.event_ts < "2026-06-01")]
    p = m.groupby(["platform", "event_name"]).user_id.nunique().unstack().reset_index()
    p["payment_to_complete_pct"] = (100 * p.order_complete / p.payment_submit).round(1)
    exp["7"] = (p.sort_values("platform"), ["platform", "view_menu", "add_to_cart", "checkout_start", "payment_submit", "order_complete", "payment_to_complete_pct"])

    # 8. dedupe assignments
    a1 = asg[asg.experiment_id == 1].sort_values("assigned_at").groupby("user_id").head(1)
    e = a1.groupby("variant").size().rename("users").reset_index()
    e["pct_of_users"] = (100 * e.users / e.users.sum()).round(1)
    exp["8"] = (e.sort_values("variant"), ["variant", "users", "pct_of_users"])
    d = asg[asg.experiment_id == 1].groupby("user_id").agg(n=("variant", "size"), v=("variant", "nunique"))
    d = d[d.n > 1]
    exp["8b"] = (pd.DataFrame([{"users_with_duplicate_rows": len(d), "users_with_conflicting_variants": int((d.v > 1).sum())}]),
                 ["users_with_duplicate_rows", "users_with_conflicting_variants"])

    # 9. experiment readout
    fs = subs.sort_values(["start_date", "subscription_id"]).groupby("user_id").head(1)
    r = a1.merge(fs, on="user_id", how="left")
    r["annual"] = (r.plan == "annual") & (r.start_date <= r.assigned_at.dt.normalize() + pd.Timedelta(days=7))
    e = r.groupby("variant").agg(users=("user_id", "count"), annual_users=("annual", "sum")).reset_index()
    e["uptake_pct"] = (100 * e.annual_users / e.users).round(1)
    exp["9"] = (e.sort_values("variant"), ["variant", "users", "annual_users", "uptake_pct"])

    # 10. revenue by current plan, totals must reconcile
    cp = subs.sort_values(["start_date", "subscription_id"]).groupby("user_id").tail(1)[["user_id", "plan"]]
    ur = done.groupby("user_id").amount.sum().rename("revenue").reset_index()
    x = users[["user_id"]].merge(cp, on="user_id", how="left").merge(ur, on="user_id", how="left")
    x["current_plan"] = x.plan.fillna("none")
    e = x.groupby("current_plan").agg(users=("user_id", "count"), revenue=("revenue", "sum")).reset_index()
    e["revenue"] = e.revenue.round(2)
    exp["10"] = (e.sort_values("current_plan"), ["current_plan", "users", "revenue"])

    failures = 0
    for key in sorted(answers, key=lambda k: (int(re.match(r"\d+", k).group()), k)):
        got = con.execute(answers[key]).df()
        ok, why = same(got, *exp[key])
        extra = ""
        if key == "10" and ok:
            total = round(done.amount.sum(), 2)
            ok = abs(got.revenue.sum() - total) < 0.05
            extra = f" (reconciles to total revenue {total:,.2f})" if ok else " (does not reconcile to total revenue)"
        if key == "5" and ok:
            top = got.iloc[0]
            extra = f" (worst drop: {top.platform} week of {pd.Timestamp(top.week).date()}, {top['pct_change']}%)"
        print(f"drill {key:<4} {'PASS' if ok else 'FAIL'}{extra}{'  ' + why if not ok else ''}")
        failures += not ok
    missing = set(exp) - set(answers)
    for k in sorted(missing):
        print(f"drill {k:<4} FAIL  no answer found in answers.sql")
        failures += 1
    print(f"\n{len(exp) - failures}/{len(exp)} checks passed")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
