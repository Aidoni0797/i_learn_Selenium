from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запуск браузера
with webdriver.Chrome() as browser:
    # Шаг 1: Открыть сайт
    browser.get("https://parsinger.ru/selenium/5.9/2/index.html")  # Замените на реальный URL

    # Шаг 2: Следить за появлением блока с ID "qQm9y1rk"
    try:
        # Ждём появления блока, например, в течение 60 секунд
        block = WebDriverWait(browser, 60).until(
            EC.presence_of_element_located((By.ID, "qQm9y1rk"))
        )

        # Шаг 3: Быстро кликаем на него
        block.click()

        # Шаг 4: Ловим alert с секретным кодом
        alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
        print("Секретный код:", alert.text)
        alert.accept()

    except Exception as e:
        print("Блок не найден или не удалось кликнуть:", e)
