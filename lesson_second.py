import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.service import Service as ChromiumService
# эти строки кода открывает именно ссылку где расположен курс, прикольно
with webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install())) as driver:
    driver.get("https://stepik.org/course/104774")
    time.sleep(5)

