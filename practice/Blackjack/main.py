# program for blackjack capstone project

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random 

print(logo)

play = input("Do you want to play/continue Blackjack? type Y or N: ").upper()

J = K = Q = [10]
A = [1,11]
cards = [2,3,4,5,6,7,8,9,10]

user_card =[]
comp_card = []

if play == "Y":
    generated_user_cards = random.sample((cards)+(A)+())
    print(f"User's Card : {generated_user_cards}")
    comp_card = ra


