# BMI Calculator

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi_index = int(weight/height**2)

print("Your BMI index is: " + str(bmi_index))