from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_form(self):
        self.should_cart_form()
        self.should_button_continue_shopping()
        self.should_button_checkout()

    def should_cart_form(self):
        assert self.is_element_present(*BasketPageLocators.CART_FORM), 'Not basket form'

    def should_button_continue_shopping(self):
        assert self.is_element_present(*BasketPageLocators.BUTTON_CONTINUE_SHOPPING), 'Not button continue shopping'

    def should_button_checkout(self):
        assert self.is_element_present(*BasketPageLocators.BUTTON_CHECKOUT), 'Not button checkout'

    def click_checkout(self):
        self.browser.find_element(*BasketPageLocators.BUTTON_CHECKOUT).click()
