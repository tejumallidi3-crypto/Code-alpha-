def chatbot():
    print("=== BASIC PYTHON CHATBOT ===")
    print("Type 'bye' to exit.")

    responses = {
        "hello": "Hi! How can I help you?",
        "hi": "Hello! Nice to meet you.",
        "how are you": "I'm doing great. Thanks for asking!",
        "what is your name": "I'm a simple Python chatbot.",
        "thanks": "You're welcome!",
        "thank you": "You're welcome!"
    }

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "bye":
            print("Bot: Goodbye! Have a great day!")
            break

        if user_input in responses:
            print("Bot:", responses[user_input])
        else:
            print("Bot: Sorry, I don't understand that yet.")


if __name__ == "__main__":
    chatbot()
