import allure
from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from utils.logger import log

class CheckoutCompletePage(BasePage):
    '''Страница с подтверждением оформления заказа'''

    BACK_BUTTON = (By.ID, 'back-to-products')

    @allure.step('Проверка заголовка.')
    def checking_header(self):
        header = self.driver.find_element(By.CSS_SELECTOR, 'h2')
        log.info('Заголовок обнаружен.')
        return header.text

    @allure.step('Проверка текста, подтверждающего заказ.')
    def checking_text(self):
        text = self.driver.find_element(By.CLASS_NAME, 'complete-text')
        log.info('Текст обнаружен.')
        return text.text

    @allure.step('Возвращение на страницу товаров.')
    def back_to_inventory(self):
        self.click(self.BACK_BUTTON)
        log.info('Вы успешно вернулись к странице с товарами.')
