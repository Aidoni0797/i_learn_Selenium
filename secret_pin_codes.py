# очень долго работает учи aiDoni учи
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/2/index.html')
    buttons = browser.find_elements(By.CLASS_NAME, 'buttons')

    for butt in buttons:
        butt.click()
        # prompt = browser.switch_to.alert
        alert = browser.switch_to.alert
        promt_text = alert.text
        alert.accept()
        # Найдите элемент поля ввода
        answer_field = browser.find_element(By.ID, "input")  # Замените на нужный ID
        # Очистите поле перед вводом текста
        answer_field.clear()
        # Введите новый текст
        answer_field.send_keys(promt_text)
        # result = browser.find_element(By.ID, "input").send_keys(promt_text)
        time.sleep(2)
        bbt = browser.find_element(By.ID, "check").click()
        time.sleep(2)
        pbt = browser.find_element(By.ID, "result").text
        if pbt != 'Неверный пин-код':
            print("Секретный код найден:", pbt)
            break

time.sleep(.5)