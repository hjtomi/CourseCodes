from datetime import datetime
import requests
import smtplib
import time

# setup
MY_LAT = 46.911016
MY_LONG = 19.693761
EMAIL = "hegymegijakotamas@gmail.com"
PASSWORD = "gnuahqrwabtmhaei"


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, EMAIL, "Subject:Nezz fel!\n\nAz ISS feletted van. Nezz fel.")


# logic
while True:
    # iss api
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    iss_position = (latitude, longitude)

    # sunrise sunset api
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    # check
    if (MY_LAT-5 <= latitude <= MY_LAT+5 and MY_LONG-5 <= longitude <= MY_LONG+5) and (time_now <= sunrise or time_now >= sunset):
        print("sending email")
        send_email()
        print("email sent")

    time.sleep(60)
