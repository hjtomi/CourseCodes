from requests.auth import HTTPBasicAuth
import os


class Prices:
    API_ENDPOINT = "https://api.sheety.co/ed1b29847306ac73b276fda28c002b5c/flightDeals/prices"
    API_HEADERS = {"Authorization": "aGp0b21pOm15cGFzc3dvcmR4b3hv"}
    BASIC = HTTPBasicAuth("hjtomi", "mypasswordxoxo")


class Users:
    API_ENDPOINT = "https://api.sheety.co/ed1b29847306ac73b276fda28c002b5c/flightDeals/users"
    API_HEADERS = {"Authorization": "Basic aGp0b21pOm15cGFzc3dvcmR4b3hv"}
    BASIC = HTTPBasicAuth("hjtomi", "mypasswordxoxo")
