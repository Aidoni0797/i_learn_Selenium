# код вообще не работает, вручную быстро находить кто-то, iDONi это не выход из ситауции к сожелению
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://parsinger.ru/selenium/5.9/7/index.html')

# Находим все блоки с чекбоксами и кнопками
blocks = driver.find_elements(By.CLASS_NAME, 'parent')

for block in blocks:
    checkbox = block.find_element(By.TAG_NAME, 'input')
    button = block.find_element(By.TAG_NAME, 'button')

    # Ждем, пока чекбокс станет выбранным
    WebDriverWait(driver, 60).until(
        EC.element_to_be_selected(checkbox)
    )
    # Когда чекбокс выбран — кликаем на соответствующую кнопку
    button.click()

# После того, как кликнули все кнопки, забираем секретный код
result = driver.find_element(By.ID, 'result').text
print('Секретный код:', result)

driver.quit()
