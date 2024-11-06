# с какой целью я использую цикл while но код работает и дал правильный ответ, прикольно, но зачем while
# и когда же я найду ответ6 печально, печально
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'https://parsinger.ru/selenium/5.5/1/1.html'
driver = webdriver.Chrome()

aiDoni = True

while aiDoni:
    driver.get(url)

    input = driver.find_elements(By.CLASS_NAME, "text-field")

    for inp in input:
        inp.clear()

    btn = driver.find_element(By.ID, "checkButton")
    btn.click()

    # Переключаемся на алерт и получаем его текст
    alert = driver.switch_to.alert.text
    print(alert)

    aiDoni = False



