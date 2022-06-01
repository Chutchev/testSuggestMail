import os
import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from steps.BaseSteps import BaseSteps
from utils.helpers import get_page


def test_translit(driver: WebDriver):
    server = os.environ.get("SERVER")
    driver.get(server)
    page = get_page(driver)()
    # 1. Нашли поле Поиска
    BaseSteps.find(driver, page, "поле", "Поле поиска")
    # 2. Нашли кнопку Найти
    BaseSteps.find(driver, page, "кнопка", "Найти")
    # 3. В поле поиска написали с недостающей буквами
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", "ghbdtn")
    # 4. Нашли все подсказки и сохранили их.
    time.sleep(1)
    translit_symbols_elements = BaseSteps.find(driver, page, "опция", "")
    translit_symbols_text = [element.text for element in translit_symbols_elements if "привет" in element.text]
    assert len(translit_symbols_text) == len(translit_symbols_elements), "Ошибка транслита. Считает по разному"