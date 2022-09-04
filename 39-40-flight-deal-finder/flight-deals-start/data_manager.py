import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_endpoint = "https://api.sheety.co/e48719e271baa951b0cb14def6302630/flightDeals/prices"
        self.sheety_headers = {
            "Content-Type": "application/json",
        }

    def get_sheet_data(self, endpoint_id=''):
        sheety_response = requests.get(url=f"{self.sheet_endpoint}{endpoint_id}")
        sheety_response.raise_for_status()
        return sheety_response.json()

    def update_iata_code_sheet(self, travel_id, iata_code):
        sheet_id_endpoint = f"{self.sheet_endpoint}/{travel_id}"
        params = {
            "price": {
                "iataCode": iata_code
            }
        }
        sheety_response = requests.put(url=sheet_id_endpoint, json=params, headers=self.sheety_headers)
        sheety_response.raise_for_status()
        sheety_response.json()
