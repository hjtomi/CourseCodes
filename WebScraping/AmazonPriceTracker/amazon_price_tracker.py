import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Teskyer-Notebook-College-Softcover-Supplies/dp/B094CX6PGM/ref=sr_1_1_sspa"
amz_headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Accept-Language': 'en-US, en;q=0.5'
}
gmail_adress = "hegymegijakotamas@gmail.com"
gmail_pw = "hlxnnetpgpzdulyw"

response = requests.get(URL, headers=amz_headers)
response.raise_for_status()
web_html = response.content

soup = BeautifulSoup(web_html, "lxml")
dollar = soup.select_one(".a-price-whole").getText().removesuffix(".")
cents = soup.select_one(".a-price-fraction").getText()
price = int(dollar+cents)

if price <= 700:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(gmail_adress, gmail_pw)
        connection.sendmail(gmail_adress, gmail_adress, f"Subject:Amazon price alert!\n\nCheck out \n{URL}")
