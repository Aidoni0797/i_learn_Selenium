# прикольно когда ползунок без твоего прикосновения двигаетс
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/selenium/5.10/5/index.html"

with webdriver.Chrome() as driver:
    driver.get(url)
    slider = driver.find_element(By.ID, "volume")
    time.sleep(3)

    ActionChains(driver).click_and_hold(slider).move_by_offset(50, 0).release().perform()

    time.sleep(10)