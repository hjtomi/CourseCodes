import requests
from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient

API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_PARAMETERS = {
    "lat": 46.911010,
    "lon": 19.693759,
    "appid": "9cf5257dcf2c3bac961291ee74135d9c"
}
TWILIO_ACC_SID = "ACacfd54ccaa982ab8251548c8f40650a0"
TWILIO_AUTH_TOKEN = "0975f63c35575996deab22ab5b88ac37"

response = requests.get(API_ENDPOINT, API_PARAMETERS)
response.raise_for_status()

weathers = response.json()["weather"]

for weather in weathers:
    if weather["id"] < 700:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {"https": os.environ["https_proxy"]}

        client = Client(TWILIO_ACC_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
        message = client.messages.create(body="Esik az eso", from_="+13856006090", to="+36302804337")
        print(message.status)
        break
