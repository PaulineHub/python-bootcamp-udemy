import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, city):
        self.city = city
        self.tequila_endpoint = "https://tequila-api.kiwi.com/locations/query"
        self.tequila_api_key = "SUTH6Ev-Ymi3IWpGA0C1xL0OvjEfN1rN"
        self.tequila_headers = {
            "accept": "application/json",
            "apikey": self.tequila_api_key
        }
        self.params = {
            "term": self.city
        }
        

    def give_iata_code(self):
        tequila_response = requests.get(url=self.tequila_endpoint, headers=self.tequila_headers, params=self.params)
        tequila_response.raise_for_status()
        tequila_data = tequila_response.json()
        return tequila_data["locations"][0]["code"]
