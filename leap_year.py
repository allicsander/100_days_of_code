# this is how you work out whether if a particular year ia a leap year:
# on every year that is evenly divisible by 4
#    except every year that is evenly divisible by 100
#       unless the year is also evenly divisible by 400

year = int(input("Type the year you want to check: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leap year.")
        else:
            print("Not a leap year.")    
    else:
        print("This is a leap year.")
else:
    print("Not a leap year.")
