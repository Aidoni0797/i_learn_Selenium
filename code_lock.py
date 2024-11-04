# логика данного кода решен без chatGPT я в шоке начинаю хоть что то понимать
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    try:
        # Шаг 1: Открытие страницы
        browser.get('https://parsinger.ru/selenium/4/4.html')

        # Шаг 2: Поиск check
        checks = browser.find_elements(By.CLASS_NAME, "check")

        for check in checks:
            check.click()

        # Шаг 3: Клик по найденной ссылке
        time.sleep(2)  # Ожидание загрузки страницы
        btn = browser.find_element(By.CLASS_NAME, "btn").click()

        # Шаг 4: Получение текста из тега <p id="result"></p>
        result = browser.find_element(By.ID, "result").text

        # Шаг 5: Запись результата
        print("Результат:", result)

    finally:
        # Закрытие браузера
        browser.quit()