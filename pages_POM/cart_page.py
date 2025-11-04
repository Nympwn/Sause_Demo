from selenium.webdriver.common.by import By
from conftest import driver
from pages_POM.base_page import BasePage
import allure
from utils.logger import log

class CartPage(BasePage):
    '''Страница корзины с товарами'''

    @allure.step('Проверка товара в корзине.')
    def checkout_cart(self, id):
        name_gds = self.driver.find_element(By.ID, f'item_{id}_title_link').text
        log.info('Элемент успешно найден.')
        return str(name_gds)

    @allure.step('Информация о товаре.')
    def checkout_inform(self, num):
        inform = self.driver.find_element(By.ID, f'item_{num}_title_link')
        inform.click()
        log.info('Успешный переход на страницу с информацией о товаре.')

    @allure.step('Возвращение в корзину.')
    def back_to_cart(self):
        cart = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart.click()
        log.info('Успешное возвращение в корзину.')


    @allure.step('Удаление товара из корзины.')
    def delete_item(self, name_product):
        delete_button = self.driver.find_element(By.ID, f'remove-{name_product}')
        delete_button.click()
        log.info('Товар успешно удален.')

    @allure.step('Поиск удаленного товара в корзине. ')
    def find_delete_item(self):
        name = self.driver.find_element(By.CLASS_NAME, 'removed_cart_item')
        return name

    @allure.step('Возвращение на страницу с товарами.')
    def go_to_checkout(self):
        checkout = self.driver.find_element(By.ID, 'checkout')
        checkout.click()
        log.info('Успешное возвращение на страницу товаров.')