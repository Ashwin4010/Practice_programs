#if int error arises uses split with , seperation or "space" seperation
student_scores = input("Enter the scores of the students : ").split(",")

student_scores_as_int = [int(i) for i in student_scores]

print(student_scores_as_int)

highest_score = 0
for scores in student_scores_as_int:
    if scores > highest_score:
        highest_score = scores
print(highest_score)

print(max(student_scores_as_int))
print(min(student_scores_as_int))