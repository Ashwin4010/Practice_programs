# Pizza ordering program

while True:
    print("Welcome to python Pizza Deliveries! \n")
    # Pizza Size
    print("Small pizza : $15 \nMedium Pizza : $20 \nLarge Pizza : $25 \n")
    print("Extra Pepporoni Costs $2 for small and $3 for Medium and Large \n")
    print("Extra Cheese costs $1 for all size \n")
    # Getting input from Users
    size = input("What size Pizza do you want : S, M, L : ")
    add_pepperoni = input("Do you want Pepporoni: Y or N : ")
    extra_cheese = input("Do you want Extra Cheese: Y or N : ")
    total_bill = 0
    #Billing
    if size == "S" or "M" or "L" or "s" or "m" or "l":
        if size == "S" or "s":
            total_bill = 15
        elif size == "M" or "m":
            total_bill = 20
        elif size == "L" or "l":
            total_bill = 25
    #Pepporoni      
    if add_pepperoni == "Y" or "y":
        if size == "S" or "s":
            total_bill += 2
        elif size == "M" or "L" or "m" or "l":
            total_bill += 3
        else:
            total_bill
    else:
        total_bill
    #Cheese Block
    if extra_cheese == "Y" or "y":
        total_bill += 1
    else:
        total_bill
    print(f"your final bill is {total_bill} \n")
