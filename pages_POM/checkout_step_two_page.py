import allure
from selenium.webdriver.common.by import By
from pages_POM.base_page import BasePage
from utils.logger import log

class CheckoutStepTwoPage(BasePage):
    '''Проверка данных перед отправкой товара'''
    CANCEL_BUTTON = (By.ID, 'cancel')
    FINISH_BUTTON = (By.ID, 'finish')

    @allure.step('Проверка отображения товаров из корзины.')
    def checking_item(self, id_product):
        product = self.driver.find_element(By.ID, f'item_{id_product}_title_link')
        log.info('Товары успешно обнаружены.')
        return product.text

    @allure.step('Проверка информации о товаре.')
    def checking_payment__shipping_and_price(self, id_value):
        value = self.driver.find_element(By.XPATH, f'//*[@id="checkout_summary_container"]/div/div[2]/div[{id_value}]')
        log.info('Информация по товару обнаружена.')
        return value.text

    @allure.step('Возвращение на страницу товаров.')
    def back_to_inventory(self):
        self.click(self.CANCEL_BUTTON)
        log.info('Вы успешно вернулись к странице товаров.')

    @allure.step('Оформление заказа.')
    def go_to_finish(self):
        self.click(self.FINISH_BUTTON)
        log.info('Заказ успешно оформлен.')