rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

human_choice = int(input("Type 1 for Rock, 2 for Paper or 3 for Scissors.\n"))

if human_choice == 1:
    human_gesture = rock
elif human_choice == 2:   
    human_gesture = paper
elif human_choice == 3:   
    human_gesture = scissors
else:
    human_gesture = "unknown gesture"        


AI_choice = random.randint(1, 3)

if AI_choice == 1:
    AI_gesture = rock
elif AI_choice == 2:   
    AI_gesture = paper
elif AI_choice == 3:   
    AI_gesture = scissors


print("Your choice is:")
print(human_gesture)

print("\n\nAI choice is:")
print(AI_gesture)

if human_choice == AI_choice:
    print("It's a draw!")
elif human_choice > 3 and human_choice < 1:   
    print("You should choose between rock, paper and scissors, you cheater!") 
elif (human_choice == 1 and AI_choice == 3) or \
     (human_choice == 2 and AI_choice == 1) or \
     (human_choice == 3 and AI_choice == 2):
    print("You win!")  
else:
    print("You lose!")          