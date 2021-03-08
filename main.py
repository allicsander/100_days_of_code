
student_scores = input("Input the list of student scores ").split()

highest_score = 0
for score in student_scores:
    if highest_score < int(score):
        highest_score = int(score)

print(f"The highest score in the class is {highest_score}")
