#Calculate average height from the given user heights

student_height = int(input("Enter a list of student's height : "))


total_height = 0
for height in student_height:
    total_height = total_height + height
print("total Height : ", total_height)

num_of_students = 0
for students in student_height:
    num_of_students = num_of_students + 1
print("Number of students : ",num_of_students)

