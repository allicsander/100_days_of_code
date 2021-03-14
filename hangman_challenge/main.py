import random
from words import words 
from stages import stages, welcome_text

print(welcome_text)

chosen_word = random.choice(words)

print(f"Pssst, the chosen word is {chosen_word}")

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    