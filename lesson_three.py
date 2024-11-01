import time
from selenium import webdriver
# эти строки кода открывает именно ссылку где расположен курс, прикольно, типа аналог кода
# зачем его и так писать и так писать что это даст пока непонятно
url = 'https://stepik.org/course/104774'
browser = webdriver.Chrome()
browser.get(url)
time.sleep(5)