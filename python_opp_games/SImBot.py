import random
import time
from true_false_oop import TrueFalseGame, LocalTrueFalseGame


def smart_bot_answer(true_value, correct_prob=0.7):
    if random.random() < correct_prob:
        return true_value
    else:
        return random.choice(['true', 'false'])

def bot_random(true_value):
    correct_prob = random.choice([0.1, 0.3, 0.2, 0.3, 0.4, 0.4, 0.5, 0.6, 0.7])
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
    allowed_wrongs = 2 if difficulty == 'medium' else None
    #

    N = 10
    game.df = game.df.sample(n=N) if len(game.df) >= N else game.df

    statements = game.generate_statements()
    game_over = False

    for idx, (st, true_value) in enumerate(statements):
        if allowed_wrongs == 2 and game.wrong_answers >= 3:
            game_over = True
            break

        # 70% correct for first 5, then drops to 50%
        #correct_prob = 0.7 if idx < 5 else 0.5
        answer = bot_random(true_value)

        if answer == true_value:
            game.score += 1
        else:
            game.wrong_answers += 1
        game.your_answers[st] = answer

    #for k, v in game.your_answers.items():
    #    game.writing_answers(game.name, k, v)

    completed = not game_over
    game.table_score(game.name, game.score)
    game.save_game_summary(completed)
    return {'Player': game.name, 'Score': game.score, 'Completed': completed}

if __name__ == "__main__":
    difficulties = ['easy', 'medium', 'hard']
    for i in range(10000):
        random_difficulty = random.choice(difficulties)
        random_name = random.randint(1,20)
        print(simulate_game(bot_name=f"RandomBot{random_name}", difficulty=random_difficulty))