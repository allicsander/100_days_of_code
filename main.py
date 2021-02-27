# BMI Calculator 2.0

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi_index = round(weight/height**2)

if bmi_index <= 18.5:
    print(f" Your IMB is {bmi_index}, you are underweight.")
elif bmi_index <= 25:
    print(f" Your IMB is {bmi_index}, you have a normal weight.")
elif bmi_index <= 30:
    print(f" Your IMB is {bmi_index}, you are slightly overweight.")
elif bmi_index <= 35:
    print(f" Your IMB is {bmi_index}, you are obese.")
else:
    print(f" Your IMB is {bmi_index}, you are clinically obese.")

