import math

import calc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    inputField = browser.find_element(By.ID, "answer")
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    robotsRule = browser.find_element(By.ID, "robotsRule")
    submitButton = browser.find_element(By.TAG_NAME, "button")
    x = x_element.text


    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))


    inputField.send_keys(calc(x))
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)
    checkbox.click()
    robotsRule.click()
    submitButton.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
