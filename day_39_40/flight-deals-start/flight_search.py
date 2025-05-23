import os
import requests
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v1/shopping/flight-offers"

class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.getenv("AMA_API_KEY")
        self.api_secret= os.getenv("AMA_SECRET")
        self.token = self.get_new_token()
        self.cities = []

    def get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers= header, data=body)
        token = response.json()["access_token"]
        return token

    def add_cities(self, cities):
            print(f"Using this token to get destination {self.token}")
            parameters = {
                "keyword": cities,
                "max": 2,
                "include": "AIRPORTS"
            }
            header = {
                "Authorization": f"Bearer {self.token}"}
            response = requests.get(url = IATA_ENDPOINT, params = parameters, headers= header )
            try:
                code = response.json()["data"][0]['iataCode']
            except IndexError:
                print(f"IndexError: No airport code found for {cities}.")
                return "N/A"
            except KeyError:
                print(f"KeyError: No airport code found for {cities}.")
                return "Not Found"
            return code
    
    def check_flight(self, origin_city, destination_city, from_time, to_time, is_direct=True ):
        header = {"Authorization": f"Bearer {self.token}"}
        query = {
              "originLocationCode": origin_city,
            "destinationLocationCode": destination_city,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true" if is_direct else "false",
            "currencyCode": "GBP",
            "max": "10",
        }
        response = requests.get(url= FLIGHT_ENDPOINT, params= query, headers= header )

 
