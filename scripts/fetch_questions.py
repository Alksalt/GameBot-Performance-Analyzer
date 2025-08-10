from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

import pandas as pd
import requests

from true_false.game import DATA_DIR

POOL_JSON = DATA_DIR / "questions_pool.json"
POOL_CSV = DATA_DIR / "questions_pool.csv"


def fetch_batch(amount: int, category: int, qtype: str) -> list[dict]:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&type={qtype}"
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    data = r.json()
    return data.get("results", [])


essential = ["category", "type", "difficulty", "question", "correct_answer"]


def normalize(items: list[dict]) -> list[dict]:
    out = []
    for it in items:
        row = {k: it.get(k) for k in essential}
        row["question"] = html.unescape(str(row["question"]))
        row["correct_answer"] = str(row["correct_answer"]).lower()
        out.append(row)
    return out


def dedupe(rows: list[dict]) -> list[dict]:
    seen = set()
    unique = []
    for r in rows:
        key = (r["question"].strip().lower(), r["correct_answer"])  # simple de-dupe
        if key not in seen:
            seen.add(key)
            unique.append(r)
    return unique


def main() -> None:
    parser = argparse.ArgumentParser(description="Download and store a local pool of OpenTDB boolean questions")
    parser.add_argument("--batches", type=int, default=50)
    parser.add_argument("--amount", type=int, default=10, help="Questions per batch")
    parser.add_argument("--category", type=int, default=9)
    parser.add_argument("--qtype", type=str, default="boolean")
    args = parser.parse_args()

    all_rows: list[dict] = []
    for _ in range(args.batches):
        items = fetch_batch(args.amount, args.category, args.qtype)
        all_rows.extend(normalize(items))

    all_rows = dedupe(all_rows)

    POOL_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(POOL_JSON, "w", encoding="utf-8") as f:
        json.dump(all_rows, f, ensure_ascii=False, indent=2)

    pd.DataFrame(all_rows).to_csv(POOL_CSV, index=False)
    print(f"Saved {len(all_rows)} unique questions to:\n- {POOL_JSON}\n- {POOL_CSV}")


if __name__ == "__main__":
    main()