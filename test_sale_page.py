import time

from pages.basket_page import BasketPage
from pages.list_products_page import ListsProductPage
from pages.login_page import LoginPage
from pages.product import ProductPage
from pages.sale_page import SalePage


def test_sale_page(browser):
    link = 'https://www.saucedemo.com/'
    page = LoginPage(browser=browser, url=link)
    page.open()
    page.input_user_name()
    page.input_password()
    page.goo_too_page_product()
    list_product_page = ListsProductPage(browser=browser, url=browser.current_url)
    list_product_page.click_link_product_test()
    product_page = ProductPage(browser=browser, url=browser.current_url)
    product_page.click_button_add_cart_in_product_page()
    product_page.click_link_cart()
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.click_checkout()
    sale_page = SalePage(browser=browser, url=browser.current_url)
    sale_page.should_sale_form()
    sale_page.input_sale_form()
    sale_page.click_button_continue()
    time.sleep(5)
