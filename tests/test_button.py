import os
import pytest

from urllib.parse import unquote
from selenium.webdriver.chrome.webdriver import WebDriver
from steps.BaseSteps import BaseSteps
from utils.helpers import get_page

test_data = [
    {"msg": "Привет"},
    ]


@pytest.mark.parametrize("testdata", test_data)
def test_random_suggest_click(driver: WebDriver, testdata):
    server = os.environ.get("SERVER")
    driver.get(server)
    page = get_page(driver)()
    # 1. Нашли поле Поиска
    BaseSteps.find(driver, page, "поле", "Поле поиска")
    # 2. Нашли кнопку Найти
    BaseSteps.find(driver, page, "кнопка", "Найти")
    # 3. В поле поиска ввели текст
    BaseSteps.send_keys(driver, page, "поле", "Поле поиска", testdata["msg"])
    # 4. Нажали на опцию любую
    BaseSteps.click(driver, page, "опция", "любая")
    # 5. Проверили что запрос прошел.
    if testdata["msg"] == "":
        assert driver.current_url == server, "Не соответствие url"
    else:
        assert f'q={testdata["msg"].lower()}' in unquote(driver.current_url).lower(), "Не соответствие url"
