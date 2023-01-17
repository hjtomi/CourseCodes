# Import the modules!
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

MY_CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
# Create a Service object and pass in the driver path (MY_CHROME_DRIVER_PATH)
service = Service(MY_CHROME_DRIVER_PATH)
# Create a Chrome Webdriver object and fulfill the "service" parameter with the previously created service object
driver = webdriver.Chrome(service=service)

# Make the webdriver go to the desired webpage
driver.get("https://www.youtube.com")

# ! Here are the different search choices by precision ascending ! #

# name property
driver.find_element(By.NAME, "q")
# class name
driver.find_element(By.CLASS_NAME, "placeholder")
# ".documentation-widget" is a parent div, "a" is the children we are looking for
driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# anchor tag text
driver.find_element(By.LINK_TEXT, "text of an anchor tag")
# the most specific is "xpath": to get it, right-click on the corresponding html code and select Copy --> Copy Xpath
driver.find_element(By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr/td[2]/span[1]/span[1]')
