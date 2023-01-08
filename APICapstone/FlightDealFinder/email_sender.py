from credentials import Users
from deal_finder import DealFinder
import smtplib
import requests

df = DealFinder()

bargains = df.find_bargains()

message = ""
for bargain in bargains:
    route = bargain["route"][0]
    message += f"{route['cityFrom']}-{route['flyFrom']} to {route['cityTo']}-{route['flyTo']} for {bargain['price']} pounds on \n{route['utc_departure'][:10]}\n\n"

email_body = f"Subject:{len(bargains)} low-cost flight available!\n\n{len(bargains)} low-cost flight available!\n\n{message}"

response = requests.get(Users.API_ENDPOINT, headers=Users.API_HEADERS, auth=Users.BASIC)

data = response.json()

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login("hegymegijakotamas@gmail.com", "seglppvtwdgporpu")

    for row in data["users"]:
        connection.sendmail("hegymegijakotamas@gmail.com", row["email"], msg=email_body)
