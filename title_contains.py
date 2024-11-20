# title_is заработает когда частично совподает с title_contains
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/2/index.html')
    element = WebDriverWait(browser, 10).until(EC.title_contains('tle'))
    print(element)