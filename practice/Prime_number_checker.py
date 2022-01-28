# Program to check whether the given number is a prime number or not

n = int(input("Check this Number: "))

def prime_checker(number):
    if (number%2 != 0 and number%number == 0) or number == 2:
        print("it's a prime number")
    else:
        print("it's not a prime number")

prime_checker(number=n)