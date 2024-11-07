# самое худшее решение
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/selenium/5.5/3/1.html")  # Замените на URL вашей основной страницы

total_sum = 0

textarea = driver.find_elements(By.TAG_NAME, "textarea")
checkbox = driver.find_elements(By.CLASS_NAME, "checkbox")

t = []
c = []

for tex in textarea:
    t.append(tex.text)

for chk in checkbox:
    if chk.is_selected():
        c.append('True')
    else:
        c.append('False')

for i in range(0, len(c)):
    if c[i] == 'True':
        total_sum += int(t[i])

print(total_sum)

driver.quit()