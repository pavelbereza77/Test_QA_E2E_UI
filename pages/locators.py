from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_button_container')
    USERNAME_INPUT = (By.CSS_SELECTOR, ".form_input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".form_input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")


class ProductPageLocators():
    PRODUCT_FORM_PAGE = (By.CSS_SELECTOR, "#page_wrapper")
    PRODUCT_NAME_LOCATOR = 'Sauce Labs Backpack'
    PRODUCT_LOCATOR_LINK = (By.XPATH, f"//div[text() ='{PRODUCT_NAME_LOCATOR}']")
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, f"#add-to-cart-{PRODUCT_NAME_LOCATOR.lower().replace(' ', '-')}")
