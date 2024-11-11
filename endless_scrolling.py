# 5 скроллов одновременно это уже что то надо было подумать но нормально нормально для прогресса aiDoni
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/infiniti_scroll_3/')
    number_search = []

    div1 = browser.find_element(By.XPATH, '//*[@id="scroll-container_1"]/div')
    div2 = browser.find_element(By.XPATH, '//*[@id="scroll-container_2"]/div')
    div3 = browser.find_element(By.XPATH, '//*[@id="scroll-container_3"]/div')
    div4 = browser.find_element(By.XPATH, '//*[@id="scroll-container_4"]/div')
    div5 = browser.find_element(By.XPATH, '//*[@id="scroll-container_5"]/div')
    for x in range(10):
        ActionChains(browser).move_to_element(div1).scroll_by_amount(1, 500).perform()
        ActionChains(browser).move_to_element(div2).scroll_by_amount(1, 500).perform()
        ActionChains(browser).move_to_element(div3).scroll_by_amount(1, 500).perform()
        ActionChains(browser).move_to_element(div4).scroll_by_amount(1, 500).perform()
        ActionChains(browser).move_to_element(div5).scroll_by_amount(1, 500).perform()



    numbers_find = [x for x in browser.find_elements(By.TAG_NAME, 'span')]
    for number_find in numbers_find:
        number_search.append(number_find.text)

    # хардкод - но нормально или плохо общм что получилось
    total = 0
    for i in range(len(number_search)):
        if number_search[i] != '':
            total += int(number_search[i])
    print(total)