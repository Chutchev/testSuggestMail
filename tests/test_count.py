import os
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from steps.BaseSteps import BaseSteps
from utils.helpers import get_page

test_data = [
    {"msg": "Привет", "count": 10},
    {"msg": 123, "count": 10},
    {"msg": "@#!@#!@#&*^!%", "count": 0},
    {"msg": "a" * 1024, "count": 0},
    {"msg": "a", "count": 10},
    {"msg": " ", "count": 0},
]


@pytest.mark.parametrize("test_data", test_data)
def test_count(driver: WebDriver, test_data):
    server = os.environ.get("SERVER")
    driver.get(server)
    page = get_page(driver)()
    # 1. Нашли поле Поиска
    BaseSteps.find(driver, page, "поле", "Поле поиска")
    # 2. Нашли кнопку Найти
    BaseSteps.find(driver, page, "кнопка", "Найти")
    # 3. Нажали на поле Поиска
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", test_data["msg"])
    # 4. Проверили что опций в подсказках ровно {count} штук
    if test_data["count"] != 0:
        elements = BaseSteps.find(driver, page, "опция", "")
    else:
        elements = BaseSteps.find(driver, page, "опция", "", value="отсутствует")
    assert len(elements) == test_data["count"], f"Количество подсказок {len(elements)} != {test_data['count']}"
