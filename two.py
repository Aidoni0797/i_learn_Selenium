from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
with webdriver.Chrome() as browser:
    # Шаг 1: Открываем сайт
    browser.get("https://parsinger.ru/expectations/6/index.html")  # Замените на нужный URL

    # Шаг 2: Находим кнопку и кликаем по ней
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, "btn"))
    )
    button.click()

    # Шаг 3: Ожидаем появления элемента с классом "BMH21YY"
    target_element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "BMH21YY"))
    )

    # Шаг 4: Извлекаем текст элемента
    secret_code = target_element.text
    print(f"iDONi нашла код: {secret_code}")
