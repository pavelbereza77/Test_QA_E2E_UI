import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
try:
    driver.get("https://www.saucedemo.com/")
    assert "Swag" in driver.title
except Exception:
    print('Connect error')

input_login = driver.find_element(By.ID, "user-name")
input_password = driver.find_element(By.ID, "password")
login_clik = driver.find_element(By.ID, "login-button")

time.sleep(1)
input_login.clear()
input_login.send_keys("standard_user")

input_password.clear()
input_password.send_keys("secret_sauce")
login_clik.send_keys(Keys.RETURN)

products_page = driver.find_element(By.CLASS_NAME, 'header_secondary_container')
if products_page.text.split()[0] == 'Products':
    print("Мы попали на главную страницу")

time.sleep(2)
product = driver.find_element(By.CLASS_NAME, 'inventory_item_name')
if product.text == 'Sauce Labs Backpack':
    print('Продукт выбран')

add_cart_product = driver.find_element(By.ID, 'add-to-cart-sauce-labs-backpack')
add_cart_product.send_keys(Keys.RETURN)

shopping_cart = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
shopping_cart.click()
print("Открыли корзину")

time.sleep(2)
to_cart = driver.find_element(By.CLASS_NAME, 'header_secondary_container')
if 'Your Cart' in to_cart.text.split():
    print("Мы на странице корзины")

product_to_cart = driver.find_element(By.ID, 'item_4_title_link')
if product_to_cart.text == 'Sauce Labs Backpack':
    print('Продукт в корзине')

order_button = driver.find_element(By.ID, 'checkout')
order_button.send_keys(Keys.RETURN)
to_order = driver.find_element(By.CLASS_NAME, 'header_secondary_container')
if 'Checkout: Your Information' in to_order.text:
    print("Мы на странице оформления заказа")

time.sleep(2)
user_first_name = driver.find_element(By.ID, 'first-name')
user_last_name = driver.find_element(By.ID, 'last-name')
user_postal_code = driver.find_element(By.ID, 'postal-code')

user_first_name.send_keys('user_first_name')
user_last_name.send_keys('user_last_name')
user_postal_code.send_keys('123456789')
print('Реквизиты покупателя заполнены')

sale_product = driver.find_element(By.ID, 'continue')
sale_product.send_keys(Keys.RETURN)

sale_product_page = driver.find_element(By.CLASS_NAME, 'header_secondary_container')
print(sale_product_page.text)
if 'Checkout: Overview' in sale_product_page.text:
    print("Мы попали на страницу оплаты")

time.sleep(2)
finish_button = driver.find_element(By.ID, 'finish')
finish_button.send_keys(Keys.RETURN)

finish_page = driver.find_element(By.CLASS_NAME, 'header_secondary_container')
if 'Checkout: Complete!' in finish_page.text:
    print("Тест завершен!")

time.sleep(2)
