# немного надо было подумать учи aiDoni учи
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with webdriver.Chrome() as browser:
    browser.get(' https://parsinger.ru/selenium/5.8/1/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')

    for butt in buttons:
        result = browser.find_element(By.ID, "result").text
        if result != '':
            print("Секретный код найден:", result)
            break  # Остановить цикл, если код найден
        else:
            butt.click()
            prompt = browser.switch_to.alert
            prompt.accept()

time.sleep(.5)