# Program to check whether the given number is a prime number or not


while True:
    def prime_checker(number):
        is_prime = True
        for i in range(2, number):
            if number%i == 0:
                is_prime = False

        if is_prime:
            print("The Given Number is a prime number")
        else:
            print("The given number is not a prime number")

    n = int(input("Check this Number: "))
    prime_checker(number=n)
