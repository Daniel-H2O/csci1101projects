import re

# Get the answer.
answer = "What's up, Doc?"

answer = answer.upper()

# Pre-game setup.
anwer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        anwer_guessed.append(False)
    else: 
        anwer_guessed.appen(True)

# Game Logic
num_of_incorrect_guesses = 5

current_incorrect_guesses= 0

letters_guessed = []

# Let user play the game
while current_incorrect_guesses < num_of_incorrect_guesses and False in anwer_guessed:
    # Display game status
    print(f"Number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")