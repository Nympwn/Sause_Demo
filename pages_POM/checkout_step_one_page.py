from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutStepOnePage(BasePage):
    '''Страница ввода информации об адресе доставки'''
    FIRST_NAME_INPUT = (By.ID, 'first-name')
    LAST_NAME_INPUT = (By.ID, 'last-name')
    ZIP_INPUT = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    CANCEL_BUTTON = (By.ID, 'cancel')
    ERROR_MESSAGE = (By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[1]/div[4]/h3')

    def information(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.ZIP_INPUT, zip_code)
        self.click(self.CONTINUE_BUTTON)

    def cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_message_error(self):
        return self.get_text(self.ERROR_MESSAGE)