from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage

class InventoryPage(BasePage):
    '''Страница каталога товаров'''

    def add_to_cart(self, product_name):
        button = (By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')
        self.click(button)

    def get_cart_count(self, value):
        count = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        return int(count)

    def filter(self):
        filter = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        self.click(filter)
        add_filter = self.driver.find_element(By.LINK_TEXT, ['Name (A to Z)', 'Name (Z to A)', 'Price (low to high)', 'Price (high to low)']).text
        self.click(add_filter)
        return str(add_filter)