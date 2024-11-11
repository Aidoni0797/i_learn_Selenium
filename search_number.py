# вставляем галочки, хех, интересно, и появляется цифры, прикольно
import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get(r"https://parsinger.ru/scroll/2/index.html")

    list_input = []      # Инициализируем пустой список для хранения обработанных элементов ввода
    while True:          # Начинаем бесконечный цикл

        # Ищем все элементы input на веб-странице и добавляем их в список input_tags
        input_tags = [x for x in browser.find_elements(By.TAG_NAME, 'input')]

        # Обходим каждый элемент input в списке
        for tag_input in input_tags:
            # Проверяем, не обрабатывали ли мы уже этот элемент ранее
            if tag_input not in list_input:
                tag_input.send_keys(Keys.DOWN)     # Отправляем клавишу "Вниз"
                browser.execute_script("return arguments[0].scrollIntoView(true);", tag_input)
                tag_input.click()                  # Кликаем на элемент
                time.sleep(.3)
                list_input.append(tag_input)       # Добавляем элемент в список обработанных элементов

        number_search = []

        numbers_find = [x for x in browser.find_elements(By.TAG_NAME, 'span')]
        for number_find in numbers_find:
            number_search.append(number_find.text)

        # хардкод - но нормально или плохо общм что получилось
        total = 0
        for i in range(len(number_search)):
            if number_search[i] != '':
                total += int(number_search[i])
        print(total)