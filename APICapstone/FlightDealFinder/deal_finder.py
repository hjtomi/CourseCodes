import requests
from datetime import date, timedelta
from credentials import Prices


class DealFinder:

    def __init__(self):

        self.tequila_api_endpoint = "http://api.tequila.kiwi.com/v2/search"
        self.tequila_api_key = "LGLMzyShZ70o8Guh4PHN61nhWa6XhRXI"

        self.tequila_api_header = {
            "apikey": self.tequila_api_key
        }

        response = requests.get(Prices.API_ENDPOINT, headers=Prices.API_HEADERS, auth=Prices.BASIC)
        response.raise_for_status()

        self.sheet_data = response.json()

    def find_bargains(self):
        """Returns a list of trip plans with a low price."""
        trips = []
        for row in self.sheet_data["prices"]:
            api_parameters = {
                "fly_from": "BUD",
                "fly_to": row["iataCode"],
                "date_from": date.today() + timedelta(1),
                "date_to": date.today() + timedelta(182),
                "ret_from_diff_city": "false",
                "ret_to_diff_city": "false",
                "curr": "GBP",
                "price_to": row["lowestPrice"],
                "max_stopovers": 0
            }

            response = requests.get(self.tequila_api_endpoint, params=api_parameters, headers=self.tequila_api_header)
            response.raise_for_status()

            flight_data = response.json()

            if len(flight_data["data"]) > 0:
                trips.append(flight_data["data"][0])

        return trips
