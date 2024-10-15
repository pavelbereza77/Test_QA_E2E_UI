import time

from pages.login_page import LoginPage
from pages.list_products_page import ListsProductPage


def test_products_page(browser):
    link = 'https://www.saucedemo.com/'
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.input_user_name()
    page.input_password()
    page.goo_too_page_product()
    list_product_page = ListsProductPage(browser=browser, url=browser.current_url)
    list_product_page.should_list_products_page()
    list_product_page.click_button_add_cart()

    list_product_page.click_link_cart()
    list_product_page.present_product_in_cart()
    time.sleep(5)
