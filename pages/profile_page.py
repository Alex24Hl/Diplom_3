import allure

from pages.base_page import BasePage
from locators.locators import ProfileLocators
from config import API_PROFILE

class ProfilePage(BasePage):
    @allure.title('Метод для перехода на сайт c эндпоинтом "/account/profile"')
    def open(self):
        self.driver.get(API_PROFILE)

    @allure.title('Метод для клика по разделу "История заказов"')
    def click_order_history(self):
        self.click_element(ProfileLocators.ORDER_HISTORY_LINK)

    @allure.title('Метод для клика по разделу "Выход"')
    def click_logout(self):
        self.click_element(ProfileLocators.LOGOUT_BUTTON)

    @allure.title('Метод получения номера заказа')
    def get_order_numbers(self):
        return self.check_displaying_of_element(ProfileLocators.ORDER_ITEM)

    @allure.title('Метод для проверки заголовка "Профиль"')
    def is_profile_section_displayed(self):
        return self.check_displaying_of_element(ProfileLocators.PROFILE_SECTION)

    @allure.title('Метод для проверки заголовка "История заказов"')
    def is_order_history_displayed(self):
        return self.check_displaying_of_element(ProfileLocators.ORDER_HISTORY_SECTION)
