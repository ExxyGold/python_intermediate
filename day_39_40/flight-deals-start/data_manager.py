from pprint import pprint
import requests
import os
from dotenv import load_dotenv
load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/e5ec8bb0924aa036467bdf513d03958a/flightDeals/prices"
USERS_ENDPOINT = "https://api.sheety.co/e5ec8bb0924aa036467bdf513d03958a/flightDeals/users"


class DataManager:
    def __init__(self):
        # AUTH = {
#     "Authorization": f"Bearer {os.getenv("GOOGLE_SHEET_TOKEN")}"
#     }
        self.destination_data = {}
        
    def get_emails(self):
        response = requests.get(url= USERS_ENDPOINT)
        userdata = response.json()["users"]
        return userdata

    def get_destination_data(self):
        self.response = requests.get(url = SHEETY_ENDPOINT)
        sheet_data = self.response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data
    
    def put_code(self):
        
        for city in self.destination_data:
            PUT_ENDPOINT = f'{SHEETY_ENDPOINT}/{city["id"]}'
            PARAMETER = {
                "price" : {
                "iataCode" : city["iataCode"]
                    }
                }
            putresponse = requests.put(url = PUT_ENDPOINT, json= PARAMETER)
           

    #This class is responsible for talking to the Google Sheet.
    

