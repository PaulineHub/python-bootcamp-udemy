import requests
from datetime import datetime, timedelta

class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, code, price):
        self.code = code
        self.price_max = price 
        self.fly_to = code
        self.fly_from = "YUL" # Montreal
        self.date_from = datetime.today() + timedelta(days=1)
        self.date_from_formated = self.date_from.strftime("%d/%m/%Y")
        self.date_to = self.date_from + timedelta(weeks=26)
        self.date_to_formated = self.date_to.strftime("%d/%m/%Y")
        self.nights_in_dst_from = '6'
        self.nights_in_dst_to = '27'
        self.flight_type = 'round'
        self.currency = 'CAD'

        self.tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.tequila_api_key = "SUTH6Ev-Ymi3IWpGA0C1xL0OvjEfN1rN"
        self.tequila_headers = {
            "accept": "application/json",
            "apikey": self.tequila_api_key
        }
        self.params = {
            "fly_from": self.fly_from,
            "fly_to": self.fly_to,
            "date_from": self.date_from_formated,
            "date_to": self.date_to_formated,
            "nights_in_dst_from": self.nights_in_dst_from,
            "nights_in_dst_to": self.nights_in_dst_to,
            "flight_type": self.flight_type,
            "curr": self.currency,
            "price_to": self.price_max
        }

    def search_flights(self):
        tequila_response = requests.get(url=self.tequila_endpoint, headers=self.tequila_headers, params=self.params)
        tequila_response.raise_for_status()
        tequila_data = tequila_response.json()
        travels = [{
            "price": f"{travel['price']} CAD",
            "departure": travel['cityFrom'],
            "arrival": travel['cityTo'], 
            "date_from": travel['local_departure'],
            "date_to": travel['local_arrival']
            } for travel in tequila_data['data']]
        return travels
