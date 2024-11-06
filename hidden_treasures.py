from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

url = 'https://parsinger.ru/methods/1/index.html'
driver = webdriver.Chrome()

aiDoni = True

while aiDoni:
    driver.get(url)

    equation_element = driver.find_element(By.ID, "result")
    equation_text = equation_element.text

    # замудренно очень пускай остается

    result = equation_text
    if equation_text == 'refresh page':
        driver.refresh()
    else:
        print("Полученный код:", result)
        aiDoni = False

