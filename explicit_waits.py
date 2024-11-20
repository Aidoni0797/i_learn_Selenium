# надо ждать и непонятно когда появиьтся, все просто прекрасно, надо просто ждать
# скорее всего aiDoni ты всю жизнь будешь учить этот мир программирование
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# Импортировал модуль expected_conditions из библиотеки webdriver и назвал его EC, чтобы не писать каждый раз его длинное название.
from selenium.webdriver.support import expected_conditions as EC
# Импортировал сам класс для работы с ожиданиями WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/expectations/1/index.html')
    # Использовал функцию EC.element_to_be_clickable, которая ожидает пока элемент станет кликабельным;
    element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "btn"))).click()
    time.sleep(3)
    print(browser.find_element(By.ID, 'result').text)

# Не спеша и в подробностях, aiDoni учи
# WebDriverWait — это класс из библиотеки Selenium, который используется для реализации явных ожиданий.
# В данном случае, мы создаем объект WebDriverWait, передавая ему два аргумента
# browser: это экземпляр драйвера браузера, с которым мы работаем (в нашем случае, это Chrome).
# 10: это максимальное количество времени (в секундах), в течение которого WebDriverWait будет пытаться выполнить условие, указанное в методе until.
# .until(...)​​ — Этот метод указывает, какое условие мы ожидаем выполнить.

# EC (или expected_conditions) — это модуль в Selenium, который содержит набор предустановленных условий,
# которые можно использовать с WebDriverWait(далее подробно про EC).

# element_to_be_clickable() — это одно из этих условий. Оно проверяет, что элемент не только присутствует на странице,
# но и видим, а также активен, так что по нему можно кликнуть (далее подробно про все функции).

# (By.ID, "btn") — это способ указать, какой именно элемент мы ищем.
# В данном случае, мы ищем элемент по его идентификатору (ID), который равен "btn".
