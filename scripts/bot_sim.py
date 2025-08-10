from __future__ import annotations

import argparse
import random
from pathlib import Path
from typing import Dict, Tuple

import pandas as pd

from true_false.game import LocalTrueFalseGame, GameConfig, DATA_DIR, SUMMARY_CSV

BOT_RUNS_CSV = DATA_DIR / "bot_runs.csv"


def smart_bot_answer(true_value: str, correct_prob: float = 0.7) -> str:
    """Return the true value with given probability; otherwise a random boolean."""
    return true_value if random.random() < correct_prob else random.choice(["true", "false"])


def difficulty_curve(label: str, idx: int) -> float:
    """Piecewise accuracy schedule by difficulty and question index."""
    if label == "easy":
        return 0.8 if idx < 5 else 0.6
    if label == "medium":
        return 0.55 if idx < 5 else 0.35
    return 0.25 if idx < 5 else 0.10  # hard


def run_single_bot(bot_name: str, pool_path: Path, difficulty: str, n: int, seed: int) -> Dict:
    rng = random.Random(seed)
    random.seed(seed)

    cfg = GameConfig(amount=n, difficulty_label=difficulty)
    game = LocalTrueFalseGame(pool_path, cfg)

    # Sample N questions if pool is larger
    if len(game.df) > n:
        game.df = game.df.sample(n=n, random_state=seed)
        game.fixed_total = n

    allowed_wrong = {"easy": 3, "medium": 2, "hard": 1}[difficulty]

    attempts = 0
    current_streak = max_streak = 0

    for idx, (q, truth) in enumerate(game._question_stream()):
        if game.wrong_answers >= allowed_wrong:
            break
        attempts += 1
        p = difficulty_curve(difficulty, idx)
        answer = smart_bot_answer(truth, correct_prob=p)
        correct = (answer == truth)
        if correct:
            game.score += 1
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            game.wrong_answers += 1
            current_streak = 0
        game.answers[q] = answer
        game._append_answer(bot_name, q, answer, correct)

    game.player_name = bot_name
    game.attempts = attempts
    game.max_streak = max_streak

    completed = game.wrong_answers < allowed_wrong and attempts == game.fixed_total
    game._append_score(bot_name, game.score)
    game._append_summary(completed=completed, total_questions=len(game.answers))

    return {
        "Player": bot_name,
        "Score": game.score,
        "Wrong": game.wrong_answers,
        "Attempted": attempts,
        "Completed": completed,
        "Difficulty": difficulty,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate many bot games for analytics")
    parser.add_argument("--runs", type=int, default=300, help="Number of bot games to simulate")
    parser.add_argument("--difficulty", choices=["easy", "medium", "hard"], default="medium")
    parser.add_argument("--n", type=int, default=10, help="Questions per game")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--pool", type=str, default=str(DATA_DIR / "questions_pool.json"))
    args = parser.parse_args()

    pool_path = Path(args.pool)
    BOT_RUNS_CSV.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    for i in range(args.runs):
        bot_name = f"SmartBot{i+1}"
        seed = args.seed + i
        res = run_single_bot(bot_name, pool_path, args.difficulty, args.n, seed)
        rows.append(res)
        print(res)

    df = pd.DataFrame(rows)
    if BOT_RUNS_CSV.exists():
        prev = pd.read_csv(BOT_RUNS_CSV)
        df = pd.concat([prev, df], ignore_index=True)
    df.to_csv(BOT_RUNS_CSV, index=False)
    print(f"Saved {len(rows)} runs to {BOT_RUNS_CSV}")


if __name__ == "__main__":
    main()