# finding the given number is odd or even
while True:
#Getting input(number) from user
    user_number = int(input("Enter a number: "))
    #dividing the given number by two
    # if user_number <= 0:
    #     print("Enter a real number next time")
    #     corrected_user_number = user_number.remove("-")
    #     if (corrected_user_number % 2) == 0:
    #         print(f"{user_number} is a even number")
    #     else:
    #         print(f"{user_number} is a odd number")
    if (user_number%2) == 0:
        print(f"{user_number} is a even number")
    else:
        print(f"{user_number} is a odd number")