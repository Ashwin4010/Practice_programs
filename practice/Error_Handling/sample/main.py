# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is a made up error")

height = float(input("height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3M ")
bmi = weight/height ** 2
print(bmi)