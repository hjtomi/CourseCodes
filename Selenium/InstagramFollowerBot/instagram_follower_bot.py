# Open instagram login page
# Log in
# Go to a profile click on followings and follow everyone

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

DRIVER_PATH = "C:\Development\chromedriver.exe"
URL_INSTA = "https://www.instagram.com/"
URL_USER = "https://www.instagram.com/etelmuhely/followers/"

# Setup
service = Service(DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get(URL_INSTA)

time.sleep(5)

# Log in
cookies = driver.find_element(By.CLASS_NAME, '_a9_1')
cookies.click()
time.sleep(5)
username = driver.find_element(By.NAME, "username")
username.send_keys("gordon_mersi")
password = driver.find_element(By.NAME, "password")
password.send_keys(os.environ.get("PASSWORD"))
time.sleep(5)
login = driver.find_element(By.CSS_SELECTOR, "._acan._acap._acas._aj1-")
login.click()
time.sleep(5)
infosave = driver.find_element(By.CSS_SELECTOR, "._acan._acao._acas._aj1-")
infosave.click()
time.sleep(3)
noti = driver.find_element(By.CSS_SELECTOR, "._a9--._a9_1")
noti.click()

time.sleep(3)

# Go to a profile click on followings and follow everyone
driver.get(URL_USER)
time.sleep(4)
follow_buttons = driver.find_element(By.XPATH, '//*[@id="f1a706f4daa9c54"]/button')
follow_buttons.click()
# for follow_button in follow_buttons:
#     follow_button.click()

time.sleep(999)

driver.quit()
