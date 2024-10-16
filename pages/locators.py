from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_button_container')
    USERNAME_INPUT = (By.CSS_SELECTOR, ".form_input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".form_input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")


class ListProductPageLocators():
    PRODUCT_FORM_PAGE = (By.CSS_SELECTOR, "#page_wrapper")
    LIST_PRODUCT_IN_PAGE = (By.CSS_SELECTOR, '.inventory_item_name')


class BasketLocators():
    ITEM_CART = (By.CSS_SELECTOR, ".cart_item a")
    LINK_CART = (By.CSS_SELECTOR, '.shopping_cart_link')


class ProductPageLocators():
    PRODUCT_NAME_LOCATOR = 'Sauce Labs Backpack'
    PAGE_FORM = (By.CSS_SELECTOR, '.inventory_details_container')
    BUTTON_ADD_PRODUCT_IN_CART = (By.CSS_SELECTOR, '#add-to-cart')
    BUTTON_BACK_PRODUCTS = (By.CSS_SELECTOR, '#back-to-products')


class BasketPageLocators():
    CART_FORM = (By.CSS_SELECTOR, '#cart_contents_container')
    BUTTON_CONTINUE_SHOPPING = (By.CSS_SELECTOR, '#continue-shopping')
    BUTTON_CHECKOUT = (By.CSS_SELECTOR, '#checkout')


class SalePageLocators():
    SALE_FORM = (By.CSS_SELECTOR, '#checkout_info_container')
    BUTTON_CANCEL = (By.CSS_SELECTOR, '#cancel')
    BUTTON_CONTINUE = (By.CSS_SELECTOR, '#continue')
    SALE_FIELD_FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    SALE_FIELD_LAST_NAME = (By.CSS_SELECTOR, '#last-name')
    SALE_FIELD_POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')


class OverviewPageLocators():
    OVERVIEW_FORM = (By.CSS_SELECTOR, '#checkout_summary_container')
    PRODUCT_IN_OVERVIEW_FORM = (By.CSS_SELECTOR, '.inventory_item_name')
    PRICE_PRODUCT = (By.CSS_SELECTOR, '.inventory_item_price')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.summary_subtotal_label')
    TAX = (By.CSS_SELECTOR, '.summary_tax_label')
    TOTAL_ORDER = (By.CSS_SELECTOR, '.summary_total_label')
    BUTTON_CANCEL_OVERVIEW_PAGE = (By.CSS_SELECTOR, '#cancel')
    BUTTON_FINISH_PAGE = (By.CSS_SELECTOR, '#finish')


def locator_name_product_link():
    name_product = ProductPageLocators.PRODUCT_NAME_LOCATOR
    return (By.XPATH, f"//div[text() ='{name_product}']")


def locator_button_add_basket():
    name_product = ProductPageLocators.PRODUCT_NAME_LOCATOR
    return (By.CSS_SELECTOR, f"#add-to-cart-{name_product.lower().replace(' ', '-')}")
