import random
import json
from datetime import datetime

print("AI Assistant Online")
print("Type 'help' for commands or 'exit' to quit.\n")

user_name = ""
favorite_color = ""
last_message = ""
message_history = []
try:
    with open("memory.json", "r") as file:
        memory = json.load(file)

    user_name = memory.get("name", "")
    favorite_color = memory.get("favorite_color", "")

except (FileNotFoundError, json.JSONDecodeError):
    pass
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Why did the computer go to therapy? It had too many bytes from its past.",
    "There are 10 kinds of people: those who understand binary and those who don't."
]

advice_messages = [
    "Progress beats perfection.",
    "Every bug teaches you something.",
    "Start small, test often, and keep going.",
    "Working code is worth celebrating.",
    "You do not have to understand everything at once."
]
def save_memory(user_name, favorite_color):
    memory = {
        "name": user_name,
        "favorite_color": favorite_color
    }

    with open("memory.json", "w") as file:
        json.dump(memory, file)


while True:
    user_input = input("You: ").strip()
    command = user_input.lower()
    words = command.split()
    if command in ["exit", "quit", "bye"]:
        save_memory(user_name, favorite_color)
        print("AI: Memory saved. Shutting down...")
        break

    elif command == "help":
        print(
            "AI: Try: time, joke, hello (hi, hey), name, profile, "
            "about, what is my favorite color, advice, add (or: add 5 and 3), "
            "how are you, what are you, favorite color, "

            "last message, history, clear history, who made you, "
            "or exit (quit, bye)"
        )

    elif command == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("AI: The current time is " + current_time)

    elif command == "joke":
        print("AI:", random.choice(jokes))

    elif command == "advice":
        print("AI:", random.choice(advice_messages))

    elif command == "name":
        new_name = input("AI: What should I call you?\nYou: ").strip()

        if new_name:
            user_name = new_name
            save_memory(user_name, favorite_color)
            print("AI: Nice to meet you, " + user_name + "!")
        else:
            print("AI: You didn't enter a name. I'll keep the previous one.")
    elif command in ["hello", "hi", "hey"]:
        if user_name:
            print("AI: Hello, " + user_name + "!")
        else:
            print("AI: Hello! Use the 'name' command so I know what to call you.")

    elif command == "favorite color":
        new_color = input(
            "AI: What is your favorite color?\nYou: "
        ).strip()

        if new_color:
            favorite_color = new_color
            save_memory(user_name, favorite_color)
            print("AI: I'll remember that your favorite color is " + favorite_color + ".")
        else:
            print("AI: You didn't enter a color. I'll keep the previous one.")

    elif command == "what is my favorite color":
        if favorite_color:
            print("AI: Your favorite color is " + favorite_color + ".")
        else:
            print("AI: You haven't told me your favorite color yet.")
    elif len(words) == 4 and words[0] == "add" and words[2] == "and":
        try:
            first_number = float(words[1])
            second_number = float(words[3])
            total = first_number + second_number
            print("AI: The answer is", total)

        except ValueError:
            print("AI: Please enter valid numbers, like: add 5 and 3")
    elif command == "add":
        first_number = input("AI: Enter the first number.\nYou: ")
        second_number = input("AI: Enter the second number.\nYou: ")

        try:
            first_number = float(first_number)
            second_number = float(second_number)

            total = first_number + second_number
            print("AI: The answer is", total)

        except ValueError:
            print("AI: Please enter valid numbers.")

    elif command == "how are you":
        responses = [
            "I'm doing great and ready to help.",
            "I'm online and learning.",
            "I'm feeling very Pythonic today."
        ]
        print("AI:", random.choice(responses))

    elif command == "who made you":
        print("AI: Chance created me using Python.")

    elif command == "what are you":
        print("AI: I am a command-based Python assistant.")
    elif command == "profile":
        print("AI: Your profile:")
        print("Name:", user_name or "Not set")
        print("Favorite color:", favorite_color or "Not set")
    elif command == "about":
        print("AI: I am a Python assistant created by Chance.")
        print("AI: I can remember information, tell jokes, give advice, and do math.")

    elif command == "history":
        if message_history:
            print("AI: Here is your message history:")
            for number, message in enumerate(message_history, start=1):
                print(str(number) + ". " + message)
        else:
            print("AI: Your message history is empty.")
    elif command == "clear history":
        message_history.clear()
        last_message = ""
        print("AI: Your message history has been cleared.")
    elif command == "last message":
        if last_message:
            print("AI: Your previous message was: " + last_message)
        else:
            print("AI: I don't have a previous message to remember yet.")

    elif command == "":
        print("AI: Please type something.")

    else:
        print("AI: I don't understand that command yet. Type 'help' for options.")

    if command not in ["last message", "history", "clear history", ""]:
        last_message = user_input
        message_history.append(user_input)