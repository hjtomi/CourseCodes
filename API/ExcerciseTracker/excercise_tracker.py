# E X E R C I S E

import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os

MY_GENDER = "male"
MY_WEIGHT = 47
MY_HEIGHT = 167
MY_AGE = 16

NUT_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
NUT_API_PARAMETERS = {
    "query": input("What did you do? "),
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE,
}

HEADERS = {
    "x-app-id": os.environ.get("NUT_API_ID"),
    "x-app-key": os.environ.get("NUT_API_KEY"),
}

# POSTNAL JSON A PARAMS HELYETT
response = requests.post(url=NUT_API_ENDPOINT, json=NUT_API_PARAMETERS, headers=HEADERS)
response.raise_for_status()

data = response.json()
print(data)


basic = HTTPBasicAuth(os.environ.get("SHEETY_BASIC_USERNAME"), os.environ.get("SHEETY_BASIC_PASSWORD"))

SHEETY_HEADERS = {
    "Authorization": os.environ.get("SHEETY_BASIC"),
    "Content-Type": "application/json",
}

# Irja a docs hogy camel caseli az osszes json key-t tehat annyi volt a hiba hogy
# a parameterek nagy kezdobetuvel voltak
for excercise in data["exercises"]:
    PARAMETERS = {
        "workout": {
            "date": datetime.today().strftime("%Y/%m/%d"),
            "time": datetime.today().strftime("%H:%M:%S"),
            "exercise": excercise["name"].title(),
            "duration": excercise["duration_min"],
            "calories": excercise["nf_calories"],
        }
    }

    response = requests.post(url=os.environ.get("SHEETY_API_ENDPOINT"), json=PARAMETERS, headers=SHEETY_HEADERS, auth=basic)
    print(response.text)
