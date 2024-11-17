# не работает логика не верно сформулирован
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Переход на указанный сайт
    driver.get("https://parsinger.ru/selenium/5.8/5/index.html")  # Замените на реальный URL

    # Поиск всех iframe на странице
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Найдено {len(iframes)} iframe")

    # Проходим по каждому iframe
    for index, iframe in enumerate(iframes):
        # Переключаемся в iframe
        driver.switch_to.frame(iframe)

        try:
            # Ищем кнопку внутри iframe
            button = driver.find_element(By.TAG_NAME, "button")  # Замените на правильный локатор, если необходимо
            button.click()  # Нажимаем на кнопку

            # Проверяем появление alert
            time.sleep(1)  # Даем время для появления alert
            alert = Alert(driver)  # Получаем alert
            secret_code = alert.text  # Извлекаем текст из alert
            alert.accept()  # Закрываем alert

            print(f"Найден секретный код: {secret_code}")
            break  # Прекращаем цикл, так как ключ найден
        except Exception as e:
            print(f"На {index + 1}-м iframe кнопка не сработала или alert не появился: {e}")
        finally:
            # Возвращаемся в главный документ
            driver.switch_to.default_content()

    print("Код успешно вставлен в поле ответа")

finally:
    # Закрытие браузера
    driver.quit()
