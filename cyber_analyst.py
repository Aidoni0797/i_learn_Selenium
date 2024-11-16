# чувствуешь себя настоящим кибераналитиком
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.8/3/index.html')
    button = browser.find_element(By.ID, 'check').click
    pins = browser.find_elements(By.CLASS_NAME, 'pin')
    res = []
    for pin in pins:
        res.append(pin.text)

    for i in range(len(res)):
        print(res[i])
        button = browser.find_element(By.ID, 'check').click()
        alert = Alert(browser)
        alert.send_keys(res[i])
        alert.accept()
        answer_field = browser.find_element(By.ID, "result")  # Замените на нужный ID
        # Очистите поле перед вводом текста
        print(answer_field.text)
        # if answer_field != 'Неверный пин-код':
        #     print(answer_field)
        #     break
        time.sleep(2)
time.sleep(.5)