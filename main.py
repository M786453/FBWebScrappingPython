import os
import time

import wget as wget
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = "https://m.facebook.com/KPESED001/photos/pcb.1313884819044193/1313880139044661/?type=3&source=48"

DRIVER_PATH = "C:/Users/Ahtesham Sarwar/Downloads/chromedriver_win32/chromedriver.exe"

PATH = os.getcwd()

os.mkdir("images")

PATH = os.path.join(PATH, "images")

FILENAME = "image"

counter = 1

driver = webdriver.Chrome(DRIVER_PATH)

driver.get(URL)

for x in range(1, 65):
    try:
        time.sleep(5)

        DOWNLOAD_PATH = os.path.join(PATH, FILENAME + str(counter) + ".jpg")

        photo_link = driver.find_element(By.CLASS_NAME, "_57-q")

        print("Photo Link: " + str(photo_link.get_attribute("data-full-size-href")))

        print(DOWNLOAD_PATH)

        wget.download(str(photo_link.get_attribute("data-full-size-href")), DOWNLOAD_PATH)

        elements = driver.find_elements(By.TAG_NAME, "i")

        for element in elements:
            # if element is previous image button then click the element to go to previous image
            if element.get_attribute("class") == "img sp_rxMRFr4y3xC sx_f2af4b":
                element.click()
                break

    except NoSuchElementException:
        print("Element not found")

    counter += 1
