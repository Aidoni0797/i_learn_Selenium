# ActionChains — класс, предназначенный для автоматизации сложных последовательностей действий пользователя.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Инициализация драйвера
driver = webdriver.Chrome()

# Открыть веб-страницу (замените URL на ваш адрес)
driver.get("https://parsinger.ru/selenium/5.7/2/index.html")

# Найти элемент на странице с использованием локатора By
draggable = driver.find_element(By.ID, "draggable")

# Использование ActionChains для выполнения перетаскивания элемента
actions = ActionChains(driver)

# 1. Переместить блок влево на 100px
actions.drag_and_drop_by_offset(draggable, -100, 0).perform()

# 2. Переместить блок вниз на 100px
actions.drag_and_drop_by_offset(draggable, 0, 100).perform()

# 3. Переместить блок вправо на 100px
actions.drag_and_drop_by_offset(draggable, 100, 0).perform()

# 4. Переместить блок вверх на 100px
actions.drag_and_drop_by_offset(draggable, 0, -100).perform()

# Закрыть браузер после завершения
driver.quit()