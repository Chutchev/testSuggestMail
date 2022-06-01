from core.BasePage import BasePage
from exceptions import LocatorNotExists
from locators.locatorConstant import INPUT_FIELD, OPTION, BUTTON


class Button:
    locators = {
        "Найти": "//button[@type='submit']"
    }

    def __getitem__(self, item) -> str:
        if item in self.locators:
            return self.locators[item]
        else:
            raise LocatorNotExists(f"Локатор для кнопки {item} не существует")


class Option:

    def __getitem__(self, item) -> str:
        base_xpath = "//li[contains(@class, 'Suggests')]"
        if item is not None:
            return f"{base_xpath}//span[contains(., '{item}')]"
        return base_xpath


class Input:

    locators = {
        "Поле поиска": "//form//input[@name='q']"
    }

    def __getitem__(self, item) -> str:
        if item in self.locators:
            return self.locators[item]
        else:
            raise LocatorNotExists(f"Локатор для поля {item} не существует")


class GoMailPage(BasePage):
    locators = {
        INPUT_FIELD: Input(),
        OPTION: Option(),
        BUTTON: Button()
    }

    links = ["https://go.mail.ru/"]
