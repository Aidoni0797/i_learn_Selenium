from selenium import webdriver

with webdriver.Chrome() as browser:
    # Загрузка указанного URL ('http://parsinger.ru/window_size/1/') в открытом окне браузера.
    browser.get('http://parsinger.ru/window_size/1/')

    # Установка размера окна браузера: ширина — 1200 пикселей и высота — 720 пикселей.
    browser.set_window_size(1200, 720)

    # Получение текущего размера окна браузера и вывод его ширины на экран.
    # Обращаемся к ключу "width" в полученном словаре.
    print(browser.get_window_size()["width"])

    # Получение текущего размера окна браузера и вывод его высоты на экран.
    # Обращаемся к ключу "height" в полученном словаре.
    print(browser.get_window_size()["height"])