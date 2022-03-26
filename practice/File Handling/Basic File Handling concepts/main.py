# reading contents of the file
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# mode "w" deletes the content of the file and replaces with the given contents, if the file don't exist it creates the file and writes the contents to it.
with open("new_file.txt", mode="w") as file:
     file.write("\nHello text")

#Mode "a" appends the given content to the existing file
with open("new_file.txt", mode="a") as file:
     file.write("\nHello text")