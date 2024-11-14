from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

# Инициализация драйвера и открытие сайта
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.7/5/index.html")

# Убедитесь, что страница загрузилась полностью
time.sleep(2)

# Найдите все кнопки
buttons = driver.find_elements(By.TAG_NAME, "button")

# Для каждой кнопки считываем значение и удерживаем нажатие
for button in buttons:
    # Получаем значение value для времени удержания
    hold_time = float(button.get_attribute("value"))

    # Удержание кнопки с использованием ActionChains
    actions = ActionChains(driver)
    actions.click_and_hold(button).perform()
    time.sleep(hold_time)  # Удерживаем кнопку в течение времени hold_time
    actions.release(button).perform()  # Отпускаем кнопку

# Дождитесь появления alert с сообщением
alert = Alert(driver)
alert_text = alert.text
alert.accept()  # Закрытие alert-окна

print(alert_text)

# Завершение работы и закрытие драйвера
time.sleep(2)  # Небольшая задержка, чтобы убедиться, что ответ отправлен
driver.quit()
