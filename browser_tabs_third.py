import time
from selenium import webdriver
with webdriver.Chrome() as browser:
    time.sleep(1)
    browser.execute_script('window.open("http://parsinger.ru/blank/0/1.html", "_blank1");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/2.html", "_blank2");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/3.html", "_blank3");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/4.html", "_blank4");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/5.html", "_blank5");')
    browser.execute_script('window.open("http://parsinger.ru/blank/0/6.html", "_blank6");')

    for x in range(len(browser.window_handles)):
        browser.switch_to.window(browser.window_handles[x])
        time.sleep(1)
        print(browser.execute_script("return document.title;"), browser.window_handles[x])