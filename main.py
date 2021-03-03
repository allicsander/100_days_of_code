print("Welcome to the Love Calculator!")
name_one = input("What is your name? \n")
name_two = input("What is the crush's name? \n")

combined_string = name_one + name_two
lower_combined_string = combined_string.lower()

t = lower_combined_string.count("t") 
r = lower_combined_string.count("r") 
u = lower_combined_string.count("u") 
e = lower_combined_string.count("e") 

true_count = t + r + u + e


l = lower_combined_string.count("l") 
o = lower_combined_string.count("o") 
v = lower_combined_string.count("v") 
e = lower_combined_string.count("e") 

love_count = l + o + v + e

love_score = int(str(true_count) + str(love_count))

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif (love_score >=40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
