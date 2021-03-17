import random
from words import words 
from stages import stages, welcome_text

print(welcome_text)

chosen_word = random.choice(words)

print(f"Pssst, the chosen word is {chosen_word}")

display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
print(display)    

guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
  
print(display)
