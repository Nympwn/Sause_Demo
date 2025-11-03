from email.errors import MessageError

from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage(BasePage):
    '''Страница корзины с товарами'''
    def checkout_cart(self, id):
        name_gds = self.driver.find_element(By.ID, f'item_{id}_title_link').text
        return str(name_gds)

    def checkout_inform(self, num):
        inform = self.driver.find_element(By.ID, f'item_{num}_title_link')
        inform.click()

    def back_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'shopping_cart_link'))
        )
        return cart.click()

    def delete_item(self, name_product):
        delete_button = self.driver.find_element(By.ID, f'remove-{name_product}')
        delete_button.click()

    def find_delete_item(self):
        name = self.driver.find_element(By.CLASS_NAME, 'removed_cart_item')
        return name

    def go_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        checkout = wait.until(
            EC.element_to_be_clickable((By.ID, 'checkout'))
        )
        return checkout.click()