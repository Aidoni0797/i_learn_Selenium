# надо быть внимательным
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
with webdriver.Chrome() as browser:
    try:
        # Шаг 1: Открытие страницы
        browser.get('https://parsinger.ru/selenium/6/6.html')
        target = ((12434107696 * 3) * 2) + 1
        # Найдите элемент <select> по его ID или другому локатору
        select_element = browser.find_element(By.ID, "selectId")  # Замените на фактический ID элемента
        # Создание объекта Select для работы с выпадающим списком
        select = Select(select_element)
        select.select_by_visible_text(str(target))
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
