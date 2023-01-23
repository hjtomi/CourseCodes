from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class SpeedtestBot:
    def __init__(self):
        self.DRIVER_PATH = "C:\Development\chromedriver.exe"
        self.URL = "https://www.speedtest.net/"

    def check_speeds(self) -> dict:
        """Returns a dict containing the download and upload speed.
        Dictionary format:
        {"download": value, "upload": value}"""
        service = Service(self.DRIVER_PATH)
        driver = webdriver.Chrome(service=service)

        driver.get(self.URL)

        time.sleep(10)

        go = driver.find_element(By.CLASS_NAME, "js-start-test")
        go.click()

        time.sleep(45)

        download = driver.find_element(By.CLASS_NAME, "download-speed")
        download_speed = float(download.text)

        upload = driver.find_element(By.CLASS_NAME, "upload-speed")
        upload_speed = float(upload.text)

        driver.quit()

        return {"download": download_speed, "upload": upload_speed}
