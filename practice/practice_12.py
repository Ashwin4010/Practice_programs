#Tressure map

row_1 = ["😀","😀","😀"]
row_2 = ["😀","😀","😀"]
row_3 = ["😀","😀","😀"]

map = [row_1,row_2,row_3]

print(f"{row_1}\n{row_2}\n{row_3}")

location = input("Enter where do you want put the treasure : ")

horizontal = int(location[1])
vertical = int(location[0])

map[vertical - 1][horizontal -1] = "X"

print(f"{row_1}\n{row_2}\n{row_3}")
