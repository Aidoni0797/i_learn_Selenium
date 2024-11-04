import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    try:
        # Шаг 1: Открытие страницы
        browser.get('https://parsinger.ru/selenium/3/3.html')

        # Извлечение всех тегов <p>
        fragments = browser.find_elements(By.TAG_NAME, "p")

        # Суммирование числовых значений в каждом теге <p>
        total_sum = 0
        for fragment in fragments:
            print(fragment.text)
            try:
                # Преобразование текста в число и добавление к сумме
                total_sum += int(fragment.text)
            except ValueError:
                # Игнорируем значения, которые не являются числами
                continue

        # Вывод итоговой суммы
        print("Общая сумма:", total_sum)

    finally:
        # Закрытие браузера
        browser.quit()