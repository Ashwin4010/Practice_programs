# Functions and inputs of functions 

#function
def greet():
    print("Welcome \n"*3)

# Function calling
greet()

#############################################

# Function with a parameter
def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
# function calling with a value passing to the parameter
greet_with_name("ashwin")
############################################

# Function with multiple parameters
def greet_with(name,location):
    print(f"Hello {name}!")
    print(f"what is it like in {location} ?")
# Function calling with parameter keyword to explectily mentioning where the argument must be passed
greet_with(name = "ashwin",location= "chennai") # passing arguments with specific parameters

#############################################



