from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

MY_CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

service = Service(MY_CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

events = list(map(lambda x: x.text, driver.find_elements(By.CSS_SELECTOR, ".event-widget time")))
times = list(map(lambda x: x.text, driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")))
print(events)
print(times)

event_dict = {}
for i, (time, event) in enumerate(zip(times, events)):
    event_dict[i+1] = {
        "time": time,
        "event": event
    }
print(event_dict)
