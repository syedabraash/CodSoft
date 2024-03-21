def simple_chatbot(user_input):
    
    user_input = user_input.lower()

    
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm here to assist you!",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "My name is Default Bot",
        "what time is it": "Sorry, I don't have the ability to tell time.",
        "thank you": "You're welcome!",
        "default": "I'm sorry, I didn't understand that."
    }

    for key in responses.keys():
        if key in user_input:
            return responses[key]

    return responses["default"]

def main():
    print("Welcome to the simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(simple_chatbot(user_input))
            break
        else:
            print("Bot:", simple_chatbot(user_input))

if __name__ == "__main__":
    main()
