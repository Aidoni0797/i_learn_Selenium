import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')

    # Ищем все div с классом 'text'
    divs = browser.find_elements(By.CLASS_NAME, 'form')

    # Проходимся по каждому div
    for i, div in enumerate(divs):
        a1 = div.find_element(By.XPATH, '/html/body/div/div/div[3]/input').send_keys('T')
        a2 = div.find_element(By.XPATH, '/html/body/div/div/div[4]/input').send_keys('T')
        a3 = div.find_element(By.XPATH, '/html/body/div/div/div[5]/input').send_keys('T')
        a4 = div.find_element(By.XPATH, '/html/body/div/div/div[6]/input').send_keys('T')
        a5 = div.find_element(By.XPATH, '/html/body/div/div/div[7]/input').send_keys('T')
        a6 = div.find_element(By.XPATH, '/html/body/div/div/div[8]/input').send_keys('T')

    # Находим элемент (например, по ID) и кликаем по нему
    element = browser.find_element(By.ID, 'btn')
    element.click()

    # Опционально ждем несколько секунд, чтобы увидеть результат
    time.sleep(5)

    # # Закрываем браузер
    # browser.quit()