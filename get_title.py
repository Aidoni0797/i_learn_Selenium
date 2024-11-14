from selenium import webdriver
with webdriver.Chrome() as browser:
    browser.get("https://stepik.org/course/104774/promo")
    print(browser.execute_script("return document.title;"))