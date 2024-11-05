# from selenium import webdriver
#
# with webdriver.Chrome() as webdriver:
#     webdriver.get('https://stepik.org/lesson/732061/step/1?unit=733594')
#     cookies = webdriver.get_cookies()
#     for cookie in cookies:
#         print(cookie['name']) имя печатает

from selenium import webdriver

with webdriver.Chrome() as webdriver:
    webdriver.get('https://stepik.org/lesson/732061/step/1?unit=733594')
    # Если вы посмотрите на первый пример с кодом, вы увидите, что в cookie хранится время экспирации 'expiry': 1685518907 т.е.,
    # время истечения срока жизни cookie.
    print(webdriver.get_cookie('_ym_uid')['expiry'])