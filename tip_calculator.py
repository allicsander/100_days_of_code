#tip calucator
print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_per_person = (total_bill + total_bill * (tip_percentage/100))/ people
formatted_bill_string = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${ formatted_bill_string }")