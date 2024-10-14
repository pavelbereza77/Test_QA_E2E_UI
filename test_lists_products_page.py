import time

from pages.login_page import LoginPage
from pages.list_products_page import Lists_ProductPage


def test_products_page(browser):
    link = 'https://www.saucedemo.com/'
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.input_user_name()
    page.input_password()
    page.goo_too_page_product()
    list_product_page = Lists_ProductPage(browser=browser, url=browser.current_url)
    list_product_page.should_list_products_page()
    list_product_page.click_link_product_test()
    time.sleep(16)
