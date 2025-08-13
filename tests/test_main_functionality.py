import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainFunctionality:
    @allure.title("Тест на переход в конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_constructor_tab()
        assert main_page.is_constructor_displayed()

    @allure.title("Тест на переход в ленту заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_order_feed_tab()

        order_page = OrderPage(driver)
        assert order_page.is_feed_page_displayed()

    @allure.title("Тест на открытие деталей ингредиента")
    def test_open_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        assert main_page.is_modal_visible()

    @allure.title("Тест на закрытие модального окна")
    def test_close_ingredient_details(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.click_ingredient()
        main_page.close_modal()
        assert not main_page.is_modal_visible()

    @allure.title("Тест на увеличение счетчика ингредиента")
    def test_ingredient_counter_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.open()
        initial_count = main_page.get_ingredient_counter(0)
        main_page.add_ingredient_to_order(0)
        assert main_page.get_ingredient_counter(0) > initial_count

    @allure.title("Тест на оформление заказа авторизованным пользователем")
    def test_create_order_by_logged_in_user(self, driver, login):
        main_page = MainPage(driver)
        main_page.add_ingredient_to_order(0)
        main_page.make_order()
        assert main_page.is_order_modal_displayed()