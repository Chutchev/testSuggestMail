import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.Constant import TIME

class BaseSteps:

    @classmethod
    def find(cls, driver, page, element_type, element_name, check="статус", value="присутствует"):
        actions = {
            "статус": {
                "присутствует": EC.presence_of_all_elements_located,
                "отсутствует": EC.presence_of_all_elements_located
            },
        }
        if value == "отсутствует":
            elements = driver.find_elements(By.XPATH, page.locators[element_type][element_name])
        else:
            elements = WebDriverWait(driver, TIME).until(actions[check].get(value, actions[check])
                                                     ((By.XPATH, page.locators[element_type][element_name])))
        return elements

    @classmethod
    def click(cls, driver, page, element_type, element_name):
        index = 0
        if element_name == "любая":
            elements = cls.find(driver, page, element_type, "")
            index = random.randint(0, len(elements))
        else:
            elements = cls.find(driver, page, element_type, element_name)
        elements[index].click()

    @classmethod
    def send_keys(cls, driver, page, element_type, element_name, text):
        elements = cls.find(driver, page, element_type, element_name)
        elements[0].clear()
        elements[0].send_keys(text)

