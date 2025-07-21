
def expense_tracker():
    expenses = []
    print("Welcome to your Expense Tracker!")

    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Get total expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                amount = float(input("Enter amount: "))
                description = input("Enter description: ")
                expenses.append({"amount": amount, "description": description})
                print("Expense added.")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '2':
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nYour Expenses:")
                for i, expense in enumerate(expenses):
                    print(f"{i + 1}. {expense["description"]}: ${expense["amount"]:.2f}")
        elif choice == '3':
            total = sum(expense["amount"] for expense in expenses)
            print(f"\nTotal Expenses: ${total:.2f}")
        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    expense_tracker()
