import random

print("AI Assistant Online")
print("Type 'help', 'time', 'joke', or 'exit'\n")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "I would tell you a UDP joke, but you might not get it.",
    "Why did the Python developer wear glasses? Because he couldn’t C."
]

user_name = ""

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("AI: Shutting down...")
        break

    elif user_input == "help":
        print("AI: Try: time, joke, hello, name, about, or anything else")

    elif user_input == "time":
        print("AI: I still don’t know real time yet, but I’m learning.")

    elif user_input == "joke":
        print("AI:", random.choice(jokes))

    elif user_input == "hello" or user_input == "hi":
        print("AI: Hello! I'm your assistant.")

    elif user_input.startswith("my name is "):
        user_name = user_input.replace("my name is ", "")
        print("AI: Nice to meet you, " + user_name.title() + ".")

    elif user_input == "name":
        if user_name:
            print("AI: Your name is " + user_name.title() + ".")
        else:
            print("AI: I don't know your name yet. Try saying: my name is Chance")

    elif user_input == "about":
        print("AI Assistant v0.2")
        print("AI: I can respond to greetings, tell jokes, and remember your name for this session.")

    else:
        print("AI: Interesting... tell me more about -> " + user_input)