from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

# Использование контекстного менеджера для управления драйвером
with webdriver.Chrome() as driver:
    # Загрузите локальный HTML-файл
    driver.get('https://parsinger.ru/selenium/5.10/5/index.html')

    slider = driver.find_element(By.ID,'volume')
    width = slider.size['width']
    # Вычислите смещение для 1 единицы
    offset = width / 100

    actions = ActionChains(driver)

    # Нажмите на ползунок и удерживайте кнопку мыши
    actions.click_and_hold(slider).perform()

    # В цикле перемещайте ползунок на 1 единицу
    for _ in range(10):  # пример для 10 шагов
        actions.move_by_offset(offset, 0).perform()
        time.sleep(0.1)  # пауза для наглядности

    # Отпустите кнопку мыши
    actions.release().perform()