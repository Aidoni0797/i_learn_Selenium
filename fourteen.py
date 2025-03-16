from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

with webdriver.Chrome() as driver:
    # Ожидание загрузки элементов (10 секунд)
    driver.implicitly_wait(10)

    # Открытие локальной HTML страницы
    driver.get("https://parsinger.ru/selenium/5.10/9/index.html")

    # Поиск элемента (квадрата) на странице
    square = driver.find_element(By.CSS_SELECTOR, "canvas")

    # Создание объекта ActionChains для выполнения действий с элементами
    actions = ActionChains(driver)

    # Передвижение квадрата на указанные координаты
    actions.click_and_hold(square).move_by_offset(100, -100).release().perform()

    # Пауза для визуальной проверки результата
    time.sleep(5)