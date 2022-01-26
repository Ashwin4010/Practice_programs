#Rock paper sissors

import random 

while True:

    Rock = """
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    """

    Paper = """
        __________
    ---'    ______)
            _______)
            _______)
            _______)
    ---.__________)
    """

    Scissors = """
        __________
    ---'   _______)
            ______)
        __________)
        (____)
    ---.__(___)
    """

    RPS = [0,1,2]

    RPS_length = len(RPS)

    users_choice = int(input("What do you choose ? Type 0 for 'Rock', Type 1 for 'Paper', Type 2 for 'Scissors' : "))

    if users_choice == 0:
        print(Rock)
    elif users_choice == 1:
        print(Paper)
    elif users_choice == 2:
        print(Scissors)
    else:
        print("Jackass, select from the given options")
        exit()

    computers_choice = random.randint(0,RPS_length -1)

    if computers_choice == 0:
        print(Rock)
    elif computers_choice == 1:
        print(Paper)
    else:
        print(Scissors)

    if users_choice == computers_choice:
        print("Its a Tie")
        print(users_choice, "\n")
        print(computers_choice)

    elif (users_choice == 0 and computers_choice == 2) or (users_choice == 1 and computers_choice == 0) or (users_choice == 2 and computers_choice == 1):
        print("You win !!!")
        print(users_choice, "\n")
        print(computers_choice)
    else:
        print("Computer Wins !!!")
        print(users_choice, "\n")
        print(computers_choice)
    #else:
        #exit() 
        