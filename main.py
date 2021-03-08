students_heights = input("Input a list of student heights ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

total_height = 0
for height in students_heights:
    total_height += height
print(total_height)    

number_of_students = 0
for height in students_heights:
    number_of_students += 1
print(number_of_students)   

print(f"average height is {round(total_height/number_of_students)}")

# short way:  sum() and len() functions