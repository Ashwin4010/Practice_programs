#TIP Calculating program

while True:
    print("Welcome to the Tip Calculator \n")
    # getting the total Bill
    total_bill = float(input("What was the totoal Bill? : $"))
    #Tip to be given
    tip = int(input("what percentage tip would youlike to give? 10, 12, or 15? "))
    #the bill amount for each person
    bill_split = int(input("How many people to split the bill? "))
    #Tip for the total bill
    tip_to_be_given = (tip/100) * total_bill
    # Splitting the bill with Tip
    bill_per_person = round(((total_bill+tip_to_be_given)/bill_split), 2)
    #bill_per_person_1 = round(bill_per_person, 2)
    #printing how much each person should pay
    bill_to_be_paid = f"\nEach person should pay: ${bill_per_person}"
    print(bill_to_be_paid)
    #Printing the total tip for the bill
    print(f"\nTip amout for the total Bill is ${tip_to_be_given}")

 

