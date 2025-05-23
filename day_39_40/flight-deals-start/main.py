from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
import time
from datetime import datetime, timedelta
from notification_manager import NotificationManager

data = DataManager()
ORIGIN_CITY_IATA = "LON"

data_sheet = data.get_destination_data()
userdata = data.get_emails()
emails = []
for users in userdata:
    each_email = users["whatIsYourEmail?"]
    emails.append(each_email)
    
flight_search = FlightSearch()

# Updates the data sheet in main.py to hv iata codes sent from flight search.
for dict in data_sheet:
    if dict["iataCode"] == "":
        dict["iataCode"] = flight_search.add_cities(dict["city"])
        # flight_data.find_cheapest_flight(dict["iataCode"])
        time.sleep(2)


#This updates destination data in data_manager with data_sheet having iata code.
data.destination_data = data_sheet

# this updates google sheet using destinaton data and put request.
data.put_code()

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in data_sheet:

    flights = flight_search.check_flight(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time= tomorrow,
        to_time= six_month_from_today,
        is_direct= False
        )
    cheapest_flight = find_cheapest_flight(flights)


    print(f"{destination['city']}: £{cheapest_flight.price}")
    time.sleep(2)

    if cheapest_flight.price != "N/A" and cheapest_flight.price <= destination["lowestPrice"]:

        notification_manager = NotificationManager(emails)
        notification_manager.send_emails(messages= f"Low price alert! Only GBP{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        
        # notification_manager.send_whatsapp(
        #     message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
        #                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #                  f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.")
        