from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/methods/5/index.html")  # Укажите URL главной страницы

# Получение всех ссылок на главной странице
links = driver.find_elements(By.TAG_NAME, 'a')  # Найти все элементы <a> на странице
urls = [link.get_attribute('href') for link in links[:42]]  # Список URL первых 42 ссылок

# Список для хранения данных о cookie
cookies_data = []

# Переход по каждой ссылке и анализ cookie
for url in urls:
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))  # Ожидание загрузки страницы
    cookies = driver.get_cookies()
    for cookie in cookies:
        if 'expiry' in cookie:
            cookies_data.append((url, cookie['expiry']))  # Сохранить URL и срок действия cookie

# Поиск cookie с максимальным сроком жизни
max_expiry_cookie = max(cookies_data, key=lambda x: x[1])
max_url = max_expiry_cookie[0]  # URL страницы с "Бессмертным Печенюшкой"

# Переход на страницу с максимальным сроком жизни cookie и получение результата
driver.get(max_url)
result = driver.find_element(By.ID, "result").text  # Извлечение числа из тега <p id="result">

print(result)

# Закрытие драйвера
driver.quit()
