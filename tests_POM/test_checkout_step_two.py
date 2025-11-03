import pytest
from pages_POM.login_page import LoginPage
from pages_POM.inventory_page import InventoryPage
from pages_POM.cart_page import CartPage
from pages_POM.checkout_step_one_page import CheckoutStepOnePage
from pages_POM.checkout_step_two_page import CheckoutStepTwoPage
from conftest import *

def test_checking_item(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    assert checkout_step_two_page.checking_item('5') == 'Sauce Labs Fleece Jacket'
    assert checkout_step_two_page.checking_item('4') == 'Sauce Labs Backpack'

def test_checking_value(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    assert checkout_step_two_page.checking_payment__shipping_and_price('2') == 'SauceCard #31337'
    assert checkout_step_two_page.checking_payment__shipping_and_price('4') == 'Free Pony Express Delivery!'
    assert checkout_step_two_page.checking_payment__shipping_and_price('6') == 'Item total: $79.98'
    assert checkout_step_two_page.checking_payment__shipping_and_price('7') == 'Tax: $6.40'
    assert checkout_step_two_page.checking_payment__shipping_and_price('8') == 'Total: $86.38'

def test_back_to_inventory(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    checkout_step_two_page.back_to_inventory()

    assert 'inventory' in driver.current_url, 'Кнопка возвращения не найдена.'


def test_go_to_finish(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    checkout_step_two_page.go_to_finish()

    assert 'checkout-complete' in driver.current_url, 'Не удалось сформировать заказ'


