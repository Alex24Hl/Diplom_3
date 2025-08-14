import allure
import pytest
import requests
from requests import RequestException

from config import API_INGREDIENTS, API_ORDERS

@allure.title('Создает заказ через API и возвращает его номер')
def create_order_via_api(token):
    ingredients_response = requests.get(API_INGREDIENTS)
    ingredients_data = ingredients_response.json()
    ingredient_ids = [ingredient['_id'] for ingredient in ingredients_data['data']]

    order_response = requests.post(
        API_ORDERS,
        headers={"Authorization": token},
        json={"ingredients": ingredient_ids[:2]}
    )
    order_response.raise_for_status()
    return order_response.json()['order']['number']

@allure.title('Получает номер последнего заказа пользователя')
def get_user_orders(test_user):
    token = test_user['token'].split()[-1]  # Извлекаем токен без 'Bearer'
    headers = {'Authorization': f'Bearer {token}'}
    try:
        response = requests.get(
            "https://stellarburgers.nomoreparties.site/api/orders",
            headers=headers
        )
        response.raise_for_status()
        return response.json()["orders"][0]["number"]
    except (RequestException, KeyError, IndexError) as e:
        pytest.fail(f"Ошибка при получении заказов через API: {str(e)}")