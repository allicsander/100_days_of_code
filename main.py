import random

names_string = input("Wecome to the Banker Roulette! Type the names, separated by a comma: ")

names = names_string.split(", ")


print(f"{names[random.randint(0, len(names) - 1)]} is going to buy the meal today:)")

# short way:  random.choice(names)