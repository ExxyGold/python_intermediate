import requests
import datetime as dt
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

today = dt.datetime.now()

date= today.date()
time = f"{today.hour}:{today.minute}"
print(time)

GOOGLE_SHEET_TOKEN = os.getenv("GOOGLE_SHEET_TOKEN")
API_KEY ="45b72590b4ae6d7d296f274eb325f078"
API_ID = "2c0c13ef"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shitty_endpoint = 'https://api.sheety.co/8c6d5312fcab0edeed83d34285105ddc/myWorkoutPlan/workouts'



exe_param = {
    "query" : input("How many Exercise did you do today?: ")
}
header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}
response = requests.post(url = exercise_endpoint, json= exe_param, headers= header)

data = response.json()
workout = data["exercises"]

header = {
    "Authorization": F"Bearer {GOOGLE_SHEET_TOKEN}"
}
for inputs in workout:
    exercise = inputs["name"].title()
    duration = inputs["duration_min"]
    calories = inputs["nf_calories"]

    body= {
    "workout":
        {
        "date": f"{date}",
        "time": time,
        "exercise": exercise,
        "intensity": "",
        "duration": duration,
        "calories": calories,
        }
    }
    response_sheet = requests.post(url= shitty_endpoint, json= body, headers= header )
    print(response_sheet.json())