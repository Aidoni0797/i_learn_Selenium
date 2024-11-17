# тобы получить ответ надо поставить в чекбокс галочку поставить а то не получается блин пишу click но почему то не реагирует
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Список сайтов
sites = ['http://parsinger.ru/blank/1/1.html', 'http://parsinger.ru/blank/1/2.html', 'http://parsinger.ru/blank/1/3.html',
         'http://parsinger.ru/blank/1/4.html', 'http://parsinger.ru/blank/1/5.html', 'http://parsinger.ru/blank/1/6.html',]

# Инициализация драйвера
driver = webdriver.Chrome()

# Список для хранения найденных кодов
codes = []

try:
    # Открытие каждого сайта в новой вкладке
    for site in sites:
        driver.execute_script(f"window.open('{site}', '_blank');")
        time.sleep(2)  # Даем странице время для загрузки

    # Перебор всех вкладок
    for handle in driver.window_handles:
        driver.switch_to.window(handle)

        # Ищем чекбокс на странице (предполагается, что он уникален по ID или классу)
        try:
            checkbox = driver.find_element(By.CLASS_NAME, "checkbox_class")  # Замените на правильный XPath
            time.sleep(20)
            if not checkbox.is_selected():
                checkbox.click()

            # После клика проверяем код на странице (предположим, что код отображается в элементе с ID 'code')
            code_element = driver.find_element(By.ID, "result")  # Замените на правильный ID
            code = int(code_element.text)  # Преобразуем текст в число
            codes.append(code)
        except Exception as e:
            print(f"Ошибка на вкладке {handle}: {e}")

        # Закрытие вкладки
        driver.close()



    # Вычисление суммы квадратных корней
    total_sum = sum(math.sqrt(code) for code in codes)

    # Округление суммы до 9 знаков после запятой
    rounded_sum = round(total_sum, 9)

finally:
    # Закрытие браузера
    driver.quit()

# Выводим итоговую сумму
print(f"Итоговая сумма (округленная): {rounded_sum}")
