__author__ = "Gustavo Nascimento"

import os
import selenium
from selenium import webdriver
import time

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)

driver.get("https://humanbenchmark.com/tests/aim")

driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]/div/div[2]").click()

while True:
    try:
        driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]/div/div[2]/div/div/div[6]").click()
    except Exception as ex:
        print(ex)
        break

#driver.quit()
#os.remove("./geckodriver.log")