from pages.base_page import BasePage
from pages.locators import OverviewPageLocators, ProductPageLocators


class OverviewPage(BasePage):
    def should_form_finish_page(self):
        self.should_present_form_page()
        self.should_present_sale_product()
        self.should_sum_price_total_and_total_price()
        self.should_button_cancel_in_finish_page()
        self.should_button_finish_in_finish_page()

    def should_present_form_page(self):
        assert self.is_element_present(*OverviewPageLocators.OVERVIEW_FORM)

    def should_present_sale_product(self):
        sale_products = self.get_sale_products()
        assert ProductPageLocators.PRODUCT_NAME_LOCATOR in sale_products, \
            f'Not {ProductPageLocators.PRODUCT_NAME_LOCATOR} in sale products'

    def should_sum_price_total_and_total_price(self):
        sum_price_sale_product = self.get_total_sum_sale()
        total_sum = self.browser.find_element(*OverviewPageLocators.TOTAL_ORDER).text.split('$')[1]
        total_price = self.browser.find_element(*OverviewPageLocators.TOTAL_PRICE).text.split('$')[1]
        tax = self.browser.find_element(*OverviewPageLocators.TAX).text.split('$')[1]

        assert sum_price_sale_product == float(total_price), \
            'The amount of goods sold does not match the information in Price Total'
        assert (sum_price_sale_product + float(tax)) == float(total_sum), \
            'The cost of goods sold, including tax, does not correspond to the information in Total:'

    def should_button_cancel_in_finish_page(self):
        assert self.is_element_present(*OverviewPageLocators.BUTTON_CANCEL_OVERVIEW_PAGE), \
            'Not button cancel in finish page'

    def should_button_finish_in_finish_page(self):
        assert self.is_element_present(*OverviewPageLocators.BUTTON_FINISH_PAGE), \
            'Not button finish in finish page'

    def click_button_finish(self):
        self.browser.find_element(*OverviewPageLocators.BUTTON_FINISH_PAGE).click()
