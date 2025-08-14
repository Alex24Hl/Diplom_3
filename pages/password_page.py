import allure

from pages.base_page import BasePage
from locators.locators import PasswordLocators
from config import API_FORGOT_PASSWORD

class PasswordPage(BasePage):
    @allure.title('Метод для перехода на сайт c эндпоинтом "/forgot-password"')
    def open(self):
        self.driver.get(API_FORGOT_PASSWORD)

    @allure.title('Метод для заполнения поля "Email"')
    def enter_email(self, email):
        self.find_element(PasswordLocators.EMAIL_INPUT).send_keys(email)

    @allure.title('Метод для клика по кнопке "Восстановить"')
    def click_reset_button(self):
        self.click_element(PasswordLocators.RESET_BUTTON)

    @allure.title('Метод для проверки активности кнопки')
    def is_reset_button_active(self):
        return "button_disabled" not in self.find_element(
            PasswordLocators.RESET_BUTTON).get_attribute("class")

    @allure.title('Метод для проверки заголовка "Восстановление пароля"')
    def is_forgot_password_page_displayed(self):
        return self.check_displaying_of_element(PasswordLocators.PASSWORD_RECOVERY_TITLE)