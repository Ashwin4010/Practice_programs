import random
from art import *
import os

# todo:
# 1. user needs to choose between easy and hard difficulty
# 2. for easy difficulty user has 10 attempts and for Hard 5 attempts
# 3. every time the user guesses wrong the reduce the remaining Attempt
# 4. once the attempts are exhauseted and if user guessed it right user wins else user loses.

print(logo)
print("Welcome to the number guessing game!")


attempts = 0
guess = 0
is_game_over = False
selected_number = random.randint(0,100)
#user_guessed = 0

print(f"I'm thinking of a number Between 1 and 100")

difficulty = input("Choose the difficulty type 'easy' or 'hard': ").lower()

while not is_game_over:
    if difficulty == "easy":
        attempts = 10
        while attempts != 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == selected_number:
                print(f"You got it ! the Answer was {selected_number}")
                print(win)
                is_game_over = True
                break
            elif guess > selected_number:
                print("Too High ")
                attempts -= 1
            elif guess < selected_number:
                print("Too low ")
                attempts -= 1
            else:
                print("Enter a valid Nuimber : ")
                attempts -= 1
        if attempts == 0:
            print(lose)
        is_game_over = True
        
    elif difficulty == "hard":
        attempts = 5
        while attempts != 0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == selected_number:
                print(f"You got it ! the Answer was {selected_number}")
                print(win)
                is_game_over = True
                break
            elif guess > selected_number:
                print("Too High ")
                attempts -= 1
            elif guess < selected_number:
                print("Too low ")
                attempts -= 1
            else:
                print("Enter a valid Nuimber : ")
                attempts -= 1  
        if attempts == 0:
            print(lose)
        is_game_over = True
        
    else:
        print("Enter a Vaild option")
        print(clown)
        break

