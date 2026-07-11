import random
from datetime import datetime

print("AI Assistant Online")
print(
    "Type 'help', 'time', 'joke', 'name', 'about', "
    "'favorite color', 'advice', 'add', or 'exit'\n"
)

user_name = ""
favorite_color = ""

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

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "exit":
        print("AI: Shutting down...")
        break

    elif user_input == "help":
        print(
            "AI: Try: time, joke, hello, name, about, "
            "favorite color, what is my favorite color, "
            "advice, add, how are you, who made you, or exit"
        )

    elif user_input == "time":
        current_time = datetime.now().strftime("%I:%M %p")
        print("AI: The current time is " + current_time)

    elif user_input == "joke":
        print("AI:", random.choice(jokes))

    elif user_input == "advice":
        print("AI:", random.choice(advice_messages))

    elif user_input == "name":
        user_name = input("AI: What should I call you?\nYou: ").strip()

        if user_name:
            print("AI: Nice to meet you, " + user_name + "!")
        else:
            print("AI: You didn't enter a name.")

    elif user_input == "hello":
        if user_name:
            print("AI: Hello, " + user_name + "!")
        else:
            print("AI: Hello! Use the 'name' command so I know what to call you.")

    elif user_input == "favorite color":
        favorite_color = input(
            "AI: What is your favorite color?\nYou: "
        ).strip()

        if favorite_color:
            print("AI: I'll remember that your favorite color is " + favorite_color + ".")
        else:
            print("AI: You didn't enter a color.")

    elif user_input == "what is my favorite color":
        if favorite_color:
            print("AI: Your favorite color is " + favorite_color + ".")
        else:
            print("AI: You haven't told me your favorite color yet.")

    elif user_input == "add":
        first_number = input("AI: Enter the first number.\nYou: ")
        second_number = input("AI: Enter the second number.\nYou: ")

        try:
            first_number = float(first_number)
            second_number = float(second_number)

            total = first_number + second_number
            print("AI: The answer is", total)

        except ValueError:
            print("AI: Please enter valid numbers.")

    elif user_input == "how are you":
        responses = [
            "I'm doing great and ready to help.",
            "I'm online and learning.",
            "I'm feeling very Pythonic today."
        ]
        print("AI:", random.choice(responses))

    elif user_input == "who made you":
        print("AI: Chance created me using Python.")

    elif user_input == "what are you":
        print("AI: I am a command-based Python assistant.")

    elif user_input == "about":
        print("AI: I am a Python assistant created by Chance.")
        print("AI: I can remember information, tell jokes, give advice, and do math.")

    elif user_input == "":
        print("AI: Please type something.")

    else:
        print("AI: I don't understand that command yet. Type 'help' for options.")