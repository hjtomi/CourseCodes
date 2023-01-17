from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get(
    "https://www.amazon.com/Dabo-Shobo-Highlighters-Assorted-Colors/dp/B09TVVYKZQ/ref=sr_1_2_sspa?keywords=highlighters&qid=1673875092&sprefix=hig%2Caps%2C242&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSUZWVzFEMTgyTExPJmVuY3J5cHRlZElkPUEwMzc1NjA4MkdZNlA1TjVRNk9aQSZlbmNyeXB0ZWRBZElkPUEwNjAwMDI1MzVEOTlHWTRIUzY1OCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
)

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print("Check", price.tag_name)
print(price.get_attribute('innerHTML'))
