# код который не дает вообще результата
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Порядок кодов, который нужно собрать
order = ['YS93', 'R9R3', 'S019', 'PPI7', 'OS80', '012C']

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://parsinger.ru/selenium/5.9/5/index.html')

# Словарь для хранения кодов
code_parts = {}

# Находим все кнопки
buttons = driver.find_elements(By.CLASS_NAME, 'btn')

for btn in buttons:
    btn.click()

    # Ждем появления и закрываем рекламу
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'close'))
    )
    driver.find_element(By.CLASS_NAME, 'close').click()

    # Ждем появления кода на кнопке
    WebDriverWait(driver, 10).until(lambda d: btn.text != '')

    part = btn.text


    code_parts[part[:4]] = part

print('Все найденные коды:', code_parts)

# Проверим, все ли коды собраны
if all(key in code_parts for key in order):
    final_key = '-'.join([code_parts[k] for k in order])
    print('Итоговый ключ:', final_key)
else:
    print('Не удалось найти все части кода!')

driver.quit()
