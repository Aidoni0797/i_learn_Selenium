# очень увлекательная задача
import time
from pprint import pprint
from selenium import webdriver

cookies_data = []

with webdriver.Chrome() as webdriver:
    webdriver.get('https://parsinger.ru/methods/3/index.html')
    cookies = webdriver.get_cookies()
    for cookie in cookies:
        if 'value' in cookie:
            cookies_data.append(cookie['value'])

res = 0

for cook in cookies_data:
    res += int(cook)

pprint(res)
