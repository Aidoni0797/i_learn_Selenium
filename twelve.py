import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By



with webdriver.Chrome() as driver:
    driver.get("https://parsinger.ru/selenium/5.10/7/index.html")
    element_to_drag = driver.find_element(By.ID, "click_and_hold")
    time.sleep(1)
    # Создание объекта ActionChains, инициализация операции перетаскивания элемента на 500 пикселей вправо
    # и выполнение цепочки действий
    ActionChains(driver).drag_and_drop_by_offset(element_to_drag, 500, 0).release().perform()

    time.sleep(10) 