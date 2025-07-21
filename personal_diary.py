
import datetime

def personal_diary():
    diary_file = "diary.txt"
    print("Welcome to your Personal Diary!")

    while True:
        print("\nOptions:")
        print("1. Add a new entry")
        print("2. View all entries")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            entry_title = input("Enter entry title: ")
            entry_content = input("Enter your diary entry: ")
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            with open(diary_file, "a") as f:
                f.write(f"Date: {timestamp}\n")
                f.write(f"Title: {entry_title}\n")
                f.write(f"Entry:\n{entry_content}\n")
                f.write("--------------------\n")
            print("Entry added successfully!")
        elif choice == '2':
            try:
                with open(diary_file, "r") as f:
                    content = f.read()
                    if content:
                        print("\n--- Your Diary Entries ---")
                        print(content)
                    else:
                        print("Your diary is empty.")
            except FileNotFoundError:
                print("Your diary is empty.")
        elif choice == '3':
            print("Exiting Personal Diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    personal_diary()
