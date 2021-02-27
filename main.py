print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 160:
    print("You can rollercoast, of course if you're bold enough")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you can't ride the rollercoast until you grow taller")