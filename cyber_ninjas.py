import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

url = 'https://parsinger.ru/selenium/5.7/4/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    action = ActionChains(browser)

    while True:
        last_child = browser.find_element(By.CSS_SELECTOR, '#main_container div:last-child')
        action.move_to_element(last_child).scroll_by_amount(0, 5000).perform()
        div_elements = browser.find_elements(By.CLASS_NAME, 'child_container')
        if len(div_elements) == 100:
            break

    for div in div_elements:
        inp_elements = div.find_elements(By.TAG_NAME, 'input')
        action.move_to_element(div).perform()
        for inp in inp_elements:
            if int(inp.get_attribute('value')) % 2 == 0:
                inp.click()

    time.sleep(1)
    browser.find_element(By.CLASS_NAME, 'alert_button').click()
    alert_text = browser.switch_to.alert.text
print(alert_text)
