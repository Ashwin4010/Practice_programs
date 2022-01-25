#importing random module
import random

# Defining what are all the letters, numbers, and symbols are 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Getting length of password, how much numbers and symbols to be included

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Generating random letters, numbers and symbols form the given user inputs
selected_letters = random.sample(letters, nr_letters) # random.sample(list(str), length(int))
selected_numbers = random.sample(numbers, nr_numbers) # random.sample(list(str), length(int))
seleccted_symbols = random.sample(symbols, nr_symbols) # random.sample(list(str), length(int))

#Concartinating the selected num,letters, symbols
password = (selected_letters+seleccted_symbols+selected_numbers)

# the password is still a list hence we need to convert it to string to use it
# inititing a new variable with empty string
password_to_string = ""

#iterating through every element in the list and adding it to the password_to_string variable
for element in password:
    password_to_string += element

#Printing the genertated string
print(password_to_string)

#printing randomized password
randomized_password = ''.join(random.sample(password,len(password))) #Join adds the randomized string to the variable without space
print(randomized_password)



