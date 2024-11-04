import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    try:
        # Шаг 1: Открытие страницы
        browser.get('https://parsinger.ru/selenium/2/2.html')

        # Шаг 2: Поиск ссылки с текстом "16243162441624"
        link = browser.find_element(By.PARTIAL_LINK_TEXT, "16243162441624")

        # Шаг 3: Клик по найденной ссылке
        link.click()
        time.sleep(2)  # Ожидание загрузки страницы

        # Шаг 4: Получение текста из тега <p id="result"></p>
        result = browser.find_element(By.ID, "result").text

        # Шаг 5: Запись результата
        print("Результат:", result)

    finally:
        # Закрытие браузера
        browser.quit()