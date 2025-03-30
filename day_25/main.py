# with open("./day_25/weather_data.csv") as file:
#     data = file.readlines()

#     print(data)

# import csv

# with open("./day_25/weather_data.csv") as file:
#     data = csv.reader(file)

#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temp = int(row[1])
#             temperature.append(temp)
#             print(row)


import pandas

data = pandas.read_csv("./day_25/weather_data.csv")

# print(type(data))

# print(data["temp"])    

data_dict = data.to_dict()

# print(data_dict)

data_list = data["temp"].to_list()

average = data["temp"].mean()

max_temp = data["temp"].max()

print(average)
print(max_temp)


# Getting hold of column

print(data.condition)
print(data["condition"])


# Getting Data in row

data_Monday = data[data.day == "Monday"]

day_max_temp = data[data["temp"]== max_temp]

print(day_max_temp)

monday_temp = int(data_Monday.temp)

print(monday_temp)


def f(x):
    x = x*1.8 + 32
    print(float(x))


f(monday_temp)

# Create DataFrame from scratch

data_dict = {
    "Students": ["Exalt", "Excel", "Saviour", "Sanctuary"],
    "Score": [78, 70, 72, 69]
             }
dataframe = pandas.DataFrame(data_dict)

print(dataframe)

dataframe.to_csv("Student_score.csv")




# import pandas

# data = pandas.read_csv("./day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")


# gray = data[data["Primary Fur Color"] == "Gray"]

# red = data[data["Primary Fur Color"] == "Cinnamon"]

# black = data[data["Primary Fur Color"] == "Black"]


# no_gray = len(gray["Primary Fur Color"].to_list())
# no_red = len(red["Primary Fur Color"].to_list())
# no_black = len(black["Primary Fur Color"].to_list())


# # print(red)

# color_dict = {
#     "Fur Color": ["grey", "red", "black"],
# "Count": [no_gray, no_red, no_black]
# }


# color_frame = pandas.DataFrame(color_dict)

# print(color_frame)


# color_frame.to_csv("./day_25/color_data.csv")