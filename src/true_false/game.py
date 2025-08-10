from __future__ import annotations

import datetime as dt
import html
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Generator, Iterable, Optional, Tuple

import pandas as pd
import requests

# -----------------------------
# Paths & logging
# -----------------------------
ROOT = Path(__file__).resolve().parents[2]  # repo/
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

LOG_LEVEL = logging.INFO
logging.basicConfig(
    level=LOG_LEVEL,
    format="[%(asctime)s] %(levelname)s - %(message)s",
    datefmt="%H:%M:%S",
)

SCORES_CSV = DATA_DIR / "scores.csv"
ANSWERS_CSV = DATA_DIR / "final_answers.csv"
SUMMARY_CSV = DATA_DIR / "game_summary.csv"


@dataclass
class GameConfig:
    amount: int = 10  # number of questions per game
    category: Optional[int] = 9  # General Knowledge in OpenTDB
    qtype: str = "boolean"
    difficulty_label: str = "medium"  # easy/medium/hard (affects allowed wrongs)


class TrueFalseGame:
    """
    True/False trivia game engine.
    - Loads questions from OpenTDB API (default) or any URL that returns OpenTDB-like JSON
      with a top-level "results" list.
    - Tracks score, streaks, attempts.
    - Saves answers, scores and a per-game summary to ../data/.
    """

    def __init__(self, url: str, config: Optional[GameConfig] = None):
        self.url = url
        self.config = config or GameConfig()

        self.df: pd.DataFrame = self._load_statements(url)
        self.score: int = 0
        self.wrong_answers: int = 0
        self.answers: Dict[str, str] = {}
        self.player_name: str = ""
        self.max_streak: int = 0
        self.attempts: int = 0
        self.fixed_total: int = len(self.df)
        self.difficulty_label: str = self.config.difficulty_label

        # High scores / answers tables (lazy-created if missing)
        self.scores_df = self._ensure_csv(SCORES_CSV, ["Player", "Score"])  # type: ignore
        self.final_answers_df = self._ensure_csv(ANSWERS_CSV, ["Player", "Question", "Player_answer", "Correct"])  # type: ignore

    # -----------------------------
    # Data loading
    # -----------------------------
    def _ensure_csv(self, path: Path, columns: Iterable[str]) -> pd.DataFrame:
        if path.exists():
            try:
                return pd.read_csv(path)
            except Exception as exc:
                logging.warning("Failed reading %s (%s). Recreating.", path, exc)
        df = pd.DataFrame(columns=list(columns))
        df.to_csv(path, index=False)
        return df

    def _normalize(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.empty:
            return df
        # Ensure required columns exist and normalize values
        want = ["category", "type", "difficulty", "question", "correct_answer"]
        missing = [c for c in want if c not in df.columns]
        if missing:
            logging.error("API response missing columns: %s", missing)
            return pd.DataFrame(columns=want)
        df = df.copy()
        df["question"] = df["question"].map(lambda s: html.unescape(str(s)))
        df["correct_answer"] = df["correct_answer"].str.lower()
        return df[want]

    def _load_statements(self, url: str) -> pd.DataFrame:
        try:
            r = requests.get(url, timeout=20)
            r.raise_for_status()
            data = r.json()
            if "results" in data:
                return self._normalize(pd.DataFrame(data["results"]))
            logging.error("Unexpected API payload: missing 'results'")
            return pd.DataFrame()
        except requests.RequestException as e:
            logging.error("Error fetching data: %s", e)
            return pd.DataFrame()

    # -----------------------------
    # Game I/O helpers
    # -----------------------------
    def _prompt_yes_no(self, message: str) -> bool:
        while True:
            ans = input(message).strip().lower()
            if ans in {"yes", "y"}:  # casual niceness
                return True
            if ans in {"no", "n"}:
                return False
            print("Please answer yes/no.")

    def _prompt_difficulty(self) -> int:
        print("\n" + "=" * 55)
        print("Choose a difficulty level:")
        print("easy   = 3 wrong tries allowed")
        print("medium = 2 wrong tries allowed")
        print("hard   = 1 wrong try  allowed")
        print("=" * 55)
        mapping = {"easy": 3, "medium": 2, "hard": 1}
        while True:
            diff = input("\nChoose between: easy/medium/hard: ").strip().lower()
            if diff in mapping:
                self.difficulty_label = diff
                return mapping[diff]
            print("Choose: easy / medium / hard.")

    def _question_stream(self) -> Generator[Tuple[str, str], None, None]:
        df = self.df.sample(frac=1, random_state=None)  # shuffle for fairness
        for _, row in df.iterrows():
            yield row["question"], row["correct_answer"]
        print("\n" + "-" * 40)
        print("No more questions left")
        print("-" * 40 + "\n")

    # -----------------------------
    # Persistence
    # -----------------------------
    def _append_score(self, player: str, score: int) -> None:
        new_row = pd.DataFrame([[player, score]], columns=["Player", "Score"])  # type: ignore
        self.scores_df = pd.concat([self.scores_df, new_row], ignore_index=True)
        self.scores_df.to_csv(SCORES_CSV, index=False)

    def _append_answer(self, player: str, question: str, player_answer: str, correct: bool) -> None:
        new_row = pd.DataFrame([[player, question, player_answer, correct]],
                               columns=["Player", "Question", "Player_answer", "Correct"])  # type: ignore
        self.final_answers_df = pd.concat([self.final_answers_df, new_row], ignore_index=True)
        self.final_answers_df.to_csv(ANSWERS_CSV, index=False)

    def _append_summary(
        self,
        completed: bool,
        total_questions: int,
    ) -> None:
        """Save metrics from the current game into the CSV."""
        accuracy_fixed = round(self.score / self.fixed_total, 3) if self.fixed_total else 0.0
        accuracy_attempted = round(self.score / self.attempts, 3) if self.attempts else 0.0
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        columns = [
            "Player",
            "Score",
            "Wrong",
            "Fixed_total",
            "Attempted",
            "Accuracy_fixed",
            "Accuracy_attempted",
            "Max_streak",
            "Difficulty",
            "Date",
            "Completed",
            "Total_questions_logged",
        ]
        new_row = pd.DataFrame([[
            self.player_name,
            self.score,
            self.wrong_answers,
            int(self.fixed_total),
            int(self.attempts),
            accuracy_fixed,
            accuracy_attempted,
            int(self.max_streak),
            self.difficulty_label,
            timestamp,
            bool(completed),
            int(total_questions),
        ]], columns=columns)  # type: ignore

        if SUMMARY_CSV.exists():
            summary = pd.read_csv(SUMMARY_CSV)
        else:
            summary = pd.DataFrame(columns=columns)
        summary = pd.concat([summary, new_row], ignore_index=True)
        summary.to_csv(SUMMARY_CSV, index=False)

    # -----------------------------
    # Public API
    # -----------------------------
    def play(self) -> bool:
        print("\n" + "=" * 55)
        print("Welcome to the True/False game!")
        print("=" * 55)
        print("\nAnswer with 'true' or 'false'. +1 for correct, -1 for wrong.")
        print("You lose if your wrong tries hit the difficulty cap.\n")

        if not self._prompt_yes_no("Are we playing? (yes/no): "):
            print("\nFair enough. See you next time!\n")
            return False

        self.player_name = input("Your name: ").strip() or "Player"
        print(f"\nHi, {self.player_name}! Let's go!\n" + "-" * 55)
        allowed_wrong = self._prompt_difficulty()

        # round init
        self.score = 0
        self.wrong_answers = 0
        self.answers = {}
        self.attempts = 0
        self.max_streak = 0
        current_streak = 0

        game_over = False
        for question_text, correct_value in self._question_stream():
            if self.wrong_answers >= allowed_wrong:
                game_over = True
                break

            self.attempts += 1
            print("\n" + "=" * 40)
            print(f"Question:\n{question_text}\n")

            user = input("Answer 'true' or 'false': ").strip().lower()
            while user not in {"true", "false"}:
                user = input("Invalid. Please enter 'true' or 'false': ").strip().lower()

            is_correct = (user == correct_value)
            if is_correct:
                self.score += 1
                current_streak += 1
                self.max_streak = max(self.max_streak, current_streak)
                print(f"\n✅ Correct! Score: {self.score} | Streak: {current_streak}")
            else:
                self.wrong_answers += 1
                current_streak = 0
                print(f"\n❌ Wrong!  Score: {self.score} | Streak: {current_streak}")
            print("=" * 40)

            self.answers[question_text] = user
            self._append_answer(self.player_name, question_text, user, is_correct)

        # end of round
        print("\n" + "*" * 55)
        if game_over:
            print("Sorry, you lost!")
            completed = False
        else:
            print("No more questions left! You won — congrats!")
            completed = True

        print(f"Final score: {self.score}\n")
        self._append_score(self.player_name, self.score)
        self._append_summary(completed=completed, total_questions=len(self.answers))
        print("*" * 55 + "\n")
        return self._prompt_yes_no("One more game? (yes/no): ")


class LocalTrueFalseGame(TrueFalseGame):
    """Load statements from a local questions_pool.json (OpenTDB format)."""

    def __init__(self, path: Path, config: Optional[GameConfig] = None):
        self.local_path = Path(path)
        with open(self.local_path, "r", encoding="utf-8") as f:
            questions = json.load(f)
        # mimic API shape
        df = pd.DataFrame(questions)
        self.url = str(self.local_path)
        self.config = config or GameConfig()

        self.df = self._normalize(df)
        self.score = 0
        self.wrong_answers = 0
        self.answers = {}
        self.player_name = ""
        self.max_streak = 0
        self.attempts = 0
        self.fixed_total = len(self.df)
        self.difficulty_label = self.config.difficulty_label

        self.scores_df = self._ensure_csv(SCORES_CSV, ["Player", "Score"])  # type: ignore
        self.final_answers_df = self._ensure_csv(ANSWERS_CSV, ["Player", "Question", "Player_answer", "Correct"])  # type: ignore


if __name__ == "__main__":
    # Default: live API 10 Qs, category=9 (General Knowledge)
    cfg = GameConfig(amount=10)
    url = f"https://opentdb.com/api.php?amount={cfg.amount}&category={cfg.category}&type={cfg.qtype}"
    game = TrueFalseGame(url, cfg)
    while game.play():
        # reload fresh questions between rounds
        game = TrueFalseGame(url, cfg)