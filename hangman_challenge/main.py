import random
from words import words 
from stages import stages, welcome_text

print(welcome_text)

chosen_word = random.choice(words)

print(f"Pssst, the chosen word is {chosen_word}")

end_of_game = False
display = []
word_length = len(chosen_word)
lives = len(stages) -1

for _ in range(word_length):
    display += "_"
# print(display)    


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed '{guess}, that's not in the word. You lose a life!")
        lives -= 1
        print(f"lives count: {lives}")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    print(stages[lives])    
