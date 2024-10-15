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
    PAGE_FORM = (By.CSS_SELECTOR, '.inventory_details_container')
    BUTTON_ADD_PRODUCT_IN_CART = (By.CSS_SELECTOR, '#add-to-cart')
    NAME_PRODUCT = (By.CLASS_NAME, '.inventory_details_name')


def locator_name_product_link(name_product):
    return (By.XPATH, f"//div[text() ='{name_product}']")


def locator_button_add_basket(name_product):
    return (By.CSS_SELECTOR, f"#add-to-cart-{name_product.lower().replace(' ', '-')}")
