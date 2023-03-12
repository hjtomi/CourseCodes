# Webscraping https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors for updated data
import pandas as pd
from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')
page_html = response.text

soup = BeautifulSoup(page_html, 'html.parser')
table = soup.find(_class='data-table', name="table")
print(table)

df = pd.read_html('https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors')

