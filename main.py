

age = int(input("What is your current age? "))

years_remaining = 90 - age
day_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"your have {day_remaining} days, {weeks_remaining} weeks, {months_remaining} months"

print(message)