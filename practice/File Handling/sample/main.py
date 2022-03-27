with open("new_file.txt") as file:
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="W") as file:
    file.write("\nNew Text")