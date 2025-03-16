from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настраиваем драйвер (например, Chrome)
driver = webdriver.Chrome()

try:
    # 1. Открываем сайт
    driver.get("https://parsinger.ru/expectations/4/index.html")  # замените на нужный URL

    # 2. Ждем, пока кнопка станет кликабельной (от 1 до 3 секунд)
    button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "btn"))  # замените ID на реальный
    )

    # 3. Кликаем по кнопке
    button.click()

    # 4. Начинаем следить за заголовком
    found = False
    while not found:
        # проверяем заголовок с интервалами (примерно от 0.1 до 0.6 сек)
        WebDriverWait(driver, 0.6)
        if EC.title_contains('JK8HQ')(driver):
            found = True
            secret_title = driver.title
            break

    # 5. Выводим найденный заголовок
    print("iDONi нашла заголовок:", secret_title)

finally:
    driver.quit()
