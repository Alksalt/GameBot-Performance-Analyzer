import random


def generate_code(length=4, digit_range=10):
    """
    Generate a secret code as a list of integers.
    - length: number of digits in the code.
    - digit_range: the digits will be in the range 0 to digit_range-1.
    """
    return [random.randint(0, digit_range - 1) for _ in range(length)]


def get_feedback(guess, code):
    """
    Compare the player's guess to the secret code and return feedback.

    Returns:
      - hits: Number of digits that are correct and in the correct position.
      - pseudo_hits: Number of correct digits but in the wrong position.

    Both lists (guess and code) are assumed to be of the same length.
    """
    # First, count exact matches (hits)
    hits = sum(g == c for g, c in zip(guess, code))

    # Count occurrences in positions that are not hits
    code_freq = {}
    guess_freq = {}
    for g, c in zip(guess, code):
        if g != c:
            code_freq[c] = code_freq.get(c, 0) + 1
            guess_freq[g] = guess_freq.get(g, 0) + 1

    # Calculate pseudo-hits by comparing frequency counts
    pseudo_hits = 0
    for digit in guess_freq:
        if digit in code_freq:
            pseudo_hits += min(guess_freq[digit], code_freq[digit])

    return hits, pseudo_hits


def play_game():
    """
    Main game loop.
    The player has a limited number of attempts to guess the secret code.
    After each guess, feedback is provided.
    """
    code_length = 4
    max_attempts = 10
    secret_code = generate_code(length=code_length, digit_range=10)

    print("Welcome to Mastermind!")
    print(f"I have generated a {code_length}-digit secret code (digits 0-9).")
    print("After each guess, you'll receive feedback:")
    print(" - Hits: Correct digit in the correct position.")
    print(" - Pseudo-hits: Correct digit but in the wrong position.\n")

    attempts = 0
    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your {code_length}-digit guess: ")

        # Validate input: must be the correct length and all digits
        if len(guess_input) != code_length or not guess_input.isdigit():
            print(f"Please enter exactly {code_length} digits (0-9).\n")
            continue

        # Convert input string into a list of integers
        guess = [int(digit) for digit in guess_input]
        attempts += 1

        hits, pseudo_hits = get_feedback(guess, secret_code)

        if hits == code_length:
            print(f"Congratulations! You cracked the code in {attempts} attempts!")
            break
        else:
            print(f"Hits: {hits}, Pseudo-hits: {pseudo_hits}\n")
    else:
        # If the loop completes without a break, the player ran out of attempts
        code_str = ''.join(str(d) for d in secret_code)
        print(f"Sorry, you've run out of attempts. The secret code was: {code_str}")


if __name__ == "__main__":
    play_game()