# этот код не работает хотя дано как пример в тексте курса с какой целью предоставлять тому подобные коды вообще непонятно
# оказывается сложно свои мысли перевоплощять в реальность, хех
# выдает 1045 ошибок который вообще непонятно
from selenium import webdriver
from selenium.webdriver.common.by import By

# Инициализация драйвера в блоке with для автоматического закрытия
with webdriver.Chrome() as driver:
    # Открытие веб-страницы
    driver.get("http://some-news-website.com")

    # Ищем все блоки новостей
    news_blocks = driver.find_elements(By.CLASS_NAME, 'news-block')

    # Проходимся по каждому блоку
    for block in news_blocks:
        # В каждом блоке ищем заголовок
        title_element = block.find_element(By.CLASS_NAME, 'title')

        # Допустим, выводим текст каждого заголовка
        print("Заголовок новости:", title_element.text)