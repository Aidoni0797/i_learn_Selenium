# круто когда создаешь код понимая а не тупо, учи aiDoni учи
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/expectations/3/index.html')
    click_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    element = WebDriverWait(browser, 20).until(EC.title_contains('345FDG3245SFD'))
    print(browser.find_element(By.ID, 'result').text)
