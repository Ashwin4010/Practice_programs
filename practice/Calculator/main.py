
from art import logo

print(logo)

def add(n1,n2):
    """adds two numbers"""
    return n1 + n2 
def subtract(n1,n2):
    """subtracts second number from hthe first number from two given numbers"""
    return n1-n2
def divide(n1,n2):
    """Divides second number from the first number from two given numbers"""
    return n1/n2
def multiply(n1,n2):
    """multiplies two numbers"""
    return n1*n2

operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply,
}
def calculate():
    num1 = float(input("What's the first number: "))
    # looping through operations dictionaries to the show the users what operations can they perform
    for operand in operations:
        print(operand)
    # variable is set to true it will trip once the user wishes to not continue
    should_continue = True

    while should_continue:
        selected_operation = input("operation you want to perform : ")
        num2 = float(input("What's the second number: "))
        calculation_function = operations[selected_operation]
        answer = calculation_function(num1,num2)
        print(f"{num1} {selected_operation} {num2} = {answer}")

        user_continue = input("do you want to continue with the previous answer ?: type 'Y' or 'N':").upper()

        if user_continue == "Y":
            num1 = answer
        else:
            should_continue = False
            calculate()
        
calculate()


