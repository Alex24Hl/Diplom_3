import allure

from pages.login_page import LoginPage
from pages.password_page import PasswordPage


class TestPasswordRecovery:
    @allure.title('Тест на проверка перехода на страницу восстановления пароля')
    def test_go_to_password_recovery_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.click_forgot_password_link()

        forgot_page = PasswordPage(driver)
        assert forgot_page.is_forgot_password_page_displayed()

    @allure.title('Тест на проверку ввода почты и клика по кнопке восстановления')
    def test_reset_password_with_email(self, driver, test_user):
        forgot_page = PasswordPage(driver)
        forgot_page.open()
        forgot_page.enter_email(test_user['email'])
        forgot_page.click_reset_button()
        assert forgot_page.is_forgot_password_page_displayed()

    @allure.title("Тест на проверка подсветки поля пароля")
    def test_password_visibility(self, driver):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.toggle_password_visibility()
        assert "input_status_active" in login_page.get_password_input_class()
