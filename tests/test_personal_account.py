import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


class TestPersonalAccount:
    @allure.title("Тест на проверку перехода в личный кабинет")
    def test_go_to_personal_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_account_button()

        profile_page = ProfilePage(driver)
        assert profile_page.is_profile_section_displayed()

    @allure.title("Тест на проверку переход в историю заказов")
    def test_go_to_order_history(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_account_button()

        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        assert profile_page.is_order_history_displayed()

    @allure.title("Тест на проверку логаута")
    def test_logout_from_account(self, driver, login):
        main_page = MainPage(driver)
        main_page.click_account_button()

        profile_page = ProfilePage(driver)
        profile_page.click_logout()

        login_page = LoginPage(driver)
        assert login_page.is_login_page_displayed()