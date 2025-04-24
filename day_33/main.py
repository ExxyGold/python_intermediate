import requests
import os
from datetime import datetime
import smtplib
from dotenv import load_dotenv, dotenv_values

MY_LAT = 5.893660 # Your latitude
MY_LONG = 5.676750 # Your longitude

def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])


    if -5 <  iss_latitude - MY_LAT < 5 and -5 < MY_LONG - iss_longitude < 5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.

def night_time():
    
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    current_hour = time_now.hour
    
    if (current_hour in range(17, 24) or current_hour in range(0, 6)):
        return True

load_dotenv()
password = os.getenv("EMAIL_PASSWORD")
#If the ISS is close to my current position

if not night_time():
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login("exaltmokonogho@gmail.com", password= password)
        connection.sendmail(from_addr="exaltmokonogho@gmail.com", to_addrs= "mokonoghoexalt@gmail.com", msg= "Subject:Hey Exxy\n\nLook up, the ISS is up there")

    print("yes")


# and it is currently dark
# Then end me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



