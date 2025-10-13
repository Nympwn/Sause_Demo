import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_pay(driver):
    driver.get('https://www.saucedemo.com/')
    time.sleep(3)

    username_input = driver.find_element(By.NAME, 'user-name')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.click()
    username_input.send_keys('standard_user')
    password_input.click()
    password_input.send_keys('secret_sauce')

    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()

    time.sleep(3)

    assert 'inventory' in driver.current_url, 'Не удалось авторизоваться'

    pay_button_backpack = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-backpack')
    pay_button_jacket = driver.find_element(By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')
    pay_button_backpack.click()
    pay_button_jacket.click()

    time.sleep(3)

    basket = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    basket.click()

    time.sleep(10)

    assert 'cart' in driver.current_url, 'Не удалось перейти в корзину'

    backpack = driver.find_element(By.LINK_TEXT, 'Sauce Labs Backpack')
    jacket = driver.find_element(By.LINK_TEXT, 'Sauce Labs Fleece Jacket')

    assert backpack.is_displayed()
    assert jacket.is_displayed()

    checkout_button = driver.find_element(By.NAME, 'checkout')
    checkout_button.click()
    time.sleep(3)

    assert 'checkout-step-one' in driver.current_url, 'Не удалось продолжить покупку'

    first_name_input = driver.find_element(By.NAME, 'firstName')
    last_name_input = driver.find_element(By.NAME, 'lastName')
    zip_input = driver.find_element(By.NAME, 'postalCode')

    first_name_input.click()
    first_name_input.send_keys('Mary')
    last_name_input.click()
    last_name_input.send_keys('Dgayr')
    zip_input.click()
    zip_input.send_keys(12312334)

    continue_button = driver.find_element(By.NAME, 'continue')
    continue_button.click()
    time.sleep(3)

    assert 'checkout-step-two' in driver.current_url, 'Не удалось заполнить данные о покупателе'

    backpack = driver.find_element(By.LINK_TEXT, 'Sauce Labs Backpack')
    jacket = driver.find_element(By.LINK_TEXT, 'Sauce Labs Fleece Jacket')
    payment_information = driver.find_element(By.CLASS_NAME, 'summary_value_label')
    shipping_information = driver.find_element(By.CLASS_NAME, 'summary_value_label')
    price_total = driver.find_element(By.CLASS_NAME, 'summary_total_label')
    time.sleep(3)

    assert backpack.is_displayed()
    assert jacket.is_displayed()
    assert payment_information.is_displayed()
    assert shipping_information.is_displayed()
    assert price_total.is_displayed()

    finish_button = driver.find_element(By.NAME, 'finish')
    finish_button.click()
    time.sleep(3)

    assert 'checkout-complete' in driver.current_url

    thanks = driver.find_element(By.CLASS_NAME,  'complete-text')
    back_home_button = driver.find_element(By.NAME, 'back-to-products')

    assert thanks.is_displayed()
    assert back_home_button.is_displayed()