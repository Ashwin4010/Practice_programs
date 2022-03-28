with open("/Users/Aravind/Desktop/new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("/Users/Aravind/Desktop/new_file.txt", mode="w") as file:
    file.write("Hell")