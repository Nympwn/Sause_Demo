import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--start-maximized')
    options.add_experimental_option('prefs', {
        'profile.password_manager_leak_detection': False
    })
    options.add_argument('--disable-notifications') # отключение всплывающих уведомлений
    options.add_argument('--disable-save-password-bubble') # отключает всплывающие окна, связанные с паролем
    options.add_argument('--no-default_browser-check')
    options.add_argument('--disable-features=PasswordLeakDetection')
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_login_and_pay(driver):
    wait = WebDriverWait(driver, 10)

    driver.get('https://www.saucedemo.com/')
    driver.implicitly_wait(5)
# Авторизация
    username_input = driver.find_element(By.NAME, 'user-name')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.click()
    username_input.send_keys('standard_user')
    password_input.click()
    password_input.send_keys('secret_sauce')

    login_button = driver.find_element(By.NAME, 'login-button')
    login_button.click()

    assert 'inventory' in driver.current_url, 'Не удалось авторизоваться'

# Страница выбора товара

    # header_text = driver.find_element(By.CLASS_NAME, 'title').text
    header_text = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'title'))
    ).text

    assert header_text == 'Products'

    backpack = wait.until((EC.element_to_be_clickable((By.NAME, 'add-to-cart-sauce-labs-backpack'))))
    backpack.click()
    jacket = wait.until(EC.element_to_be_clickable((By.NAME, 'add-to-cart-sauce-labs-fleece-jacket')))
    jacket.click()

    basket = wait.until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
    )
    basket.click()

# Корзина

    assert 'cart' in driver.current_url, 'Не удалось перейти в корзину'

    backpack = driver.find_element(By.ID, 'item_4_title_link').text
    jacket = driver.find_element(By.ID, 'item_5_title_link').text

    assert backpack == 'Sauce Labs Backpack'
    assert jacket == 'Sauce Labs Fleece Jacket'

    checkout_button = driver.find_element(By.NAME, 'checkout')
    checkout_button.click()

    driver.implicitly_wait(5)

# Ввод данных для доставки

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

    continue_button = wait.until(
        EC.element_to_be_clickable((By.NAME, 'continue'))
    )
    continue_button.click()

    driver.implicitly_wait(5)

# Проверка заказа

    assert 'checkout-step-two' in driver.current_url, 'Не удалось заполнить данные о покупателе'
    assert backpack == 'Sauce Labs Backpack'
    assert jacket == 'Sauce Labs Fleece Jacket'

    finish_button = driver.find_element(By.NAME, 'finish')
    finish_button.click()

    driver.implicitly_wait(5)

# Финальная страница

    assert 'checkout-complete' in driver.current_url

    thanks = driver.find_element(By.CLASS_NAME,  'complete-header').text
    thanks_text = driver.find_element(By.CLASS_NAME, 'complete-text').text
    back_home_button = driver.find_element(By.NAME, 'back-to-products')

    assert thanks == 'Thank you for your order!'
    assert thanks_text == 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
    assert back_home_button.is_displayed()