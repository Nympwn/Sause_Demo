from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutStepTwoPage(BasePage):
    '''Проверка данных перед отправкой товара'''
    CANCEL_BUTTON = (By.ID, 'cancel')
    FINISH_BUTTON = (By.ID, 'finish')

    def checking_item(self, id_product):
        product = self.driver.find_element(By.ID, f'item_{id_product}_title_link')
        return product.text

    def checking_payment__shipping_and_price(self, id_value):
        value = self.driver.find_element(By.XPATH, f'//*[@id="checkout_summary_container"]/div/div[2]/div[{id_value}]')
        return value.text

    def back_to_inventory(self):
        self.click(self.CANCEL_BUTTON)

    def go_to_finish(self):
        self.click(self.FINISH_BUTTON)