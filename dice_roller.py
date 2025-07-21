
import random

def dice_roller():
    print("Welcome to the Dice Roller!")
    while True:
        input("Press Enter to roll the dice (or type 'quit' to exit): ")
        
        roll = random.randint(1, 6)
        print(f"You rolled a {roll}!")

        choice = input("Roll again? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    dice_roller()
