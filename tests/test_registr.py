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
    # 3. В поле поиска написали маленькими буквами
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", "привет")
    # 4. Нашли все подсказки и сохранили их.
    lower_symbols_elements = BaseSteps.find(driver, page, "опция", "")
    lower_symbols_text = [element.text for element in lower_symbols_elements]
    # 5. В поле поиска написали БОЛЬШИМИ буквами
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", "ПРИВЕТ")
    # 6. Нашли все подсказки и сохранили их.
    time.sleep(1)
    upper_symbols_elements = BaseSteps.find(driver, page, "опция", "")
    upper_symbols_text = [element.text for element in upper_symbols_elements]
    # 5. В поле поиска написали раЗныМи буквами
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", "ПрИвеТ")
    # 6. Нашли все подсказки и сохранили их.
    time.sleep(1)
    lower_upper_symbols_elements = BaseSteps.find(driver, page, "опция", "")
    lower_upper_symbols_text = [element.text for element in lower_upper_symbols_elements]
    assert lower_symbols_text == upper_symbols_text == lower_upper_symbols_text, f"Ошибка регистров. Должно быть регистронезависимое поле!"
