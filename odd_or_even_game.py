
def odd_or_even_game():
    print("Welcome to the Odd or Even Game!")
    while True:
        try:
            number = int(input("Enter a number (or 0 to quit): "))
            if number == 0:
                break
            if number % 2 == 0:
                print(f"The number {number} is Even.")
            else:
                print(f"The number {number} is Odd.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    odd_or_even_game()
