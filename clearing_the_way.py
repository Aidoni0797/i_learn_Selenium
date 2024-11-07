from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()
driver.get("https://parsinger.ru/scroll/4/index.html")  # Замените на URL вашей основной страницы

# Найдите все кнопки на странице и инициализируйте переменную для суммы
buttons = driver.find_elements(By.CLASS_NAME, 'btn')  # Предположим, что у кнопок класс 'btn'
total_sum = 0

# Цикл по всем кнопкам для клика и получения результата
for button in buttons:
    # Прокрутка к элементу, чтобы он был виден
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    # Клик по кнопке
    button.click()

    # Ожидание появления результата
    result_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "result"))
    )

    # Получение текста из тега <p id="result"> и преобразование его в число
    result = int(result_element.text)
    total_sum += result  # Добавление к общей сумме

    print(total_sum)

# Закрытие драйвера
driver.quit()
