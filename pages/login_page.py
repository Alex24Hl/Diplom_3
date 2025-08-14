import allure

from pages.base_page import BasePage
from locators.locators import LoginLocators
from config import API_LOGIN

class LoginPage(BasePage):
    @allure.title('Метод для перехода на сайт c эндпоинтом "/login"')
    def open(self):
        self.driver.get(API_LOGIN)

    @allure.title('Метод для заполнения поля "Email"')
    def enter_email(self, email):
        self.find_element(LoginLocators.EMAIL_INPUT).send_keys(email)

    @allure.title('Метод для заполнения поля "Пароль"')
    def enter_password(self, password):
        self.find_element(LoginLocators.PASSWORD_INPUT).send_keys(password)

    @allure.title('Метод для клика по кнопке "Войти"')
    def click_login_button(self):
        self.click_element(LoginLocators.LOGIN_BUTTON)

    @allure.title('Метод для клика по полю "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.click_element(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.title('Метод для переключения тогла видимости пароля')
    def toggle_password_visibility(self):
        self.click_element(LoginLocators.PASSWORD_VISIBILITY_TOGGLE)

    @allure.title('Метод для проверки атрибута поля "Пароль"')
    def get_password_input_class(self):
        return self.find_element(LoginLocators.CHECK_INPUT_ACTIVE).get_attribute('class')

    @allure.title('Метод прооверки заголовка "Вход"')
    def is_login_page_displayed(self):
        return self.check_displaying_of_element(LoginLocators.ENTRANCE_TITLE)
