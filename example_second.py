from selenium import webdriver
from selenium.webdriver.common.by import By
import time


browser = webdriver.Chrome()
browser.get('http://parsinger.ru/html/watch/1/1_1.html')
button = browser.find_element(By.ID, "sale_button").click()

time.sleep(10)