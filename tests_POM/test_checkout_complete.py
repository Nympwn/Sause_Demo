import pytest
from pages_POM.login_page import LoginPage
from pages_POM.inventory_page import InventoryPage
from pages_POM.cart_page import CartPage
from pages_POM.checkout_step_one_page import CheckoutStepOnePage
from pages_POM.checkout_step_two_page import CheckoutStepTwoPage
from pages_POM.checkout_complete_page import CheckoutCompletePage
from conftest import *
from utils.logger import log

@pytest.mark.ui
@pytest.mark.regression
def test_checking_header(driver):
    log.info('Старт теста "test_checking_header"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    checkout_step_two_page.go_to_finish()

    assert 'Thank you for your order!' in checkout_complete_page.checking_header()
    log.info('Тест "test_checking_header" успешно завершен')

@pytest.mark.ui
@pytest.mark.regression
def test_checking_text(driver):
    log.info('Старт теста "test_checking_text"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    checkout_step_two_page.go_to_finish()

    assert 'Your order has been dispatched' in checkout_complete_page.checking_text()
    log.info('Тест "test_checking_text" успешно завершен')

@pytest.mark.ui
@pytest.mark.smoke
def test_back_to_inventory(driver):
    log.info('Старт теста "test_back_to_inventory"')
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_step_one_page = CheckoutStepOnePage(driver)
    checkout_step_two_page = CheckoutStepTwoPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    inventory_page.add_to_cart('Sauce Labs Backpack')
    inventory_page.add_to_cart('Sauce Labs Fleece Jacket')

    inventory_page.go_to_cart()

    cart_page.go_to_checkout()

    checkout_step_one_page.information('Emily', 'Curter', '123-456')

    checkout_step_two_page.go_to_finish()

    checkout_complete_page.back_to_inventory()
    assert 'inventory' in driver.current_url, 'Не удалось вернуться на страницу с товаром'
    log.info('Тест "test_back_to_inventory" успешно завершен')