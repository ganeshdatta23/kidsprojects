
def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def palindrome_checker():
    print("Welcome to the Palindrome Checker!")
    while True:
        word = input("Enter a word or phrase (or 'quit' to exit): ")
        if word.lower() == 'quit':
            break
        if not word.strip():
            print("Please enter some text.")
            continue

        if is_palindrome(word):
            print(f"'{word}' is a palindrome!")
        else:
            print(f"'{word}' is not a palindrome.")

if __name__ == "__main__":
    palindrome_checker()
