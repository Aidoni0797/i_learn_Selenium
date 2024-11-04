# было не легко пока понять логику блин
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
        for i, fragment in enumerate(fragments):
            if int(fragment.text) % 2 == 0:  # Проверка каждого второго тега <p>, а скорее всего на четное число зачем я использую enumerate ладно пускай стоит
                try:
                    print(fragment.text)
                    # Преобразование текста в число и добавление к сумме
                    total_sum += int(fragment.text)
                    i += 1
                except ValueError:
                    # Игнорируем значения, которые не являются числами
                    continue


        # Вывод итоговой суммы
        print("Общая сумма:", total_sum)

    finally:
        # Закрытие браузера
        browser.quit()
