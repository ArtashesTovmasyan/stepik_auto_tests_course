import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:

    link = "https://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element(By.ID, "input_value")
    inputField = browser.find_element(By.ID, "answer")
    x = x_element.text
    submit = browser.find_element(By.XPATH, "//button[@type='submit']")

    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))

    inputField.send_keys(calc(x))

    submit.click()



finally:

    time.sleep(10)
