# очень похож на предыдущий надо просто логику включить и местами поменять элементы
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for x in range(10):
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()

    number_search = []

    numbers_find = [x for x in browser.find_elements(By.TAG_NAME, 'p')]
    for number_find in numbers_find:
        number_search.append(number_find.text)

    # хардкод - но нормально или плохо общм что получилось
    total = 0
    for i in range(len(number_search)):
        if number_search[i] != '':
            total += int(number_search[i])
    print(total)