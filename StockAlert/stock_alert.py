import requests
import datetime as dt
from twilio.rest import Client

MY_NUMBER = "+36302804337"

TWILIO_SID = "ACacfd54ccaa982ab8251548c8f40650a0"
TWILIO_AUTH_TOKEN = "0975f63c35575996deab22ab5b88ac37"
TWILIO_NUMBER = "+13856006090"

DATE_YESTERDAY = str(dt.date.today() - dt.timedelta(3))
DATE_BEFORE_YESTERDAY = str(dt.date.today() - dt.timedelta(4))
print(DATE_YESTERDAY, DATE_BEFORE_YESTERDAY)

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_ENDPOINT_STOCKS = "https://www.alphavantage.co/query"
API_ENDPOINT_NEWS = "https://newsapi.org/v2/everything"

API_KEY_STOCKS = "97JA2IZ9CQR7K45X"
API_KEY_NEWS = "1d7675e8ad334184bbdbb98ec7703d7b"

PARAMETERS_STOCKS = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API_KEY_STOCKS
}
PARAMETERS_NEWS = {
    "q": "tesla",
    "from": "2022-12-24",
    "sortBy": "publishedAt",
    "apiKey": "1d7675e8ad334184bbdbb98ec7703d7b"
}

response = requests.get(API_ENDPOINT_STOCKS, PARAMETERS_STOCKS)
response.raise_for_status()

data_stock = response.json()
day_values = data_stock["Time Series (Daily)"]

yesterday_close_value = float(day_values[DATE_YESTERDAY]["4. close"])
before_yesterday_close_value = float(day_values[DATE_BEFORE_YESTERDAY]["4. close"])

close_price_diff = round(yesterday_close_value - before_yesterday_close_value, 3)

change_percentage = round((close_price_diff / yesterday_close_value) * 100, 2)


def send_message():
    response = requests.get(API_ENDPOINT_NEWS, PARAMETERS_NEWS)
    response.raise_for_status()

    data = response.json()
    most_recent_article = data["articles"][0]
    most_recent_article_headline = most_recent_article["title"]
    most_recent_article_brief = most_recent_article["description"].split(".")[0]

    body_to_send = f"""{STOCK}: {change_str}\nHeadline: {most_recent_article_headline}.\nBrief: {most_recent_article_brief}."""

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body_to_send,
        from_=TWILIO_NUMBER,
        to=MY_NUMBER
    )


if change_percentage < -5:
    change_str = f"🔻{change_percentage[1:]}%"
    send_message()

elif change_percentage > 5:
    change_str = f"🔺{change_percentage}%"
    send_message()
