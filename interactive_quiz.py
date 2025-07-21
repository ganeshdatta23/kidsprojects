
def interactive_quiz():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the color of the sky?": "Blue"
    }
    score = 0

    print("Welcome to the Interactive Quiz!")

    for question, answer in questions.items():
        user_answer = input(f"\n{question} ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}")

    print(f"\nYou got {score} out of {len(questions)} questions correct.")

if __name__ == "__main__":
    interactive_quiz()

