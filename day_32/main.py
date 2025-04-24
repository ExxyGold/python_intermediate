import random
import datetime as dt
import pandas
import smtplib
import os
from dotenv import load_dotenv, dotenv_values
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
birthdays = pandas.read_csv("./day_32/birthdays.csv")

birth_dict = birthdays.to_dict(orient = "list")


# print(birth_dict)
friends = birth_dict["name"]
months = birth_dict["month"]
day = birth_dict["day"]
email = birth_dict["email"]

now = dt.datetime.now()
this_month = now.month
today  = now.day
hour = now.hour

celebs_dict = {}

for name in friends:
    cel_index = friends.index(name)
    if months[cel_index] == this_month and day[cel_index] == today:
        celebs_dict[name] = email[cel_index]

letters = []
for n in range(1,4):
    with open(f"./day_32/letter_templates/letter_{n}.txt") as file:
        letter = file.read()
        letters.append(letter)

load_dotenv()
my_password =  os.getenv("EMAIL_PASSWORD")

for persons in celebs_dict:
    chosen_letter = random.choice(letters)

    modified_letter = chosen_letter.replace("[NAME]", persons)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login("exaltmokonogho@gmail.com", my_password)
        connection.sendmail(from_addr= "exaltmokonogho@gmail.com", 
                            to_addrs= celebs_dict[persons], 
                            msg= f"Subject:Happy Birthday {persons}\n\n{modified_letter}")



# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




