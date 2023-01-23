import bs4
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

DRIVER_PATH = "C:\Development\chromedriver.exe"
URL_FORM = "https://docs.google.com/forms/d/e/1FAIpQLScW94M_YrsDlkhyhu8a58-HRRvoRsNLm7pFKZrPwCzHTa9ziQ/viewform?usp=sf_link"
URL_ZILLOW = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66639245996974%2C%22north%22%3A37.88403027709227%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

response = requests.get(URL_ZILLOW, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"})
web_html = response.text


soup = BeautifulSoup(web_html, "html.parser")

addresses = list(map(lambda x: x.getText(), soup.select('address[data-test="property-card-addr"]')))
# print(len(addresses))
# print(addresses)
costs = list(map(lambda x: x.getText()[:6], soup.select('span[data-test="property-card-price"]')))
# print(len(costs))
# print(costs)
links = list(set(list(map(lambda x: x["href"] if x["href"][:4] == "http" else "https://www.zillow.com"+x["href"], soup.select('a[data-test="property-card-link"]')))))
# print(len(links))
# print(links)

service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get(URL_FORM)

for adr, cost, link in zip(addresses, costs, links):
    driver.implicitly_wait(5)
    inputs = driver.find_elements(By.CSS_SELECTOR, 'input[class="whsOnd zHQkBf"]')
    inputs[0].send_keys(adr)
    inputs[1].send_keys(cost)
    inputs[2].send_keys(link)
    time.sleep(0.5)
    send = driver.find_element(By.CSS_SELECTOR, 'div[role="button"]')
    send.click()
    time.sleep(2)
    again = driver.find_element(By.CSS_SELECTOR, "a")
    again.click()

driver.quit()
