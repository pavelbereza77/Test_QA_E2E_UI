import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class SaucedemoSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_connect_log_product_add_product_cart(self):
        product_test = 'Sauce Labs Backpack'
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        input_login = driver.find_element(By.ID, "user-name")
        input_password = driver.find_element(By.ID, "password")
        login_clik = driver.find_element(By.ID, "login-button")

        input_login.clear()
        input_login.send_keys("standard_user")
        input_password.clear()
        input_password.send_keys("secret_sauce")
        login_clik.send_keys(Keys.RETURN)

        product = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
        self.assertEqual(product.text, product_test)
        product_test_cart = product.text

        add_cart_product = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
        add_cart_product.send_keys(Keys.RETURN)

        shopping_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        shopping_cart.click()

        product_to_cart = driver.find_element(By.ID, 'item_4_title_link')
        self.assertEqual(product_to_cart.text, product_test_cart)

    def tearDown(self):
        self.driver.close()
