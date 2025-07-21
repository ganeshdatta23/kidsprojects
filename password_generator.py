
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    try:
        length = int(input("Enter the desired length of the password (or 0 to quit): "))
        if length == 0:
            break
        if length < 4:
            print("Password length should be at least 4.")
            continue
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")
