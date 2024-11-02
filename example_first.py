import time
from selenium import webdriver

url = 'https://stepik.org/course/104774'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)