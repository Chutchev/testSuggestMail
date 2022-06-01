import os

from selenium.webdriver.chrome.webdriver import WebDriver
from steps.BaseSteps import BaseSteps
from utils.helpers import get_page


def test_random_suggest_click(driver: WebDriver):
    server = os.environ.get("SERVER", "https://go.mail.ru/")
    driver.get(server)
    page = get_page(driver)()
    # 1. Нашли поле Поиска
    BaseSteps.find(driver, page, "поле", "Поле поиска")
    # 2. Нашли кнопку Найти
    BaseSteps.find(driver, page, "кнопка", "Найти")
    # 3. Нажали на поле Поиска
    BaseSteps.click(driver, page, "поле", "Поле поиска")
    # 4. Проверили количество подсказок
    elements = BaseSteps.find(driver, page, "опция", "")
    assert len(elements) == 10, f"Количество подсказок {len(elements)} != 10"
