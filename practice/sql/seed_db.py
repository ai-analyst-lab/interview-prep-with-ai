"""
Build the practice database: a synthetic Fernly (fictional meal-kit subscription app).

Usage:
    python seed_db.py

Creates fernly.duckdb next to this file. The data is random but seeded, so everyone
gets the same numbers and the answers in answers.sql always match.

Tables
    users          one row per user (signup date, platform, channel, region)
    subscriptions  one row per subscription period (a user can have more than one)
    orders         one row per order (completed, cancelled, or refunded)
    events         app events: app_open, view_menu, add_to_cart, checkout_start,
                   payment_submit, order_complete
    experiments    one row per A/B test
    assignments    who got which variant (has duplicate rows on purpose)

Two things are planted in the data for you to find:
    1. One week in May, iOS orders drop because the payment step breaks.
    2. The assignments table logs some users twice, sometimes with a different variant.
"""

import os
import random
from datetime import date, datetime, timedelta

import duckdb
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "fernly.duckdb")

SEED = 7
N_USERS = 800
START = date(2026, 1, 5)   # a Monday
END = date(2026, 6, 28)    # a Sunday
BUG_WEEK = (date(2026, 5, 11), date(2026, 5, 17))  # iOS payment bug

EXP1 = dict(experiment_id=1, name="annual_discount", start_date=date(2026, 3, 2),
            end_date=date(2026, 4, 12), primary_metric="annual_plan_uptake")
EXP2 = dict(experiment_id=2, name="new_menu_layout", start_date=date(2026, 4, 6),
            end_date=date(2026, 4, 19), primary_metric="orders_per_user")


def ts(d, rng, hour_lo=7, hour_hi=22):
    return datetime(d.year, d.month, d.day, rng.randint(hour_lo, hour_hi), rng.randint(0, 59), rng.randint(0, 59))


