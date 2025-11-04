import allure
from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from utils.logger import log

class LoginPage(BasePage):
    '''Страница логина'''
    USERNAME_INPUT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    @allure.step('Открытие страницы сайта.')
    def open_login_page(self):
        self.open('https://www.saucedemo.com/')
        log.info('Страница успешно открыта.')

    @allure.step('Авторизация на сайте.')
    def login(self, username, password):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        log.info('Авторизация прошла успешно.')

    @allure.step('Ошибка, возникающая при неверных данных.')
    def get_error_message(self):
        log.error('Ошибка авторизации – ввод неверных данных.')
        return self.get_text(self.ERROR_MESSAGE)