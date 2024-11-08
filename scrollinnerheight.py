from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/scroll/1/')
    height = browser.execute_script("return window.innerHeight")
    print(height)