def main():
    rng = random.Random(SEED)
    users, subs, orders, events, assignments = [], [], [], [], []
    sub_id = order_id = event_id = 0
    total_days = (END - START).days

    def add_event(uid, when, name, platform):
        nonlocal event_id
        event_id += 1
        events.append((event_id, uid, when, name, platform))

    for uid in range(1, N_USERS + 1):
        signup = START + timedelta(days=int(rng.random() ** 0.9 * (total_days - 14)))
        platform = rng.choices(["ios", "android", "web"], [0.5, 0.3, 0.2])[0]
        channel = rng.choices(["paid_social", "search", "referral", "organic"], [0.35, 0.25, 0.15, 0.25])[0]
        region = rng.choice(["west", "central", "east"])
        users.append((uid, signup, platform, channel, region))
        add_event(uid, ts(signup, rng), "app_open", platform)

        # Experiment 1: users who sign up during the test are randomized at signup.
        variant = None
        if EXP1["start_date"] <= signup <= EXP1["end_date"]:
            variant = rng.choice(["control", "treatment"])
            assigned_at = ts(signup, rng, 0, 6)
            assignments.append((1, uid, variant, assigned_at))
            if rng.random() < 0.05:  # logging bug: a second row, a day or two later
                dup_variant = rng.choice(["control", "treatment"])
                assignments.append((1, uid, dup_variant, assigned_at + timedelta(days=rng.randint(1, 3))))

        if rng.random() > 0.85:
            continue  # never subscribes

        annual_p = {"control": 0.09, "treatment": 0.14}.get(variant, 0.10)
        plan = "annual" if rng.random() < annual_p else "monthly"
        sub_start = signup + timedelta(days=rng.randint(0, 2))
        order_p = rng.uniform(0.3, 0.6)
        current = sub_start
        active = True
        while active and current <= END:
            week_end = min(current + timedelta(days=6), END)
            # order attempt this week
            if rng.random() < order_p:
                d = current + timedelta(days=rng.randint(0, (week_end - current).days))
                t = ts(d, rng)
                steps = ["app_open", "view_menu", "add_to_cart", "checkout_start", "payment_submit"]
                for i, s in enumerate(steps):
                    add_event(uid, t + timedelta(minutes=2 * i), s, platform)
                success_p = 0.35 if (platform == "ios" and BUG_WEEK[0] <= d <= BUG_WEEK[1]) else 0.94
                if rng.random() < success_p:
                    add_event(uid, t + timedelta(minutes=11), "order_complete", platform)
                    order_id += 1
                    status = rng.choices(["completed", "refunded", "cancelled"], [0.94, 0.03, 0.03])[0]
                    amount = round(rng.uniform(45, 95), 2)
                    orders.append((order_id, uid, d, platform, amount, status))
            # a browse-only session
            if rng.random() < 0.25:
                d = current + timedelta(days=rng.randint(0, (week_end - current).days))
                t = ts(d, rng)
                add_event(uid, t, "app_open", platform)
                add_event(uid, t + timedelta(minutes=1), "view_menu", platform)
                if rng.random() < 0.3:
                    add_event(uid, t + timedelta(minutes=3), "add_to_cart", platform)

            nxt = current + timedelta(days=7)
            churn_p = 0.02 if plan == "annual" else 0.06
            if rng.random() < churn_p and nxt <= END:
                sub_id += 1
                subs.append((sub_id, uid, plan, sub_start, nxt, "cancelled"))
                active = False
            elif plan == "monthly" and rng.random() < 0.02 and nxt <= END:
                sub_id += 1
                subs.append((sub_id, uid, plan, sub_start, nxt, "switched"))
                plan, sub_start = "annual", nxt
            current = nxt
        if active:
            sub_id += 1
            subs.append((sub_id, uid, plan, sub_start, None, "active"))

    # Experiment 2: everyone with an active subscription on the start date.
    s2 = EXP2["start_date"]
    active_on_s2 = sorted({s[1] for s in subs if s[3] <= s2 and (s[4] is None or s[4] > s2)})
    for uid in active_on_s2:
        assignments.append((2, uid, rng.choice(["control", "treatment"]), ts(s2, rng, 0, 6)))

    frames = {
        "users": pd.DataFrame(users, columns=["user_id", "signup_date", "platform", "acquisition_channel", "region"]),
        "subscriptions": pd.DataFrame(subs, columns=["subscription_id", "user_id", "plan", "start_date", "end_date", "status"]),
        "orders": pd.DataFrame(orders, columns=["order_id", "user_id", "order_date", "platform", "amount", "status"]),
        "events": pd.DataFrame(events, columns=["event_id", "user_id", "event_ts", "event_name", "platform"]),
        "experiments": pd.DataFrame([EXP1, EXP2]),
        "assignments": pd.DataFrame(assignments, columns=["experiment_id", "user_id", "variant", "assigned_at"]),
    }
    frames["events"]["event_ts"] = frames["events"]["event_ts"].astype("datetime64[us]")
    frames["assignments"]["assigned_at"] = frames["assignments"]["assigned_at"].astype("datetime64[us]")
    for col in ("start_date", "end_date"):
        frames["subscriptions"][col] = pd.to_datetime(frames["subscriptions"][col])
    frames["users"]["signup_date"] = pd.to_datetime(frames["users"]["signup_date"])
    frames["orders"]["order_date"] = pd.to_datetime(frames["orders"]["order_date"])

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    con = duckdb.connect(DB_PATH)
    date_cols = {
        "users": ["signup_date"],
        "subscriptions": ["start_date", "end_date"],
        "orders": ["order_date"],
        "experiments": ["start_date", "end_date"],
    }
    ts_cols = {"events": ["event_ts"], "assignments": ["assigned_at"]}
    for name, df in frames.items():
        con.register("tmp_df", df)
        con.execute(f"CREATE TABLE {name} AS SELECT * FROM tmp_df")
        con.unregister("tmp_df")
        for c in date_cols.get(name, []):
            con.execute(f"ALTER TABLE {name} ALTER {c} TYPE DATE")
        for c in ts_cols.get(name, []):
            con.execute(f"ALTER TABLE {name} ALTER {c} TYPE TIMESTAMP")
    for name in frames:
        n = con.execute(f"SELECT COUNT(*) FROM {name}").fetchone()[0]
        print(f"{name:<14} {n:>7,} rows")
    con.close()
    print(f"\nWrote {os.path.basename(DB_PATH)}. Try: python q.py --schema")


if __name__ == "__main__":
    main()
