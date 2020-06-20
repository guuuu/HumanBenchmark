__author__ = "Gustavo Nascimento"

import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=firefox_options)

driver.get("https://humanbenchmark.com/tests/number-memory")

start = "/html/body/div/div/div[4]/div[1]/div/div/div/div[3]/button"
numeros = "/html/body/div/div/div[4]/div[1]/div/div/div/div[1]"
caixa = "/html/body/div/div/div[4]/div[1]/div/div/div/form/div[2]/input"
submit = "/html/body/div/div/div[4]/div[1]/div/div/div/form/div[3]/button"
nexxt = "/html/body/div/div/div[4]/div[1]/div/div/div/div[2]/button"
ronda = 1
holder = ""

driver.find_element_by_xpath(start).click()

while True:
    try:
        print("============================================================")
        print("Ronda numero {0}".format(ronda))
        ronda += 1
        holder = driver.find_element_by_xpath(numeros).text
        print("O numero é {0}".format(holder))
        WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, caixa))).send_keys(holder)
        print("Input enviado")
        driver.find_element_by_xpath(submit).click()
        print("Botão submeter clicado")
        WebDriverWait(driver, 2000).until(EC.element_to_be_clickable((By.XPATH, nexxt))).click()
        print("Botão next clicado")
    except Exception as ex:
        print("\n\nErro\n\n" + str(ex))
        break

os.remove("./geckodriver.log")