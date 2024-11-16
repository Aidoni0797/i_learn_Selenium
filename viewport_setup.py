# чувствуешь себя настоящим кибераналитиком
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/window_size/1/')
    browser.set_window_size(571, 702)
    time.sleep(10)
    print(browser.find_element(By.ID, 'result').text)
time.sleep(.5)