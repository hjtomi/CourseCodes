from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

DRIVER_PATH = "C:\Development\chromedriver.exe"
PW = os.environ.get("PASSWORD")

service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3401885989&f_AL=true&geoId=100288700&keywords=python%20developer&location=Hungary&refresh=true")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "nav__button-secondary").click()
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("hjtomipls@gmail.com")
driver.find_element(By.ID, "password").send_keys(PW)
driver.find_element(By.CLASS_NAME, "btn__primary--large").click()
time.sleep(2)
jobs = driver.find_elements(By.CSS_SELECTOR, ".full-width.artdeco-entity-lockup__title a")
for job in jobs:
    job.click()
    time.sleep(2)
    apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
    apply_btn.click()
    time.sleep(999)


time.sleep(9999)


driver.quit()
