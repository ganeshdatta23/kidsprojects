

import random

def word_guessing_game():
    words = ["python", "java", "kotlin", "javascript", "ruby", "swift"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to the Word Guessing Game!")

    while attempts > 0:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts}")

        if display_word == word_to_guess:
            print("Congratulations! You guessed the word.")
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
        else:
            attempts -= 1
            print("Incorrect guess.")

    if attempts == 0:
        print(f"\nGame over! The word was '{word_to_guess}'.")

if __name__ == "__main__":
    word_guessing_game()

