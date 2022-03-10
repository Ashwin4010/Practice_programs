from random import sample
from art import *
from game_data import data

#todo 
# 1. pick two random elements from data i.e a and b

print(logo)

current_score = 0
final_score = 0
game_over = False

while not game_over:
    
    a = sample(data,1)
    b = sample(data,1)
    
    name_of_a = a[0]['name']
    follower_count_of_a = a[0]['follower_count']
    description_of_a = a[0]['description']
    country_of_a = a[0]['country']

    name_of_b = b[0]['name']
    follower_count_of_b = b[0]['follower_count']
    description_of_b = b[0]['description']
    country_of_b = b[0]['country']

    def compare(follower_count_of_a,follower_count_of_b,user_choice):
        """Function which compares a with b"""
        if user_choice == "A" :
            if follower_count_of_a > follower_count_of_b:
                print(" Correct")
                current_score += 1
            else:
                final_score = current_score
                print(final_score)    
                game_over = True
        if user_choice == "B":
            if follower_count_of_b > follower_count_of_a:
                print(" Correct")
                current_score += 1
            else:
                final_score = current_score
                print(final_score)
                game_over = True
    print(f"Compare A: {name_of_a}, {description_of_a}, {country_of_a} ")
    print(vs)
    print(f"Compare B: {name_of_b}, {description_of_b}, {country_of_b} ")
    
    user_choice = input("Who has more Followers ? A or B :").upper()
    compare(follower_count_of_a,follower_count_of_b,user_choice)
    game_over = True
# 2. ask the user if the a is greater than b 
# 3. if user predicts the right answer move the b to the postion of a
# 4. pick another element from data and place it in the position of b(previous)
# 5. perform step 2,3,4 until user is Wrong
# 6. if the user is wrong then calculate the number of times they predicted correctly
