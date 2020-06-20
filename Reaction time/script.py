__author__ = "Gustavo Nascimento"

import os
import selenium
from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)

driver.get("https://humanbenchmark.com/tests/reactiontime")

driver.find_element_by_xpath("/html/body/div/div/div[4]/div[1]").click()

for i in range(5):
    print("Tentativa {0}".format(i + 1))
    while True:
        try:
            driver.find_element_by_class_name("view-go").click()
            break
        except:
            try:
                driver.find_element_by_class_name("view-result").click()
            except:
                pass
