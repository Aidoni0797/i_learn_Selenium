from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ids_to_find = [
    'xhkVEkgm', 'QCg2vOX7', '8KvuO5ja', 'CFoCZ3Ze', '8CiPCnNB',
    'XuEMunrz', 'vmlzQ3gH', 'axhUiw2I', 'jolHZqD1', 'ZM6Ms3tw',
    '25a2X14r', 'aOSMX9tb', 'YySk7Ze3', 'QQK13iyY', 'j7kD7uIR'
]

# Запуск браузера
with webdriver.Chrome() as browser:
    browser.get("https://parsinger.ru/selenium/5.9/3/index.html")  # Замените на нужный URL

    clicked_ids = set()

    try:
        for key_id in ids_to_find:
            # Ждем появления элемента с нужным ID и видимостью
            element = WebDriverWait(browser, 60).until(
                EC.visibility_of_element_located((By.ID, key_id))
            )
            element.click()
            clicked_ids.add(key_id)
            print(f'Активирован портал: {key_id}')

        # Ждем появления алерта с секретным кодом
        alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
        print("Секретный код:", alert.text)
        alert.accept()

    except Exception as e:
        print("Что-то пошло не так:", e)
