from pages.base_page import BasePage
from pages.locators import SalePageLocators


class SalePage(BasePage):
    def should_sale_form(self):
        self.should_present_form_sale_page()
        self.should_present_sale_first_name()
        self.should_present_sale_last_name()
        self.should_present_sale_postal_code()
        self.should_present_sale_button_cancel()
        self.should_present_sale_button_continue()

    def should_present_form_sale_page(self):
        assert self.is_element_present(*SalePageLocators.SALE_FORM), 'Not form sale'

    def should_present_sale_first_name(self):
        assert self.is_element_present(*SalePageLocators.SALE_FIELD_FIRST_NAME), 'Not in sale page first_name'

    def should_present_sale_last_name(self):
        assert self.is_element_present(*SalePageLocators.SALE_FIELD_LAST_NAME), 'Not in sale page last_name'

    def should_present_sale_postal_code(self):
        assert self.is_element_present(*SalePageLocators.SALE_FIELD_POSTAL_CODE), 'Not in sale page postal_cod'

    def should_present_sale_button_cancel(self):
        assert self.is_element_present(*SalePageLocators.BUTTON_CANCEL), 'Not in sale page button_cancel'

    def should_present_sale_button_continue(self):
        assert self.is_element_present(*SalePageLocators.BUTTON_CONTINUE), 'Not in sale page button_continue'

    def input_sale_form(self):
        self.browser.find_element(*SalePageLocators.SALE_FIELD_FIRST_NAME).send_keys('test')
        self.browser.find_element(*SalePageLocators.SALE_FIELD_LAST_NAME).send_keys('test')
        self.browser.find_element(*SalePageLocators.SALE_FIELD_POSTAL_CODE).send_keys('12345678')

    def click_button_continue(self):
        self.browser.find_element(*SalePageLocators.BUTTON_CONTINUE).click()
