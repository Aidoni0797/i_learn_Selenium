import time
from selenium import webdriver

# Задаем опции для Chrome
options_chrome = webdriver.ChromeOptions()
# Указываем путь к профилю пользователя

# показывает ошибку пришлось закоментировать и запустить вроде запустился, но почему при указании пути не работет фиг знает
# options_chrome.add_argument("user-data-dir='C:\Users\user\AppData\Local\Google\Chrome\User Data'")
#
# Инициализируем драйвер с указанными опциями
with webdriver.Chrome(options=options_chrome) as browser:
    url = 'https://yandex.ru/'
    browser.get(url)  # Открываем страницу
    time.sleep(10)  # Даем время на загрузку страницы