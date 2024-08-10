import random

print("==============================")
title = "Word Scramble".upper()
print(title.center(30, "="))
print("==============================")
print("Instructions:\n-- Choose a level between 1-3.\n-- A random word is scrambled.\n-- Try to guess the word.\n-- You have 3 attempts.\n-- Goodluck!")

#words seperated by levels
def word_scramble():
    words_by_level = {
        1: [
            "cat", "dog", "fish", "bat", "ant", "rat", "cow", "pig", "fox", "hen",
            "bee", "owl", "elk", "ape", "deer", "lion", "tiger", "bear", "frog", "seal",
            "goat", "eagle", "hawk", "lamb", "duck"
        ],
        2: [
            "python", "scramble", "arcade", "guitar", "piano", "drum", "dance", "paint", "juggle", "write",
            "sail", "swing", "jump", "build", "draw", "scoop", "sprint", "kick", "twirl", "cycle",
            "flute", "trumpet", "violin", "origami", "fossil"
        ],
        3: [
            "programming", "enthusiastic", "development", "algorithm", "abstraction", "inheritance", "encapsulation", "polymorphism", "constructor", "framework",
            "database", "repository", "asynchronous", "synchronous", "debugging", "optimization", "deployment", "interface", "iteration", "refactoring",
            "exception", "inheritance", "serialization", "virtualization", "scripting"
        ]
    }

    while True:
        level = input("Choose a level of difficulty (1/2/3): ")
        if level.isdigit():
            level = int(level)
            if level in words_by_level:
                break
            else:
                print("Invalid level 🚫 Please choose a valid level (1/2/3).")
        else:
            print("Invalid input 🚫 Please enter a number (1/2/3).")

    words = words_by_level[level]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))

    print(f"Unscramble the word: {scrambled}")

    attempts = 3
    while attempts > 0:
        guess = input(f"You have {attempts} attempts left: ").lower()
        if guess == word:
            print("Correct! 🥳 You've unscrambled the word!")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print("Incorrect ❌ Try again.")
            else:
                print(f"You've run out of guesses 😔 The correct word was: {word}\nBetter luck next time")

    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y':
            break
        elif play_again == 'n':
            print("Goodbye! 👋")
            return
        else:
            print("Invalid input 🚫 Please enter y/n.")

word_scramble()

