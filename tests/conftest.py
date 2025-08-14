import allure
import pytest
import requests
import random
import string

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL, API_AUTH_REGISTER, API_AUTH_LOGIN, API_AUTH_USER, API_INGREDIENTS, API_ORDERS

from pages.login_page import LoginPage

@allure.title('Фикстура для инициализации драйвера')
@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    elif request.param == 'firefox':
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title('Фикстура генерации уникальных данных пользователя')
@pytest.fixture
def generate_unique_user():
    random_symbol = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return {
        "email": f"user_{random_symbol}@yandex.com",
        "password": f"Password_{random_symbol}",
        "name": f"User_{random_symbol}"
    }

@allure.title('Фикстура создания тестового пользователя')
@allure.description('Создаёт пользователя через API и удаляет после теста')
@pytest.fixture(scope='function')
def test_user(generate_unique_user):
    user_data = generate_unique_user
    register_response = requests.post(
        API_AUTH_REGISTER,
        json={
            "email": user_data["email"],
            "password": user_data["password"],
            "name": user_data["name"]
        }
    )
    assert register_response.status_code == 200, "Не удалось создать пользователя"

    login_response = requests.post(
        API_AUTH_LOGIN,
        json={
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )
    token = login_response.json().get("accessToken")
    user_data["token"] = token

    yield user_data

    requests.delete(
        API_AUTH_USER,
        headers={"Authorization": token}
    )

@allure.title('Фикстура авторизации пользователя')
@pytest.fixture(scope='function')
def login(driver, test_user):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.enter_email(test_user['email'])
    login_page.enter_password(test_user['password'])
    login_page.click_login_button()
    WebDriverWait(driver, 10).until(EC.url_to_be(f"{BASE_URL}/"))
    return driver

@allure.title('Фикстура создания заказа')
@pytest.fixture(scope='function')
def create_order(test_user):
    ingredients_response = requests.get(API_INGREDIENTS)
    ingredients_data = ingredients_response.json()
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data']]
    order_response = requests.post(
        API_ORDERS,
        headers={"Authorization": f"{test_user['token']}"},
        json={"ingredients": ingredient_ids[:2]}
    )
    assert order_response.status_code == 200, "Не удалось создать заказ"
    order_number = order_response.json()['order']['number']
    return order_number
