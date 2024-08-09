import calc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    lastname = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    file_up = browser.find_element(By.ID, "file")
    submit = browser.find_element(By.TAG_NAME, "button")
    name.send_keys("Artashes")
    lastname.send_keys("Tovmasyan")
    email.send_keys("examplefake@yopmail.com")
    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'ReadMe.txt')
    file_up.send_keys(file_path)
    submit.click()





finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
