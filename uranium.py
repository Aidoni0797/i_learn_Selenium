# как хорошо что существует chatgpt - хех - прикольно
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

# Инициализация веб-драйвера и открытие сайта
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.7/1/index.html")  # Замените "URL_САЙТА_ЗДЕСЬ" на фактический URL

# Убедитесь, что страница загрузилась полностью
time.sleep(2)

# Найдите все кусочки урана
uranium_pieces = driver.find_elements(By.CLASS_NAME, "clickMe")
print(len(uranium_pieces))
i = 0
# Прокрутка к каждому кусочку и клик по нему
for piece in uranium_pieces:
    i += 1
    driver.execute_script("return arguments[0].scrollIntoView(true);", piece)
    piece.click()
    if i == len(uranium_pieces):
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
        print(alert_text)




# Закрытие драйвера
time.sleep(200)
driver.quit()
