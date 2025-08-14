import allure
import time

from pages.base_page import BasePage
from locators.locators import MainLocators

class MainPage(BasePage):
    @allure.title('Метод для клика по кнопке "Войти в аккаунт"')
    def click_login_button(self):
        self.click_element(MainLocators.LOGIN_BUTTON)

    @allure.title('Метод для клика по полю "Личный кабинет"')
    def click_account_button(self):
        self.click_element(MainLocators.ACCOUNT_BUTTON)

    @allure.title('Метод для клика по полю "Конструктор"')
    def click_constructor_tab(self):
        self.click_element(MainLocators.CONSTRUCTOR_TAB)

    @allure.title('Метод для клика по полю "Лента Заказов"')
    def click_order_feed_tab(self):
        self.click_element(MainLocators.ORDER_FEED_TAB)

    @allure.title('Метод для клика по ингредиенту')
    def click_ingredient(self):
        self.click_element(MainLocators.INGREDIENT_ITEM)

    @allure.title('Метод для закрытия модального окна')
    def close_modal(self):
        self.click_element(MainLocators.MODAL_CLOSE)

    @allure.title('Метод для проверки отображения модального окна')
    def is_modal_visible(self):
        time.sleep(1)
        return self.check_displaying_of_element(MainLocators.MODAL)

    @allure.title('Метод для получения количества ингредиентов')
    def get_ingredient_counter(self, index=0):
        ingredients = self.driver.find_elements(*MainLocators.INGREDIENT_ITEM)
        try:
            counter = ingredients[index].find_element(*MainLocators.INGREDIENT_COUNTER)
            return int(counter.text)
        except:
            return 0

    @allure.title('Метод для добавления ингредиента в заказ')
    def add_ingredient_to_order(self, index=0):
        ingredients = self.driver.find_elements(*MainLocators.INGREDIENT_ITEM)
        constructor_area = self.find_element(MainLocators.CONSTRUCTOR_AREA)
        self.drag_and_drop_element(ingredients[index], constructor_area)

    @allure.title('Метод для клика по кнопку "Оформить заказ"')
    def make_order(self):
        self.click_element(MainLocators.ORDER_BUTTON)

    @allure.title('Метод для проверки отображения модального окна заказа')
    def is_order_modal_displayed(self):
        return self.check_displaying_of_element(MainLocators.ORDER_MODAL)

    @allure.title('Метод получения номер заказа')
    def get_order_number(self):
        time.sleep(5)
        return self.find_element(MainLocators.ORDER_NUMBER).text

    @allure.title('Метод для проверки заголовка "Соберите бургер"')
    def is_constructor_displayed(self):
        return self.check_displaying_of_element(MainLocators.CONSTRUCTOR_TITLE)
