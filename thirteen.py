from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

url = "https://parsinger.ru/selenium/5.10/7/index.html"

# Инициализация драйвера
with webdriver.Chrome() as driver:
    # Устанавливаем неявное ожидание для всех элементов
    driver.implicitly_wait(10)

    # Переход на страницу
    driver.get(url)
    time.sleep(1)
    # Поиск элемента для перетаскивания и контейнера
    click_and_hold_element = driver.find_element(By.ID, "click_and_hold")
    container = driver.find_element(By.CLASS_NAME, "container")

    # Выполнение операции перетаскивания
    actions = ActionChains(driver)
    actions.click_and_hold(click_and_hold_element).move_to_element(container).release().perform()

    # Даем время для визуальной проверки (по желанию)
    time.sleep(5)