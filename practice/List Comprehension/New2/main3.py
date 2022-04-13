student_dict = {
    "student": ["Angela","James","Lily"],
    "score":[56,76,98]
}

import pandas as pd

student_DF = pd.DataFrame(student_dict)
# print(student_DF)

for (index, row) in student_DF.iterrows():
   if row.student == "Angela":
       print(row.score)