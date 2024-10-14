from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_button_container')
    USERNAME_INPUT = (By.CSS_SELECTOR, ".form_input[placeholder='Username']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".form_input[placeholder='Password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#login-button")
