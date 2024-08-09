import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    inputField = browser.find_element(By.ID, "answer")
    submit = browser.find_element(By.XPATH, "//button[text()='Submit']")

    x = x_element.text


    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))


    inputField.send_keys(calc(x))
    submit.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
