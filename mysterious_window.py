# chatgpt ты облегчаешь жизнь
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ваши списки размеров окон
window_size_x = [516, 648, 680, 701, 730, 750, 805, 820, 855, 890, 955, 1000]
window_size_y = [270, 300, 340, 388, 400, 421, 474, 505, 557, 600, 653, 1000]

# Словарь для результата
result = {}


# Создаем экземпляр драйвера
driver = webdriver.Chrome()

try:
    # Открываем сайт
    driver.get("https://parsinger.ru/window_size/2/index.html")  # Замените на ваш URL

    # Перебираем размеры окон
    for width in window_size_x:
        for height in window_size_y:
            # Устанавливаем размер окна
            driver.set_window_size(width+16, height+147)

            # Проверяем наличие числа в id="result"
            element = driver.find_element(By.ID, "result")
            if element.text.isdigit():  # Проверяем, является ли текст числом
                time.sleep(10)
                result = {'width': width, 'height': height}
                break
        if result:
            break

finally:
    # Закрываем браузер
    driver.quit()

# Выводим результат
print(result)
