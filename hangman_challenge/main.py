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


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print("no match, sorry about that!")
    
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
