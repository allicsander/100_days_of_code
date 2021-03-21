
def prime_number(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("it is a prime number")
    else:
        print("It's not a prime number")        

prime_number(int(input("Enter a number to check: ")))             