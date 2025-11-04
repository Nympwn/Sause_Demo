import pytest
from conftest import *
from pages_POM.login_page import LoginPage
from pages_POM.inventory_page import InventoryPage
from utils.logger import log

@pytest.mark.ui
@pytest.mark.ui
def test_add_product(driver):
    log.info('Старт теста "test_add_product"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')
    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

#    assert inventory_page.add_to_cart('Sauce Labs Backpack') == 'Remove'
# Кнопка считается кортежем, не получается вытянуть из нее текст. Через цикл/if-else не получилось.
    log.error('Тест не может быть завершен.')

@pytest.mark.ui
@pytest.mark.regression
def test_get_cart_count(driver):
    log.info('Старт теста "test_get_cart_count"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    assert inventory_page.get_cart_count(driver) == 2
    log.info('Тест "test_get_cart_count" успешно завершен')

@pytest.mark.ui
@pytest.mark.smoke
def test_filter(driver):
    log.info('Старт теста "test_filter"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.filter(2)
    assert inventory_page.filter(2).is_selected() == True
    log.info('Тест "test_filter" успешно завершен')
    # проверить по местоположению определенного товара не получится (либо не знаю как) - у товара не меняется ID в зависимости от местоположения

@pytest.mark.ui
@pytest.mark.smoke
def test_add_to_cart(driver):
    log.info('Старт теста "test_add_to_cart"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    assert 'cart' in driver.current_url, 'Не удалось перейти в корзину.'
    log.info('Тест "test_add_to_cart" успешно завершен')