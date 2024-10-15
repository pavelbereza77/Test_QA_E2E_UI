from pages.base_page import BasePage
from pages.locators import (ListProductPageLocators,
                            ProductPageLocators,
                            locator_button_add_basket,
                            locator_name_product_link)


class ListsProductPage(BasePage):
    # PRODUCT_NAME_LOCATOR = 'Sauce Labs Backpack'

    def should_list_products_page(self):
        self.should_present_form_list_products_page()
        self.should_present_list_products()
        self.should_present_button_product_add_to_basket()

    def should_present_form_list_products_page(self):
        assert self.is_element_present(*ListProductPageLocators.PRODUCT_FORM_PAGE), 'Not form page product'

    def should_present_list_products(self):
        sale_list_product = [product.text for product in
                             self.browser.find_elements(*ListProductPageLocators.LIST_PRODUCT_IN_PAGE)]
        assert ProductPageLocators.PRODUCT_NAME_LOCATOR in sale_list_product, f'Not {ProductPageLocators.PRODUCT_NAME_LOCATOR} in list sale products'

    def should_present_button_product_add_to_basket(self):
        assert self.is_element_present(*locator_button_add_basket(
            name_product=ProductPageLocators.PRODUCT_NAME_LOCATOR)), f'Not button add cart for {ProductPageLocators.PRODUCT_NAME_LOCATOR}'

    def click_button_add_cart(self):
        self.browser.find_element(*locator_button_add_basket(ProductPageLocators.PRODUCT_NAME_LOCATOR)).click()

    def click_link_product_test(self):
        self.browser.find_element(*locator_name_product_link(ProductPageLocators.PRODUCT_NAME_LOCATOR)).click()

    def present_product_in_cart(self):
        list_product_in_cart = self.get_list_product_in_cart()
        assert ProductPageLocators.PRODUCT_NAME_LOCATOR in list_product_in_cart, \
            f'Not {ProductPageLocators.PRODUCT_NAME_LOCATOR} in basket'
