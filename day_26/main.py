# num = [1, 3, 5, 6]

# new_num = [n*10 for n in num]

# print(new_num)

import pandas

student_scores = {"Students": ["Exalt", "Saviour", "Sanctuary"], "Scores": [78, 60, 50]}


student_dataframe = pandas.DataFrame(student_scores)

# for (key, value) in student_dataframe.items():
#     print(value)

# for (index, row) in student_dataframe.iterrows():
#     if index == 0:
#         print(row)