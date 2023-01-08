# Smart Mail Transfer Protocol LIBrary
import smtplib
import datetime as dt
import random

with open("quotes.txt") as file:
    quotes = [quote.rstrip() for quote in file.readlines()]

my_email = "hegymegijakotamas@gmail.com"
password = "gnuahqrwabtmhaei"


if dt.datetime.now().weekday() == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            my_email,
            my_email,
            f"Subject:Monday motivation\n\n{random.choice(quotes)}"
        )
