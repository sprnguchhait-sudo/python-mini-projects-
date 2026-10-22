"""Task 4: A small rule-based chatbot."""


def get_reply(message: str) -> str:
    """Return a response based on a normalized user message."""
    message = message.strip().lower()
    if message in {"hello", "hi", "hey"}:
        return "Hi! Nice to meet you."
    elif message in {"how are you", "how are you?"}:
        return "I'm fine, thanks! How can I help you?"
    elif message in {"what is your name", "what's your name"}:
        return "I'm PyBot, a simple rule-based chatbot."
    elif message == "help":
        return "Try saying hello, asking how I am, or typing bye to exit."
    elif message in {"bye", "goodbye", "exit", "quit"}:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don't understand that yet. Type 'help' to see examples."


def main():
    print("PyBot: Hello! Type 'help' for examples, or 'bye' to exit.")
    while True:
        user_message = input("You: ")
        reply = get_reply(user_message)
        print("PyBot:", reply)
        if user_message.strip().lower() in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
