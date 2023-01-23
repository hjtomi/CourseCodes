from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import selenium.common.exceptions as ex
import time


class TwitterBot:
    def __init__(self, email, password):
        self.DRIVER_PATH = "C:\Development\chromedriver.exe"
        self.URL = "https://twitter.com/i/flow/login"
        self.EMAIL = email
        self.PASSWORD = password


    def send_tweet(self, msg: str):
        service = Service(self.DRIVER_PATH)
        driver = webdriver.Chrome(service=service)

        driver.get(self.URL)

        time.sleep(10)

        repeat = True
        while repeat:
            try:
                email = driver.find_element(By.NAME, "text")
            except ex.NoSuchElementException:
                time.sleep(2)
            else:
                email.send_keys(self.EMAIL)
                repeat = False

        time.sleep(2)

        next = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next.click()

        time.sleep(2)

        verify = driver.find_element(By.NAME, "text")
        verify.send_keys("hjtomi_")

        next = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
        next.click()

        time.sleep(2)

        pw = driver.find_element(By.NAME, "password")
        pw.send_keys(self.PASSWORD)

        next = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        next.click()

        time.sleep(2)

        tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()

        time.sleep(2)

        content = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        content.send_keys(msg)

        send = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        send.click()

        time.sleep(5)

        driver.quit()
