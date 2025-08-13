import allure

from pages.base_page import BasePage
from locators.locators import OrderLocators

from config import API_FEED

class OrderPage(BasePage):
    @allure.title('Метод для перехода на сайт c эндпоинтом "/feed"')
    def open(self):
        self.driver.get(API_FEED)

    @allure.title('Метод для клика по заказу')
    def click_order(self):
        self.click_element(OrderLocators.ORDER_ITEM)

    @allure.title('Метод отображения модального окна')
    def is_order_modal_displayed(self):
        return self.check_displaying_of_element(OrderLocators.ORDER_MODAL)

    @allure.title('Метод получения заказов выполненных за всё время')
    def get_total_orders(self):
        return int(self.find_element(OrderLocators.TOTAL_ORDERS).text)

    @allure.title('Метод получения заказов выполненных за сегодня')
    def get_today_orders(self):
        return int(self.find_element(OrderLocators.TODAY_ORDERS).text)

    @allure.title('Метод для проверки заголовка "Лента заказов"')
    def is_feed_page_displayed(self):
        return self.check_displaying_of_element(OrderLocators.FEED_TITLE)
