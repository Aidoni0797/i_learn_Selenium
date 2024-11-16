# Очень долго решала, ну очень долго
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    # Откройте сайт
    url = "https://parsinger.ru/window_size/2/index.html"  # Замените на нужный сайт
    driver.get(url)

    # Списки размеров
    window_size_x = [616, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
    window_size_y = [300, 330, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

    # Перебор размеров
    found = False
    for width in window_size_x:
        for height in window_size_y:
            # Изменение размера окна
            driver.set_window_size(width+16, height+147)

            # Проверка содержимого элемента с id="result"
            try:
                result_element = driver.find_element(By.ID, "result")
                result_text = result_element.text.strip()

                # Проверка: появилось ли число
                if result_text.isdigit():
                    print(f"Найдено! Размеры: {width}x{height}, Число: {result_text}")
                    found = True
                    break
            except Exception:
                # Элемент не найден или текст отсутствует
                pass
        if found:
            break
finally:
    # Закрытие браузера
    driver.quit()
