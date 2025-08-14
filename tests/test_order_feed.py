import allure

from pages.order_page import OrderPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from helpers import create_order_via_api
from helpers import get_user_orders


class TestOrderFeed:
    @allure.title("Тест на открытие деталей заказа")
    def test_open_order_details(self, driver):
        order_page = OrderPage(driver)
        order_page.open()
        order_page.click_order()
        assert order_page.is_order_modal_displayed()

    @allure.title("Тест на отображение заказов пользователя в ленте")
    def test_user_orders_in_feed(self, driver, login, create_order):
        main_page = MainPage(driver)
        main_page.click_account_button()

        profile_page = ProfilePage(driver)
        profile_page.click_order_history()
        profile_page.get_order_numbers()

    @allure.title("Тест на увеличение счетчика 'Выполнено за всё время'")
    def test_total_orders_counter_increases(self, driver, test_user):
        order_page = OrderPage(driver)
        order_page.open()

        initial_total = order_page.get_total_orders()
        create_order_via_api(test_user['token'])
        driver.refresh()

        new_total = order_page.get_total_orders()
        assert new_total > initial_total, "Cчётчик 'Выполнено за всё время' не изменился"

    @allure.title("Тест на увеличение счетчика 'Выполнено за сегодня'")
    def test_today_orders_counter_increases(self, driver, test_user):
        order_page = OrderPage(driver)
        order_page.open()

        initial_today = order_page.get_today_orders()
        create_order_via_api(test_user['token'])
        driver.refresh()

        new_today = order_page.get_today_orders()
        assert new_today > initial_today, "Cчётчик 'Выполнено за сегодня' не изменился"

    @allure.title("Тест на отображение заказа в разделе 'В работе'")
    def test_new_order_in_progress(self, driver, test_user, login):
        main_page = MainPage(driver)
        main_page.open()
        main_page.add_ingredient_to_order(0)
        main_page.make_order()
        main_page.is_order_modal_displayed()
        order_number = main_page.get_order_number()

        order_page = OrderPage(driver)
        order_page.open()

        api_order_number = str(get_user_orders(test_user))
        assert order_number == api_order_number