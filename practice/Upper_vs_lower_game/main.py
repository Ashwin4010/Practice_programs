# Display art
from art import logo,vs
from game_data import data
import random 
import os

def format_data(account):
    """format the account data into a printable format"""
    account_name = account["name"]
    account_descr =account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they guessed it correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo)
# Generate a random account from the game data

score = 0
game_should_continue = True
account_b = random.choice(data)


while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A:{format_data(account_a)}")
    print(vs)
    print(f"Against B:{format_data(account_b)}")

    # ask the user for a guess

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if the user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    # get follower count of each account

    is_correct = check_answer(guess,a_follower_count,b_follower_count)
    
    os.system('cls')
    print(logo)
    # use if statement to check if the user is correct

    if is_correct:
        score += 1
        print(f"You are Right !!!: your Score: {score}")
    else:
        print(f"You are Wrong. final Score: {score}")
        game_should_continue = False
