##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv # DONE

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import smtplib
import random
import pandas as pd

letters = []

with open("letter_templates/letter_1.txt") as l1f:
    letters.append(l1f.read())

with open("letter_templates/letter_2.txt") as l2f:
    letters.append(l2f.read())

with open("letter_templates/letter_3.txt") as l3f:
    letters.append(l3f.read())

MY_EMAIL = "hegymegijakotamas@gmail.com"
PASSWORD = "gnuahqrwabtmhaei"

data_dict = pd.read_csv("birthdays.csv").to_dict()


def write_email(name, adress):
    letter_to_send = random.choice(letters)
    letter_to_send.replace('[NAME]', name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, adress, f"Subject:Happy Birthday\n\n{letter_to_send}")


current_month = dt.date.today().month
current_day = dt.date.today().day

for i, (month_value, day_value) in enumerate(zip(data_dict["month"].values(), data_dict["day"].values())):
    if month_value == current_month and day_value == current_day:
        write_email(data_dict["name"][i], data_dict["email"][i])
