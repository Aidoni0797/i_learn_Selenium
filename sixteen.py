from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Открываем браузер и переходим на сайт
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://parsinger.ru/draganddrop/3/index.html')

# Находим синий квадрат
blue_square = driver.find_element(By.ID, 'block1')

# Находим все красные точки (ориентиры) в порядке следования слева направо
red_points = driver.find_elements(By.CLASS_NAME, 'point')

actions = ActionChains(driver)

# Проводим синий квадрат через все красные точки
for point in red_points:
    actions.click_and_hold(blue_square).move_to_element(point).release().perform()
    time.sleep(0.5)  # Добавляем небольшую паузу для плавности

# Ждем появления токена
token = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'token'))
).text

# Вставляем токен в поле и нажимаем на кнопку
driver.find_element(By.ID, 'input').send_keys(token)
driver.find_element(By.ID, 'submit').click()

print('Токен успешно отправлен!')

driver.quit()
