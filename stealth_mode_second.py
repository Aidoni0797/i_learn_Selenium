# код работает без файла coordinates.crx и aiDoni не знает где его получить, плохо очень плохо
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless=chrome')
# options_chrome.add_extension('coordinates.crx') где мне найти этот файл




with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)
    time.sleep(5)
    a = browser.find_element(By.TAG_NAME, 'a')
    print(a.get_attribute('href'))