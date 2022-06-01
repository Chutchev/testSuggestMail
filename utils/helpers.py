from selenium.webdriver.chrome.webdriver import WebDriver

from core.BasePage import BasePage
from locators.GoMailPage import GoMailPage


def get_page(driver: WebDriver):
    links = {
        "https://go.mail.ru/": GoMailPage
    }
    url = driver.current_url
    return links.get(url, None)
