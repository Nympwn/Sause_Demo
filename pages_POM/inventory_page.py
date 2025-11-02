from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    '''Страница каталога товаров'''

    def add_to_cart(self, product_name):
        button = (By.XPATH, f'//div[text()="{product_name}"]/ancestor::div[@class="inventory_item"]//button')
        self.click(button)

    def get_cart_count(self, value):
        count = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        return int(count)

    def filter(self, filter_number):
        wait = WebDriverWait(self.driver, 10)
        filter = self.driver.find_element(By.CLASS_NAME, 'product_sort_container')
        self.click(filter)
        add_filter = wait.until(
            EC.element_to_be_clickable(
            self.driver.find_element(By.XPATH, f'//*[@id="header_container"]/div[2]/div/span/select/option[{filter_number}]'))
        )
        self.click(add_filter)
        return add_filter

    def go_to_cart(self):
        cart = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
        return cart.click()