#Love Calculaor

while True:
    print("Welcome to Love Calculator !!!!!! \n")
    # Getting Users name
    name_1 = input("Enter your name : ")
    name_2 = input("Enter their name : ")
    # Lowering their name to avoid case sensitivity
    ln1 = name_1.lower()
    ln2 = name_2.lower()
    #Counting how amny time TRUE/LOVE occured in Name 1 and Name 2
    total_ln1 = ln1.count("t") + ln1.count("r") + ln1.count("u") + ln1.count("e") + ln1.count("l") + ln1.count("o") + ln1.count("v")
    total_ln2  = ln2.count("t") + ln2.count("r") + ln2.count("u") + ln2.count("e") + ln2.count("l") + ln2.count("o") + ln2.count("v")
    #Combinig the result
    match = str(total_ln1) + str(total_ln2)
    #comparing the result
    if int(match) < 10 or int(match) < 40:
        print(f"{match} Your match is like coke and mentos")
    elif int(match) > 40 and int(match) < 50:
        print(f"{match} you are alright together")
    else:
        print(f"Your score is {match}")