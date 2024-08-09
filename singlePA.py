import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import alerts

try:

    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    bookBtn = browser.find_element(By.ID, "book")
    bookBtn.click()

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    x_element = browser.find_element(By.ID, "input_value")
    inputField = browser.find_element(By.ID, "answer")
    x = x_element.text
    submit = browser.find_element(By.XPATH, "//button[@type='submit']")

    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))


    inputField.send_keys(calc(x))
    submit.click()
    alert = browser.switch_to.alert
    print(alert.text)

finally:

    time.sleep(10)
