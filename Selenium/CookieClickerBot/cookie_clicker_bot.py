from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions as exceptions
import time

# SETUP
CHROME_WEBDRIVER_PATH = "C:\Development\chromedriver.exe"
COOKIE_CLICKER_URL = "https://orteil.dashnet.org/cookieclicker/"

service = Service(CHROME_WEBDRIVER_PATH)
driver = webdriver.Chrome(service=service)

# LOAD WEBSITE
driver.get(COOKIE_CLICKER_URL)
# Loading delay
time.sleep(8)

english = driver.find_element(By.ID, "langSelect-EN")
english.click()
# Loading delay
time.sleep(4)

# WEB VARIABLES
big_cookie = driver.find_element(By.ID, "bigCookie")
cookies = driver.find_element(By.ID, "cookies")
actual_cookies = int(cookies.text.partition(" ")[0])

# LOGIC VARIABLES
QUIT_AFTER_COOKIES = 100

# LOGIC
iteration = 0
while True:
    # Delays
    if iteration % 50 == 0:
        purchasable_buildings = driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        if purchasable_buildings:
            purchasable_buildings[-1].click()

        try:
            upgrade = driver.find_element(By.XPATH, '//*[@id="upgrade0"]')
        except exceptions.NoSuchElementException:
            pass
        else:
            try:
                upgrade.click()
            except exceptions.StaleElementReferenceException:
                pass

    big_cookie.click()

    iteration += 1
