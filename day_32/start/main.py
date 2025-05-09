import smtplib
import datetime as dt
import random
import os
from dotenv import dotenv_values, load_dotenv


load_dotenv()

my_email = "exaltmokonogho@gmail.com"
my_password = os.getenv("EMAIL_PASSWORD")

print(my_email)
now = dt.datetime.now()

day_of_week = now.weekday()

if day_of_week == 3:
    with open("./day_32/start/quotes.txt") as quotes:
        quote_list = quotes.readlines()

    message = random.choice(quote_list)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port = 465) as connection:

        connection.login(user = my_email, password= my_password)
        connection.sendmail(from_addr= my_email,
                            to_addrs= "mokonoghoexalt@gmail.com", 
                            msg= f"Subject:Quote Of The Day\n\n{message}"
                            )



now = dt.datetime.now()

year= now.year
month = now.month
day_of_week = now.weekday()


date_of_birth = dt.datetime(year = 2004, month= 4, day = 15, hour = 15)

day_of_b = date_of_birth.weekday()

print(date_of_birth)
print(day_of_b)