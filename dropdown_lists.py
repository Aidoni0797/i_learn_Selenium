# все работает вот бы в реальной жизне так нет думаешь и сидишь блин
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/7/7.html')
    opts = browser.find_elements(By.TAG_NAME, 'option')
    rst = 0
    for opt in opts:
        rst += int(opt.text)

    input_result = browser.find_element(By.ID, "input_result").send_keys(rst)

    # Шаг 3: Клик по найденной ссылке
    time.sleep(2)  # Ожидание загрузки страницы
    btn = browser.find_element(By.CLASS_NAME, "btn").click()

    # Шаг 4: Получение текста из тега <p id="result"></p>
    result = browser.find_element(By.ID, "result").text

    # Шаг 5: Запись результата
    print("Результат:", result)