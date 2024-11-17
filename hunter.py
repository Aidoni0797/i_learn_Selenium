# хех, chatgpt ты крутой все таки
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Инициализация драйвера
driver = webdriver.Chrome()

# Открытие исходной страницы
driver.get("https://parsinger.ru/blank/3/index.html")  # Замените на ваш URL

# Список для хранения найденных чисел
numbers = []

# Поиск всех 10 кнопок (предполагается, что у них есть общий класс или ID)
buttons = driver.find_elements(By.CLASS_NAME, "buttons")  # Замените на правильный класс кнопок
ss = 0
# Перебор кнопок
for button in buttons:
    # Кликаем по кнопке
    button.click()

    # Переходим в новую вкладку
    driver.switch_to.window(driver.window_handles[-1])

    # Ждем, чтобы страница успела загрузиться
    time.sleep(1)

    # Ищем число в title страницы
    title = driver.title
    ss += int(title)

    number = ''.join(filter(str.isdigit, title))  # Извлекаем число из title

    if number:
        numbers.append(int(number))  # Добавляем число в список

    # Закрываем вкладку
    driver.close()

    # Переходим обратно на исходную вкладку
    driver.switch_to.window(driver.window_handles[0])

# Суммируем все найденные числа
total_sum = sum(numbers)



# Закрываем браузер
driver.quit()

# Выводим результат
print(f"Итоговая сумма: {total_sum}")
