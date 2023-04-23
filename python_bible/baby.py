from random import choice 

questions = [
    "Why is there so much hate in the world?: ",
    "Why am I treated differently as a brown person?: ",
    "Why does Uncle Joe always seem so sad?: "
    ]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("why?: ").strip().lower()

print("Oh... Okay")
