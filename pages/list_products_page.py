from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class Lists_ProductPage(BasePage):
    def should_list_products_page(self):
        self.should_present_form_list_products_page()
        self.should_present_list_products()
        self.should_present_button_product_add_to_basket()

    def should_present_form_list_products_page(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_FORM_PAGE), 'Not form page product'

    def should_present_list_products(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_LOCATOR_LINK), f'Not {ProductPageLocators.PRODUCT_NAME_LOCATOR}'

    def should_present_button_product_add_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.BUTTON_ADD_BASKET), f'Not button add cart for {ProductPageLocators.PRODUCT_NAME_LOCATOR}'

    def click_link_product_test(self):
        self.browser.find_element(*ProductPageLocators.PRODUCT_LOCATOR_LINK).click()
