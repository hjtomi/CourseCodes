# Webscraping https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors for updated data
import pandas as pd
import bs4
import requests

data_dict = {
    'rank': [],
    'major': [],
    'degree_type': [],
    'early_career_pay': [],
    'mid_career_pay': [],
    'percentage_high_meaning': [],
}

for i in range(1, 35):
    print(i)
    web_html = requests.get(f'https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}').text
    soup = bs4.BeautifulSoup(web_html, 'html.parser')

    data_names = ['rank', 'major', 'degree_type', 'early_career_pay', 'mid_career_pay', 'percentage_high_meaning']

    for data, data_name in zip(map(lambda x: x.text, soup.select('.data-table__value')), data_names*999):
        data_dict[data_name].append(data)
