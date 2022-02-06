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

ace = [1,11]
cards_without_ace = [2,3,4,5,6,7,8,9,10,10,10,10]
cards = ace + cards_without_ace

user_cards =[]
comp_cards = []
user_card_total = 0
comp_card_total = 0

def deal_card():
    user_cards = random.sample(cards,2)
    print(f"User's Card : {user_cards}")
    comp_cards = random.sample(cards,2)
    print(f"computer's card: {comp_cards}")

def calcualte():
    user_card_total = sum(user_cards)
    print(user_card_total)
    comp_card_total = sum(comp_cards)
    print(comp_card_total)

def compare(user,comp):
    if user > comp:
        print("User Wins !")
    elif user == comp:
        print("It's a Draw")
    else:
        print("Computer Wins")



if user_card_total > 21 and user_cards == any(ace): 
    if user_cards == any(ace):
        ace_selection = input("You have Ace card. do you want it to be 1 or 11 ? : ")
        for i in user_cards:
            user_cards[i] = ace_selection
        print(user_cards)
elif user_card_total < 21 and user_cards == any(ace):
    while user_card_total <21:
        new_card = input("Pick another card ? : type 'y' or 'N' ").upper()
        if new_card == "Y":
            user_cards.append(random.sample(cards,1))
            print(user_card_total)
        elif user_card_total < 17:
            comp_cards.append(random.sample(cards,1))
            print(comp_card_total)
    
    if comp_card_total > 21:
        print("User Wins !")
    else:
        compare(user=user_card_total,comp=comp_card_total)

deal_card()
compare(user=user_card_total,comp=comp_card_total)

# else:
#     print("end of the line")

#compare(user=user_card_total,comp=comp_card_total)
    
