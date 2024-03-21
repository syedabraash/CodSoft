import re
import random

greetings_responses = [
    "Hello! How can I help you with your table tennis queries?",
    "Hi there! Ready to talk about table tennis?",
    "Hey! What table tennis questions do you have?",
]

table_tennis_responses = {
    "serve": "In table tennis, the serve is the starting shot of a point. It must bounce once on the server's side and once on the opponent's side of the table.",
    "rally": "A rally in table tennis is a sequence of shots between the server and the receiver until a point is won or lost.",
    "forehand": "A forehand stroke in table tennis is a shot made by swinging the racket across the body with the front of the hand facing the direction of the stroke.",
    "backhand": "A backhand stroke in table tennis is a shot made by swinging the racket across the body with the back of the hand facing the direction of the stroke.",
    "ping pong": "Ping pong is another name for table tennis, often used informally.",
    "equipment": "Table tennis equipment includes a racket (or paddle) and a table tennis ball. The racket consists of a blade and rubber covering on both sides.",
    "table tennis rules": "Table tennis has rules regarding service, scoring, and gameplay. It is played to 11 points, with alternate serves and a two-point advantage to win a game.",
    "table tennis clubs": "Table tennis clubs are places where players can gather to play, practice, and compete with each other.",
    "table tennis tournaments": "Table tennis tournaments are competitive events where players compete against each other to win titles and prizes.",
    "table tennis techniques": "Table tennis techniques include various strokes, footwork, and strategies used to play the game effectively.",
    "table tennis history": "Table tennis, also known as ping pong, originated in England in the late 19th century as an indoor version of lawn tennis.",
    "table tennis grip": "The grip in table tennis refers to how a player holds the racket. Common grips include shakehand grip and penhold grip.",
    "table tennis serve rules": "Table tennis serve rules specify how the serve must be performed, including tossing the ball vertically and hitting it so that it bounces once on each side of the table.",
    "table tennis doubles": "Table tennis doubles is a variation of the game played with two players on each side of the table.",
    "table tennis techniques": "Table tennis techniques include various strokes, footwork, and strategies used to play the game effectively.",
    "table tennis scoring": "Table tennis scoring is based on a rally system, where a point is awarded to the player who wins each rally. A game is won by the first player to reach 11 points with a two-point advantage.",
    "table tennis serve spin": "Table tennis serve spin refers to the spin imparted on the ball by the server, which can affect its trajectory and bounce.",
    "table tennis serve placement": "Table tennis serve placement refers to where the server aims to land the ball on the opponent's side of the table, often used to set up advantageous positions for the server.",
    "table tennis serve tactics": "Table tennis serve tactics involve varying the spin, speed, and placement of serves to keep opponents off balance and gain an advantage in the rally.",
    "table tennis serve rules": "Table tennis serve rules specify how the serve must be performed, including tossing the ball vertically and hitting it so that it bounces once on each side of the table.",
    "table tennis serve techniques": "Table tennis serve techniques include pendulum serve, backhand serve, tomahawk serve, and other variations used to generate spin and deception.",
    "table tennis serve spin": "Table tennis serve spin refers to the rotation of the ball caused by the motion of the racket at the moment of contact.",
    "table tennis serve grip": "The grip used for serving in table tennis may vary depending on the type of serve being performed, with players often adjusting their grip to generate spin and control.",
    "table tennis serve faults": "Table tennis serve faults occur when a player violates the rules of service, such as failing to toss the ball vertically or failing to strike it so that it bounces on both sides of the table.",
    "table tennis serve tactics": "Table tennis serve tactics involve using a variety of serves to keep opponents guessing and gain an advantage in the rally.",
    "table tennis serve drills": "Table tennis serve drills are exercises designed to improve a player's serving technique, consistency, and placement.",
    "table tennis serve receive": "Table tennis serve receive is the act of returning the opponent's serve, often requiring quick reflexes and good anticipation of the ball's spin and placement.",
    "table tennis serve return": "Table tennis serve return is the shot made by the receiver in response to the opponent's serve, often aimed at gaining an advantage in the rally.",
    "table tennis serve return tactics": "Table tennis serve return tactics involve anticipating the opponent's serve, adjusting one's position, and choosing an appropriate shot to neutralize the serve and gain control of the rally.",
    "table tennis serve return techniques": "Table tennis serve return techniques include blocking, looping, pushing, and flicking, each used to counter different types of serves and gain an advantage in the rally.",
    "table tennis serve return spin": "Table tennis serve return spin refers to the spin imparted on the ball by the receiver's racket when returning the opponent's serve, which can affect the trajectory and bounce of the ball.",
    "table tennis serve return placement": "Table tennis serve return placement refers to where the receiver aims to land the ball on the opponent's side of the table when returning the serve, often used to set up advantageous positions for the receiver.",
    "table tennis serve return drills": "Table tennis serve return drills are exercises designed to improve a player's ability to return various types of serves with accuracy, consistency, and placement.",
    "table tennis serve return tactics": "Table tennis serve return tactics involve analyzing the opponent's serve, predicting its trajectory and spin, and choosing an appropriate shot to counter the serve and gain an advantage in the rally.",
    "table tennis serve return grip": "The grip used for returning serves in table tennis may vary depending on the type of shot being executed, with players often adjusting their grip to generate spin, control, and power.",
    "table tennis serve return faults": "Table tennis serve return faults occur when a player fails to return the opponent's serve within the rules, such as failing to make a legal return or failing to keep the ball in play.",
}

default_responses = [
    "I'm sorry, I didn't understand your question. Can you please rephrase?",
    "Hmm, I'm not sure what you're asking. Could you provide more details?",
    "I'm still learning about table tennis. Could you ask me something else?",
]

def chatbot(user_input):
    user_input = user_input.lower()

    if any(greeting in user_input for greeting in ["hello", "hi", "hey", "howdy", "hola"]):
        return random.choice(greetings_responses)

    for keyword, response in table_tennis_responses.items():
        if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
            return response

    return random.choice(default_responses)

def main():
    print("Welcome to the Table Tennis Chatbot!")
    print("Ask me anything about table tennis, or just say hello!")
    print("Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Bot:", chatbot(user_input))
#
if __name__ == "__main__":
    main()
