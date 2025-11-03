import pytest
from pages_POM.login_page import LoginPage
from pages_POM.inventory_page import InventoryPage
from pages_POM.cart_page import CartPage
from pages_POM.checkout_step_one_page import CheckoutStepOnePage
from conftest import *

def test_filling_data(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    assert 'checkout-step-two' in driver.current_url, 'Не удалось перейти на страницу проверки информации.'

def test_empty_field_zip_code(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '')

    assert 'Postal Code is required' in checkout_step_one_page.get_message_error()

def test_empty_field_last_name(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', '', '123-456')

    assert 'Last Name is required' in checkout_step_one_page.get_message_error()

def test_empty_field_first_name(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('', 'Curter', '123-456')

    assert 'First Name is required' in checkout_step_one_page.get_message_error()

def test_return_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.cancel()

    assert 'cart' in driver.current_url, 'Не удалось вернуться в корзину.'