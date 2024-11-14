from selenium import webdriver

with webdriver.Chrome() as browser:
    # Открываем указанный URL в браузере.
    browser.get('http://parsinger.ru/window_size/1/')

    # Устанавливаем размер окна браузера на 1200 пикселей в ширину и 720 пикселей в высоту.
    browser.set_window_size(1200, 720)

    # Получаем текущий размер окна браузера в виде словаря, где 'height' - высота окна,
    # 'width' - ширина окна. И затем печатаем значение высоты окна.
    print(browser.get_window_size().get('height'))

    # Аналогично печатаем значение ширины окна.
    print(browser.get_window_size().get('width'))

# После завершения выполнения кода в блоке 'with', браузер автоматически закрывается.