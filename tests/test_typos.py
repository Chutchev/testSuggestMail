import os
import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from steps.BaseSteps import BaseSteps
from utils.helpers import get_page


def test_registr(driver: WebDriver):
    server = os.environ.get("SERVER")
    driver.get(server)
    page = get_page(driver)()
    # 1. Нашли поле Поиска
    BaseSteps.find(driver, page, "поле", "Поле поиска")
    # 2. Нашли кнопку Найти
    BaseSteps.find(driver, page, "кнопка", "Найти")
    # 3. В поле поиска написали с недостающей буквами
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", "пивет")
    # 4. Нашли все подсказки и сохранили их.
    time.sleep(1)
    typos_minus_symbols_elements = BaseSteps.find(driver, page, "опция", "")
    typos_minus_symbols_text = [element.text for element in typos_minus_symbols_elements if "привет" in element.text]
    assert len(typos_minus_symbols_text) == len(typos_minus_symbols_elements)
    # 5.
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", "пкивет")
    time.sleep(1)
    typos_not_right_symbols_elements = BaseSteps.find(driver, page, "опция", "")
    typos_not_right_symbols_text = [element.text for element in typos_not_right_symbols_elements if "привет" in element.text]
    assert len(typos_not_right_symbols_text) == len(typos_not_right_symbols_elements), f"Ошибка опечаток. {typos_not_right_symbols_text} != {typos_not_right_symbols_elements}"