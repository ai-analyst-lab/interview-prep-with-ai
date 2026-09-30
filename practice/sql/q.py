"""
Run a SQL query against the Fernly practice database and print the result.

Usage:
    python q.py "SELECT * FROM orders LIMIT 5"
    python q.py -f my_answer.sql
    python q.py --schema

Write your query before you run it. The point is to get it right cold,
the way you would on a whiteboard or a shared doc in an interview.
"""

import os
import sys

import duckdb

HERE = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(HERE, "fernly.duckdb")


def show_schema(con):
    for (table,) in con.execute("SHOW TABLES").fetchall():
        n = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"\n{table}  ({n:,} rows)")
        for col in con.execute(f"PRAGMA table_info('{table}')").fetchall():
            print(f"    {col[1]:<22} {col[2]}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    if not os.path.exists(DB_PATH):
        sys.exit("No database yet. Run: python seed_db.py")
    con = duckdb.connect(DB_PATH, read_only=True)
    if sys.argv[1] == "--schema":
        show_schema(con)
        return
    if sys.argv[1] == "-f":
        with open(sys.argv[2]) as fh:
            sql = fh.read()
    else:
        sql = " ".join(sys.argv[1:])
    con.sql(sql).show(max_rows=50)


if __name__ == "__main__":
    main()
