from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_product_page(self):
        self.should_present_form_page()
        self.should_present_button_add_cart()
        self.should_button_back_products()

    def should_present_form_page(self):
        assert self.is_element_present(*ProductPageLocators.PAGE_FORM), 'Not form page'

    def should_present_button_add_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_PRODUCT_IN_CART), 'Not button add cart'

    def should_button_back_products(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_BACK_PRODUCTS)

    def click_button_add_cart_in_product_page(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT_IN_CART).click()

    def present_add_product_in_cart(self):
        product = ProductPageLocators.PRODUCT_NAME_LOCATOR
        products_in_cart = self.get_list_product_in_cart()
        assert product in products_in_cart, f'Not {product} in basket'
