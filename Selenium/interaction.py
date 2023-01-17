from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MY_CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"

service = Service(MY_CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://app.usertesting.com/users/sign_in")

# Click on a link
# wiki_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# wiki_articles.click()

# Pass inputs to search bar
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)

input_email = driver.find_element(By.NAME, "email")
input_pw = driver.find_element(By.NAME, "password")
btn_log_in = driver.find_element(By.CLASS_NAME, "btn--primary")

input_email.send_keys("testmail@dzsimail.kom")
input_pw.send_keys("ezajelszom")
btn_log_in.click()

time.sleep(3)

driver.quit()

