import random
#getting names form users
name = input("Give me everybody's name seperated by comma : ")
#seperating every name from the list
name = name.split(", ")
name_items = len(name)
#selecting a random name within the list
random_choice = random.randint(0, name_items-1) # list starting from index 0 to last index denoted with -1
person_who_will_pay = name[random_choice]
print(person_who_will_pay + " is going to pay")
