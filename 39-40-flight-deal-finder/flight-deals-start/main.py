from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
import requests
from pprint import pprint # pretty print

# --------------------------------------------------------
# Populate google sheet with IATA codes

data = DataManager()
sheet_data = data.get_sheet_data()

for travel in sheet_data['prices']:
    travel_id = str(travel['id'])
    
    if travel['iataCode'] == '':
        # Search IATA Code
        flight_search = FlightSearch(travel['city'])
        iata_code = flight_search.give_iata_code()
        # Update IATA code in Google Sheet
        data.update_iata_code_sheet(travel_id, iata_code)
    # Search flight with lower prices than our maximal prices on the travel sheet, per destination
    data_travel = data.get_sheet_data(f'/{travel_id}')
    data_code = data_travel['price']['iataCode']
    data_price = data_travel['price']['lowestPrice']
    flight_data = FlightData(data_code, data_price)
    data_trips = flight_data.search_flights()
    pprint(data_trips)
    
