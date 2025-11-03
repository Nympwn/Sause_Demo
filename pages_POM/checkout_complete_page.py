from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage(BasePage):
    '''Страница с подтверждением оформления заказа'''
    BACK_BUTTON = (By.ID, 'back-to-products')
    def checking_header(self):
        header = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        return header.text

    def checking_text(self):
        text = self.driver.find_element(By.CLASS_NAME, 'complete-text')
        return text.text

    def back_to_inventory(self):
        self.click(self.BACK_BUTTON)
