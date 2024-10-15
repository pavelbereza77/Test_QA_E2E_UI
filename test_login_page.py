import time

from pages.login_page import LoginPage


def test_login_page(browser):
    link = 'https://www.saucedemo.com/'
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.should_login_form()
    page.input_user_name()
    page.verification_of_correct_input_username()
    page.input_password()
    page.verification_of_correct_input_password()
    page.goo_too_page_product()
    time.sleep(5)