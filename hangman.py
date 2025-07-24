import random

# Predefined word list
WORDS = ["apple", "table", "robot", "green", "beach"]

# Choose a random word
secret_word = random.choice(WORDS)
guessed_letters = []
attempts_remaining = 6

def display_current_progress():
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

print(" Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(f"You have {attempts_remaining} incorrect attempts allowed.\n")

# Game loop
while attempts_remaining > 0:
    print("Word: ", display_current_progress())
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print(" Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Good guess!\n")
    else:
        attempts_remaining -= 1
        print(f" Wrong guess! Attempts left: {attempts_remaining}\n")

    # Check win condition
    if all(letter in guessed_letters for letter in secret_word):
        print(f" Congratulations! You guessed the word: {secret_word}")
        break
else:
    print(f"Game Over! The word was: {secret_word}")
