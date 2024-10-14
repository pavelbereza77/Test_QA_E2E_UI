from pages.login_page import LoginPage


def test_login_page(browser):
    link = 'https://www.saucedemo.com/'
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.should_login_form()
    page.input_user_name('standard_user')
    page.input_password('secret_sauce')