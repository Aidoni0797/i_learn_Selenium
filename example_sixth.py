import time
from selenium import webdriver
from selenium.webdriver.common.by import By


try:
    driver= webdriver.Chrome()
    driver.get('http://parsinger.ru/html/watch/1/1_1.html')
    button = driver.find_element(By.ID, "sale_button")
    time.sleep(2)
    button.click()
    time.sleep(2)
finally:

    # Окно браузера закроется в любом случае
    driver.quit()