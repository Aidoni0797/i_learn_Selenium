import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/blank/modal/1/index.html')
    browser.find_element(By.ID, 'confirm').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.accept() #Замените на .dismiss() чтобы нажать на кнопку "Отмена"
    time.sleep(.5)