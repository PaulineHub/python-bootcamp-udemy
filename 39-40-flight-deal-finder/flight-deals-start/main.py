from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import requests
from pprint import pprint # pretty print

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

sheet_endpoint = "https://api.sheety.co/e48719e271baa951b0cb14def6302630/flightDeals/prices"

sheety_response = requests.get(url=sheet_endpoint)
sheety_response.raise_for_status()
sheet_data = sheety_response.json()
#pprint(sheet_data['prices'][0]['iataCode'])

sheety_headers = {
    "Content-Type": "application/json",
}

# --------------------------------------------------------
# Populate google sheet with IATA codes

for travel in sheet_data['prices']:
    travel_id = str(travel['id'])
    sheet_id_endpoint = f"https://api.sheety.co/e48719e271baa951b0cb14def6302630/flightDeals/prices/{travel_id}"
    if travel['iataCode'] == '':
        # Search IATA Code
        flight_search = FlightSearch(travel['city'])
        iata_code = flight_search.give_iata_code()
        travel['iataCode'] = iata_code
        # Update IATA code in Google Sheet
        params = {
            "price": {
                "iataCode": travel['iataCode']
            }
        }
        sheety_response = requests.put(url=sheet_id_endpoint, json=params, headers=sheety_headers)
        sheety_response.raise_for_status()
        sheety_response.json()
    # Compare prices
    sheety_response = requests.get(url=sheet_id_endpoint)
    sheety_response.raise_for_status()
    data_travel = sheety_response.json()
    data_code = data_travel['price']['iataCode']
    data_price = data_travel['price']['lowestPrice']
    flight_data = FlightData(data_code, data_price)
    data_trips = flight_data.search_flights()
    pprint(data_trips)
    
