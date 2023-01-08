import requests
from datetime import date

USERNAME = "hjtomi"
TOKEN = "32edfr4gt5bhy67c597n68w43"

PIXELA_API_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_ACC_INFO = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_API_ENDPOINT, json=PIXELA_ACC_INFO)
# print(response.text)

graph_endpoint = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "minute",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs/graph1"
todays_date_formatted = date.today().strftime("%Y%m%d")

dot_config = {
    "date": todays_date_formatted,
    "quantity": "180"
}

# response = requests.post(url=pixel_creation_endpoint, json=dot_config, headers=headers)
# print(response.text)

pixel_modifying_endpoint = f"{PIXELA_API_ENDPOINT}/{USERNAME}/graphs/graph1/{todays_date_formatted}"

# response = requests.put(url=pixel_modifying_endpoint, json={"quantity": "120"}, headers=headers)

response = requests.delete(pixel_modifying_endpoint, headers=headers)
