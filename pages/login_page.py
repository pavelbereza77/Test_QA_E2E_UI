from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
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

    def input_user_name(self, username):
        self.browser.find_element(*LoginPageLocators.USERNAME_INPUT).send_keys(username)
        input_username = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT).text
        assert input_username == username, 'The user name entered does not match the one displayed'

    def input_password(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        input_password = self.browser.find_element(*LoginPageLocators.USERNAME_INPUT).text
        assert input_password == password, 'The password entered does not match the one displayed'