import random

# 5 predefined words
word_list = ["apple", "banana", "cherry", "grapes", "orange"]

# Randomly choose a word
word_to_guess = random.choice(word_list)

# Create a list of underscores for the hidden word
hidden_word = ["_"] * len(word_to_guess)

# Track guessed letters and number of wrong guesses
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print(" ".join(hidden_word))

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in hidden_word:
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is in the word
    if guess in word_to_guess:
        print(f"✅ Good guess! '{guess}' is in the word.")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                hidden_word[index] = guess
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! You have {max_wrong_guesses - wrong_guesses} tries left.")

    # Show current progress
    print(" ".join(hidden_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")

# End game result
if "_" not in hidden_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game Over! The word was:", word_to_guess)