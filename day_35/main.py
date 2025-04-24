import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv, dotenv_values

load_dotenv()

auth_token = os.getenv("AUTH_TOKEN")

api_key = "d45b6a63b43af269fb9d12267329dd5b"

account_sid = os.getenv("ACC_SID")



My_lat = 5.89
my_long = 5.67

parameter = {"lat": 5.89,
    "lon": 5.67,
    "cnt":4,
    "appid": api_key
}


weather = requests.get(url = "https://api.openweathermap.org/data/2.5/forecast", params= parameter)
weather.raise_for_status()

print(weather.status_code)
weather_data = weather.json()

data_list = weather_data["list"]

will_rain = False

for time in data_list:

    each_weather = time["weather"][0]

    weather_id = each_weather["id"]
    if weather_id < 700:
        will_rain = True
       
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    body="Bring an umbrella cuz its going to rain☔",
    from_="whatsapp:+14155238886",
    to="whatsapp:+2348136552264",
    )

    print(message.status)