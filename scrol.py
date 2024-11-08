import time
from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    for i in range(10):
        browser.execute_script("window.scrollBy(0,5000)")
        time.sleep(2)