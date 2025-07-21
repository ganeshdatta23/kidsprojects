
import random

def rock_paper_scissors_game():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user_choice == 'quit':
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    rock_paper_scissors_game()

