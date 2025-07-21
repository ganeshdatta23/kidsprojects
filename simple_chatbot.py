
def simple_chatbot():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm a chatbot, so I don't have feelings, but I'm ready to help!")
        elif "name" in user_input:
            print("Chatbot: I don't have a name. I'm just a simple chatbot.")
        elif "help" in user_input:
            print("Chatbot: I can answer simple questions. Try asking about my name or how I am.")
        else:
            print("Chatbot: I'm not sure how to respond to that.")

if __name__ == "__main__":
    simple_chatbot()
