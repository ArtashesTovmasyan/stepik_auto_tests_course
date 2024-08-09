import calc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")
    num1 = int(num1_element.text)

    num2 = int(num2_element.text)


    def calc():
        return num1 + num2


    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(calc()))
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
