
def recipe_app():
    recipes = {}
    print("Welcome to the Recipe App!")

    while True:
        print("\nOptions:")
        print("1. Add a new recipe")
        print("2. View all recipes")
        print("3. View a specific recipe")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter recipe name: ")
            ingredients = input("Enter ingredients (comma-separated): ").split(',')
            instructions = input("Enter instructions: ")
            recipes[name] = {"ingredients": [i.strip() for i in ingredients], "instructions": instructions}
            print("Recipe added successfully!")
        elif choice == '2':
            if not recipes:
                print("No recipes available yet.")
            else:
                print("\n--- Your Recipes ---")
                for name in recipes:
                    print(f"- {name}")
        elif choice == '3':
            name = input("Enter the name of the recipe to view: ")
            if name in recipes:
                recipe = recipes[name]
                print(f"\n--- {name} ---")
                print("Ingredients:")
                for ingredient in recipe["ingredients"]:
                    print(f"- {ingredient}")
                print("\nInstructions:\n{recipe["instructions"]}")
            else:
                print("Recipe not found.")
        elif choice == '4':
            print("Exiting Recipe App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    recipe_app()
