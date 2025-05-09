# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("./day_26/NATO-alphabet-start/nato_phonetic_alphabet.csv")

# print(nato_data)

# for (index, row) in nato_data.iterrows():
    # print(row.letter)

nato_dict = { row.letter : row.code for (index,row) in nato_data.iterrows() }

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name = input("Enter a word: ").upper()

coded_list = [ nato_dict[n] for n in name ]

print(coded_list)