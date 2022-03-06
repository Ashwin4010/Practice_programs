from random import randint
from tabnanny import check

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =5

def check_answer(guess, answer, turns):
    """Checks anser against guess and returns the number of turns remaining """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it ! the Answer was {answer}")
        
def set_difficulty():
    level = input("Choose the difficulty type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    
def game():
    
    print("Welcome to the number guessing game!")
    print(f"I'm thinking of a number Between 1 and 100")
    answer = randint(1,100)

    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        guess = int(input("Make a guess : "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out attempts, you lose.")
            return
game()