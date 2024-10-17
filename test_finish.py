import time

from pages.basket_page import BasketPage
from pages.finish_page import FinishPage
from pages.overview_page import OverviewPage
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
    time.sleep(2)
    list_product_page = ListsProductPage(browser=browser, url=browser.current_url)
    list_product_page.click_link_product_test()
    time.sleep(2)
    product_page = ProductPage(browser=browser, url=browser.current_url)
    product_page.click_button_add_cart_in_product_page()
    product_page.click_link_cart()
    time.sleep(2)
    basket_page = BasketPage(browser=browser, url=browser.current_url)
    basket_page.click_checkout()
    time.sleep(2)
    sale_page = SalePage(browser=browser, url=browser.current_url)
    sale_page.input_sale_form()
    sale_page.click_button_continue()
    time.sleep(2)
    overview_page = OverviewPage(browser=browser, url=browser.current_url)
    overview_page.click_button_finish()
    time.sleep(2)
    finish_page = FinishPage(browser=browser, url=browser.current_url)
    finish_page.should_finish_page()

    time.sleep(10)
