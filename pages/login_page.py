from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    def should_login_form(self):
        self.should_present_form_login()
        self.should_user_name()
        self.should_password()
        self.should_button_login()

    def should_present_form_login(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Not form login'

    def should_user_name(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_INPUT), 'Not field input username'

    def should_password(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT), 'Not field input password'

    def should_button_login(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Not button login'

    def input_user_name(self):
        self.browser.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(self.USERNAME)

    def verification_of_correct_input_username(self):
        input_username = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT)
        input_username_value = input_username.get_attribute("value")
        assert input_username_value == self.USERNAME, 'The user name entered does not match the one displayed'

    def input_password(self):
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(self.PASSWORD)

    def verification_of_correct_input_password(self):
        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        input_password_value = input_password.get_attribute("value")
        assert input_password_value == self.PASSWORD, 'The password entered does not match the one displayed'

    def goo_too_page_product(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
