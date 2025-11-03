import pytest
from conftest import *
from pages_POM.login_page import LoginPage
from pages_POM.inventory_page import InventoryPage

def test_add_product(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

def test_get_cart_count(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    assert inventory_page.get_cart_count(driver) == 2

def test_filter(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.filter(2)
    assert inventory_page.filter(2).is_selected() == True
    # проверить по местоположению определенного товара не получится (либо не знаю как) - у товара не меняется ID в зависимости от местоположения

def test_add_to_cart(driver):

    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    assert 'cart' in driver.current_url, 'Не удалось перейти в корзину.'