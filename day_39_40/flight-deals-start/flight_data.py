import requests
import datetime as dt

CURRENT_DATE = dt.datetime.now()

for n in range(1, 30*6+1):
    future = CURRENT_DATE+ dt.timedelta(days = n)
    



class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops

def find_cheapest_flight(data):
        if data is None or not data['data']:
            print("No flight data")
            return FlightData(price = "N/A",
                              origin_airport= "N/A",
                               destination_airport= "N/A", 
                               out_date = "N/A",
                                return_date= "N/A",
                                stops= "N/A")
        
        first_flight = data['data'][0]
        lowest_price = float(first_flight["price"]["grandTotal"])
        nr_stops = len(first_flight["itineraries"][0]["segments"])-1
        origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
        out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]


        cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
        
        for flight in data["data"]:
            price = float(flight["itineraries"][0]["segments"][0]["departure"]["iataCode"])
            if price < lowest_price:
                origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
                destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
                return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
                cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, nr_stops)
                 
        return cheapest_flight
        
