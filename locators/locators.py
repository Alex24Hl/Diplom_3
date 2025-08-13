from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    PASSWORD_VISIBILITY_TOGGLE = (By.XPATH, "//div[contains(@class, 'input__icon')]")
    ENTRANCE_TITLE = (By.XPATH, "//h2[text()='Вход']")
    CHECK_INPUT_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")

class PasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    RESET_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_RECOVERY_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")

class MainLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_TAB = (By.XPATH, "//p[text()='Лента Заказов']")
    INGREDIENT_ITEM = (By.XPATH, "//div[contains(@class, 'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTER = (By.XPATH, "//div[contains(@class, 'counter_counter')]")
    MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'close')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

class ProfileLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]")
    PROFILE_SECTION = (By.XPATH, "//a[text()='Профиль']")
    ORDER_HISTORY_SECTION = (By.XPATH, "//a[text()='История заказов']")

class OrderLocators:
    ORDER_ITEM = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')]")
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]")
    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10')]")
    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")