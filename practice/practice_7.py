# Finding if the given year is a leap year or not
while True:
    year = int(input("Enter a year : "))

    if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")