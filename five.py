# Код чуть-чуть работает не правильно
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Открываем сайт
driver = webdriver.Chrome()
driver.get('https://parsinger.ru/selenium/5.9/4/index.html')

wait = WebDriverWait(driver, 30)

# Ждем появления крестика и кликаем на него
close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
close_btn.click()

# Ждем, пока баннер исчезнет
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'banner')))

time.sleep(60)

# После исчезновения баннера жмем на кнопку
result_btn = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
result_btn.click()

# Ловим alert и печатаем код
alert = driver.switch_to.alert
print(alert.text)
alert.accept()

driver.quit()
