import pytest

from selenium.common import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasketLocators


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False

        return True

    def should_cart_link(self):
        assert self.is_element_present(*BasketLocators.LINK_CART), 'Not link cart'

    def click_link_cart(self):
        self.browser.find_element(*BasketLocators.LINK_CART).click()

    def get_list_product_in_cart(self):
        return [product.text for product in self.browser.find_elements(*BasketLocators.ITEM_CART)]