import requests
import allure

from data.data import BASE_URL
from helpers.user_generator import generate_user_data
from helpers.ingredient_helper import get_ingredient_ids
from helpers.ingredient_helper import get_ingredient_ids
from helpers.order_helper import create_order


class TestCreateOrder:

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_with_authorization_success(
        self,
        delete_user_after_test
    ):
        ingredient_ids = get_ingredient_ids()

        response = create_order(
            ingredient_ids,
            delete_user_after_test
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()
        assert "number" in response.json()["order"]

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_authorization_success(self):
        ingredient_ids = get_ingredient_ids()

        response = requests.post(
            f"{BASE_URL}/api/orders",
            json={
                "ingredients": ingredient_ids
            }
        )

        assert response.status_code == 200
        assert response.json()["success"] is True

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients_success(self):
        ingredient_ids = get_ingredient_ids()

        response = requests.post(
            f"{BASE_URL}/api/orders",
            json={
                "ingredients": ingredient_ids
            }
        )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "order" in response.json()

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_returns_error(self):
        response = requests.post(
            f"{BASE_URL}/api/orders",
            json={
                "ingredients": []
            }
        )

        assert response.status_code == 400
        assert response.json()["success"] is False
        assert response.json()["message"] == (
            "Ingredient ids must be provided"
        )

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_with_invalid_ingredient_hash_returns_error(self):
        response = requests.post(
            f"{BASE_URL}/api/orders",
            json={
                "ingredients": [
                    "invalid_ingredient_hash"
                ]
            }
        )

        assert response.status_code == 500