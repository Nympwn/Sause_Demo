import pytest
from conftest import *
from pages_POM.login_page import LoginPage

@pytest.mark.ui
@pytest.mark.smoke
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login('standard_user', 'secret_sauce')

@pytest.mark.ui
@pytest.mark.regression
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login('invalid_user', 'wrong')

    assert 'Epic sadface' in login_page.get_error_message()