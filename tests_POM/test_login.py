import pytest
from conftest import *
from pages_POM.login_page import LoginPage
from utils.logger import log

@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(driver):
    log.info('Старт теста: test_successful_login')
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

    assert 'inventory' in driver.current_url, 'Не удалось авторизоваться'

    log.info('Тест успешно завершен: test_successful_login')

@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(driver):
    log.info('Старт теста: test_invalid_login')
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login('invalid_user', 'wrong')

    assert 'Epic sadface' in login_page.get_error_message()
    log.info('Тест успешно завершен: test_invalid_login')