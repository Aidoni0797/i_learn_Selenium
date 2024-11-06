# aiDoni не понимает она скопировала тупо 
from selenium import webdriver
from selenium.webdriver.common.by import By

# скрытый режим
# options_chrome = webdriver.ChromeOptions()
# options_chrome.add_argument('--headless=new')
#with webdriver.Chrome(options=options_chrome) as browser:
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    lst = []
    for x in cookies:
        if int(x.get('name')[14:]) % 2 == 0:
            lst.append(int(x.get('value')))
    print(sum(lst))