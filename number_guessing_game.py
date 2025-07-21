
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    print("Welcome to the Number Guessing Game!")
    while guess != number_to_guess:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
        except ValueError:
            print("Invalid input. Please enter a number.")
    print("Congratulations! You guessed the number.")

if __name__ == "__main__":
    number_guessing_game()
