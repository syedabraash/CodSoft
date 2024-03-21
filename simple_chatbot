def simple_chatbot(user_input):
    # Convert user input to lowercase for easier processing
    user_input = user_input.lower()

    # Predefined rules and responses
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm here to assist you!",
        "bye": "Goodbye! Have a great day!",
        "what is your name": "My name is Default Bot",
        "what time is it": "Sorry, I don't have the ability to tell time.",
        "thank you": "You're welcome!",
        "default": "I'm sorry, I didn't understand that."
    }

    # Check if user input matches any predefined rules
    for key in responses.keys():
        if key in user_input:
            return responses[key]

    # If no match found, return default response
    return responses["default"]

# Main function to run the chatbot
def main():
    print("Welcome to the simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(simple_chatbot(user_input))
            break
        else:
            print("Bot:", simple_chatbot(user_input))

# Run the chatbot
if __name__ == "__main__":
    main()
