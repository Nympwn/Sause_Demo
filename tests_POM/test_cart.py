from email.errors import MessageError

import pytest
from pages_POM.login_page import LoginPage
from pages_POM.inventory_page import InventoryPage
from pages_POM.cart_page import CartPage
from conftest import *

def test_checkout_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.checkout_cart('4')
    assert cart_page.checkout_cart('4') == 'Sauce Labs Backpack'

    cart_page.checkout_cart('5')
    assert cart_page.checkout_cart('5') == 'Sauce Labs Fleece Jacket'

def test_checkout_inform_and_back_to_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.checkout_inform('4')
    assert 'inventory-item.html?id=4' in driver.current_url, 'Выбран неверный товар'

    cart_page.back_to_cart()
    assert 'cart' in driver.current_url, 'Не удалось вернуться в корзину'

    cart_page.checkout_inform('5')
    assert 'inventory-item.html?id=5' in driver.current_url, 'Выбран неверный товар'

    cart_page.back_to_cart()
    assert 'cart' in driver.current_url, 'Не удалось вернуться в корзину'

def test_delete_item(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.delete_item('sauce-labs-backpack')
    # не понимаю, как через assert прописать, удален ли товар
    with pytest.raises(MessageError):
        cart_page.delete_item('sauce-labs-backpack')

def test_go_to_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()