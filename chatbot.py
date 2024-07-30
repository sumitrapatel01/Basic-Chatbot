#pip install nltk

import nltk
from nltk.chat.util import Chat, reflections
import string

# Preprocess function to clean input text
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Sumitra.",]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing fine. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's okay, no need to apologize.",]
    ],
    [
        r"i'm (.*) doing good",
        ["Great to hear that!",]
    ],
    [
        r"i am (.*)",
        ["Nice to meet you %1. How can I help you today?",]
    ],
    [
        r"what is your favorite (.*)?",
        ["I don't have preferences, but I can help you with information about %1.",]
    ],
    [
        r"what is (.*)?",
        ["%1 is a very interesting topic. Let me tell you more about it.", "I don't have information on %1 right now, but I can help with something else."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you, answer your questions, and help with information.",]
    ],
    [
        r"can you help me with (.*)?",
        ["I can try to help you with %1. What do you need to know?",]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!",]
    ],
    [
        r"goodbye|bye|quit",
        ["Bye, take care!", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that. Can you rephrase?",]
    ]
]

# Chatbot function
def chatbot():
    print("Hi, I'm a chatbot created by ChatGPT. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    while True:
        user_input = input("> ")
        if user_input.lower() in ["quit", "bye", "goodbye"]:
            print("Bye, take care!")
            break
        preprocessed_input = preprocess(user_input)
        response = chat.respond(preprocessed_input)
        if not response:
            response = "I'm sorry, I don't understand that. Can you rephrase?"
        print(response)

if __name__ == "__main__":
    chatbot()
