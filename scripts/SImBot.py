import random
import time
from true_false_oop import TrueFalseGame, LocalTrueFalseGame


def smart_bot_answer(true_value, correct_prob=0.7):
    if random.random() < correct_prob:
        return true_value
    else:
        return random.choice(['true', 'false'])

def get_correct_prob(difficulty, idx):
    if difficulty == 'easy':
        return 0.8 if idx < 5 else 0.6
    elif difficulty == 'medium':
        return 0.55 if idx < 5 else 0.35
    elif difficulty == 'hard':
        return 0.25 if idx < 5 else 0.1


def bot_random(true_value):
    #correct_prob = random.choice([0.1, 0.3, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7])
    correct_prob = random.choice([0.1, 0.2])
    if random.random() < correct_prob:
        return true_value
    else:
        return random.choice(['true', 'false'])

def simulate_game(bot_name="SmartBot", difficulty='medium'):
    game = LocalTrueFalseGame("/Users/alt/Library/CloudStorage/OneDrive-Personal/pythonProject/python_opp_games/questions_pool.json")
    if game.df.empty:
        print(f"Bot '{bot_name}': No questions fetched. Skipping this simulation.")
        return None

    game.name = bot_name
    game.difficulty_label = difficulty

    if difficulty == 'easy':
        allowed_wrongs = 3
    elif difficulty == 'medium':
        allowed_wrongs = 2
    elif difficulty == 'hard':
        allowed_wrongs = 1

    N = 10
    game.df = game.df.sample(n=N) if len(game.df) >= N else game.df

    statements = game.generate_statements()
    game_over = False

    attempts = 0
    current_streak = max_streak = 0

    for idx, (st, true_value) in enumerate(statements):
        attempts += 1
        if allowed_wrongs is not None and game.wrong_answers > allowed_wrongs:
            game_over = True
            break

        # 70% correct for first 5, then drops to 50%
        #correct_prob = 0.7 if idx < 5 else 0.5
        correct_prob = get_correct_prob(difficulty, idx)
        answer = smart_bot_answer(true_value, correct_prob=correct_prob)

        if answer == true_value:
            game.score += 1
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            game.wrong_answers += 1
            current_streak = 0

    #for k, v in game.your_answers.items():
    #    game.writing_answers(game.name, k, v)

    game.attempts = attempts
    game.fixed_total = N
    game.max_streak = max_streak

    completed = not game_over
    game.table_score(game.name, game.score)
    game.save_game_summary(completed)
    return {'Player': game.name, 'Score': game.score, 'Completed': completed}

if __name__ == "__main__":
    difficulties = ['easy','medium', 'hard']
    for i in range(3000):
        random_difficulty = random.choice(difficulties)
        random_name = random.randint(1,20)
        print(simulate_game(bot_name=f"SmartBot{random_name}", difficulty='medium'))