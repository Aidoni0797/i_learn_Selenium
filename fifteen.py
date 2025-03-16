# код вроде рабочий и дал ответ верный, но как то заканчивает некрасиво
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Запуск браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://parsinger.ru/draganddrop/1/index.html')

# Находим красный блок
block = driver.find_element(By.ID, 'draggable')

# Находим второе поле для перетаскивания
target = driver.find_element(By.ID, 'field2')

# Перетаскиваем блок с помощью ActionChains
actions = ActionChains(driver)
actions.drag_and_drop(block, target).perform()

# Ждем появления токена
token = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'token'))
).text

# Вставляем токен в поле ввода и отправляем
input_field = driver.find_element(By.ID, 'input')
input_field.send_keys(token)

driver.find_element(By.ID, 'submit').click()

print('Токен успешно отправлен!')

driver.quit()
