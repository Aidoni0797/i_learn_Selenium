# пока не совсем понятно, что-то выдает в консоли
# в курсе описывается список всех cookie, но что это даст, чем полезно
from pprint import pprint
from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://stepik.org/lesson/732061/step/1?unit=733594')
    cookies = webdriver.get_cookies()
    pprint(cookies)