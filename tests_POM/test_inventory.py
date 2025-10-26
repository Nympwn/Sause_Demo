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

    assert inventory_page.get_cart_count(driver) == 2


    inventory_page.filter().click('Price (low to high)')

    assert inventory_page.filter == 'Price (low to high)'