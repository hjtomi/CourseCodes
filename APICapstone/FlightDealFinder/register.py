import credentials
import requests

print("Welcome to 'hj flight deals' where you get notified about bargains!")
first = str(input("What is your first name? "))
last = str(input("What is your last name? "))
email = str(input("What is your email? "))
remail = ""
while remail != email:
    remail = str(input("Please confirm your email! "))

user_data = {
    "user": {
        "firstName": first,
        "lastName": last,
        "email": email
    }
}

response = requests.post(credentials.Users.API_ENDPOINT, json=user_data, headers=credentials.Users.API_HEADERS, auth=credentials.Users.BASIC)
print("You are in the club!")
