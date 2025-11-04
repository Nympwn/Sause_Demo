import allure
from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from utils.logger import log

class InventoryPage(BasePage):
    '''Страница каталога товаров'''

    @allure.step('Добавление товара в корзину.')
    def add_to_cart(self, product_name):
        button = (By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')
        self.click(button)
        log.info(f'Товар {product_name} успешно добавлен.')

    @allure.step('Проверка количества товаров в корзине')
    def get_cart_count(self):
        count = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        log.debug(f'Количество товара в корзине: {int(count)}')
        return int(count)

    @allure.step('Проверка работы фильтра')
    def filter(self, filter_number):
        filter = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        self.click(filter)
        add_filter = self.driver.find_element(By.XPATH, f'//*[@id="header_container"]/div[2]/div/span/select/option[{filter_number}]')
        self.click(add_filter)
        log.debug(f'Фильтр был успешно применен.')
        return add_filter

    @allure.step('Переход в корзину.')
    def go_to_cart(self):
        cart = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        cart.click()
        log.info('Успешный переход в корзину.')