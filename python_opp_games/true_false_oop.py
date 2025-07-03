import pandas as pd
import requests
import os
import datetime
import json

class TrueFalseGame:
    """
    A class to manage a True/False trivia game with questions loaded from an API.
    Supports different difficulty levels, saving results, and score tracking.
    """

    def __init__(self, url):
        """
        Initialize the game with a URL for question data.
        Loads high scores and player answers if CSV files exist.

        Args:
            url (str): The API endpoint to load questions from.
        """
        self.df = self.load_statements(url)
        self.url = url
        self.score = 0
        self.wrong_answers = 0
        self.your_answers = {}
        self.name = ''

        try:
            self.df2 = pd.read_csv("scores.csv")
        except FileNotFoundError:
            self.df2 = pd.DataFrame(columns=['Player', 'Score'])

        try:
            self.final_answers = pd.read_csv('Final_answers.csv')
        except FileNotFoundError:
            self.final_answers = pd.DataFrame(columns=['Player', 'Question', "Player's answer"])

    def load_statements(self, url):
        """
        Fetches True/False statements from the API, returns as a DataFrame.

        Args:
            url (str): The API endpoint to load questions from.

        Returns:
            pd.DataFrame: DataFrame with questions and answers.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if "results" in data:
                return pd.DataFrame(data["results"])
            else:
                print("\n" + "!"*40)
                print("Error: Unexpected API response format!")
                print("!"*40 + "\n")
                return pd.DataFrame()
        except requests.exceptions.RequestException as e:
            print("\n" + "!"*40)
            print(f"Error fetching data: {e}")
            print("!"*40 + "\n")
            return pd.DataFrame()

    def generate_statements(self):
        """
        Generator that yields a tuple (statement, truth_value) for each question, removing it from the DataFrame.

        Yields:
            tuple: (statement, truth_value)
        """
        while not self.df.empty:
            random_row = self.df.sample(n=1).iloc[0]
            st, truth_value = random_row['question'], random_row['correct_answer'].lower()
            self.df = self.df.drop(random_row.name)
            yield st, truth_value
        print('\n' + '-'*40)
        print('No more questions left')
        print('-'*40 + '\n')
        return

    def play_game(self):
        """
        Start the game. Prompts user if they want to play and asks for the player name.

        Returns:
            bool: True if the player wants to play, False otherwise.
        """
        print('\n' + '='*55)
        print('Welcome to the True or False game!')
        print('='*55)
        print('\nYou need to answer "true" or "false".')
        print('For each right answer you earn +1, and for each wrong answer score goes down (-1).\n')
        print('For score < 0   -->   You lose')
        print('For score = 0   -->   Tie')
        print('For score > 0   -->   You win')
        print('For score > 10  -->   You are the champion!\n')
        print('-'*55)
        print('If you are ready to start, let\'s begin!\n')

        while True:
            play = input('Are we playing? (yes/no): ').lower().strip()
            if play == 'yes':
                print()
                self.name = input('Name yourself: ')
                print(f'\nHi, {self.name}! Let\'s play then!\n')
                print('-' * 55)
                return True
            elif play == 'no':
                print("\nSo sad. See you next time :)\n")
                return False

    def dif(self):
        """
        Prompts user to choose difficulty level.

        Returns:
            int or None: Number of allowed wrong attempts (None for unlimited/easy).
        """
        print('\n' + '='*55)
        print('Choose a difficulty level:')
        print('  easy   = unlimited tries')
        print('  medium = 3 wrong tries allowed')
        print('  hard   = just 1 wrong try allowed')
        print('='*55)
        lvls = {'easy': None, 'medium': 2, 'hard': 3}
        diff = input('\nChoose between: easy/medium/hard: ').lower().strip()
        while diff not in ['easy', 'medium', 'hard']:
            print('\nYou have to choose between easy/medium/hard. Try again.')
            diff = input('Choose between: easy/medium/hard: ').lower().strip()
        print(f'\nYou chose "{diff}" mode.\n' + '-'*55)

        self.difficulty_label = diff

        return lvls[diff]

    def one_more(self):
        """
        Asks the user if they want to play one more game.

        Returns:
            bool: True if yes, False otherwise.
        """
        print('\n' + '-'*40)
        game_more = input('One more game? (yes/no): ').strip().lower()
        while game_more not in ['yes', 'no']:
            game_more = input('One more game? (yes/no): ').strip().lower()
        print('-'*40)
        if game_more == 'yes':
            print('\nRestarting the game...\n')
            return True
        else:
            print('\nThanks for playing!')
            return False

    def reset_statements(self):
        """
        Resets questions and scores to start a new game round.
        """
        self.df = self.load_statements(self.url)
        self.score = 0
        self.wrong_answers = 0
        self.your_answers = {}



    def table_score(self, player, score):
        """
        Records the player's score in the 'scores.csv' file.

        Args:
            player (str): Name of the player.
            score (int): The final score.
        """
        new_entry = pd.DataFrame([[player, score]], columns=["Player", "Score"])
        self.df2 = pd.concat([self.df2, new_entry], ignore_index=True)
        return self.df2.to_csv("scores.csv", index=False)

    def writing_answers(self, player, question, answer):
        """
        Records player's answers to the 'Final_answers.csv' file.

        Args:
            player (str): Name of the player.
            question (str): The trivia question.
            answer (str): The player's answer.
        """
        new_entry = pd.DataFrame([[player, question, answer]], columns=['Player', 'Question', "Player's answer"])
        self.final_answers = pd.concat([self.final_answers, new_entry], ignore_index=True)
        return self.final_answers.to_csv("Final_answers.csv", index=False)

    def start_game(self):
        """
        Main loop for playing the game, managing rounds, checking win/lose conditions,
        and prompting for replay. Also saves summary analytics at the end of each game.
        """
        while True:
            if not self.play_game():
                return

            difficulty = self.dif()
            statements = self.generate_statements()
            game_over = False

            for st, true_value in statements:
                # Check losing conditions BEFORE asking the question:
                if (difficulty == 2 and self.wrong_answers >= 3) or \
                        (difficulty == 3 and self.wrong_answers >= 1):
                    game_over = True
                    break

                print('\n' + '=' * 40)
                print(f'Question:\n{st}\n')
                answer = input("Answer 'true' or 'false': ").lower().strip()
                while answer not in ["true", "false"]:
                    answer = input("Invalid input. Please enter 'true' or 'false': ").lower().strip()

                # Process answer:
                if answer == true_value:
                    self.score += 1
                    print("\n✅ Correct! Your score is", self.score)
                else:
                    self.wrong_answers += 1
                    print("\n❌ Wrong! Your score is", self.score)
                print('=' * 40)
                self.your_answers[st] = answer

            # --- End of the round/game ---
            print('\n' + '*' * 55)
            if game_over:
                print("Sorry, you lost!")
                completed = False
            else:
                print("No more questions left!")
                print('You won!!! Congrats!!!')
                completed = True

            print(f"The game is over. Your final score is {self.score}.\n")
            print('Your answers:')
            print('-' * 55)
            for k, v in self.your_answers.items():
                self.writing_answers(self.name, k, v)
                print(f"Statement: {k}\nYour answer: {v}\n")

            self.table_score(self.name, self.score)
            self.save_game_summary(completed)  # <-- Analytics call
            print('*' * 55 + '\n')

            if not self.one_more():
                print('\nSo sad, see you next time :)\n')
                return

            self.reset_statements()


    def save_game_summary(self, completed):
        """
        Save metrics from the current game into the CSV.
        """
        total_questions = len(self.your_answers)
        accuracy = round(self.score / total_questions, 2) if total_questions > 0 else 0
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new_entry = pd.DataFrame([[
            self.name,
            self.score,
            self.wrong_answers,
            total_questions,
            accuracy,
            self.difficulty_label,
            date,
            completed
        ]], columns=[
            'Player', 'Score', 'Wrong', 'Total_questions', 'Accuracy', 'Difficulty', 'Date', 'Completed'
        ])
        try:
            summary_df = pd.read_csv("game_summary.csv")
        except FileNotFoundError:
            summary_df = pd.DataFrame(columns=new_entry.columns)
        summary_df = pd.concat([summary_df, new_entry], ignore_index=True)
        summary_df.to_csv("game_summary.csv", index=False)

class LocalTrueFalseGame(TrueFalseGame):
    def load_statements(self, path):
        with open(path, 'r') as f:
            questions = json.load(f)
        return pd.DataFrame(questions)

if __name__ == "__main__":
    game = TrueFalseGame("https://opentdb.com/api.php?amount=10&category=9&type=boolean")
    game.start_game()

