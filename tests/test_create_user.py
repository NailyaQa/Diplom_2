import requests
import allure

from data.data import BASE_URL, REGISTER_USER_ENDPOINT
from helpers.user_generator import generate_user_data
from helpers.ingredient_helper import get_ingredient_ids


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user_success(
        self,
        delete_user_after_test
    ):
        user_data = generate_user_data()

        response = requests.post(
            f"{BASE_URL}{REGISTER_USER_ENDPOINT}",
            json=user_data
        )

        delete_user_after_test["access_token"] = (
            response.json()["accessToken"]
        )
        
        assert response.status_code == 200
        assert response.json()["success"] is True

       

    @allure.title("Создание уже зарегистрированного пользователя")
    def test_create_existing_user_returns_error(
        self,
        registered_user
    ):
        response = requests.post(
            f"{BASE_URL}{REGISTER_USER_ENDPOINT}",
            json=registered_user
        )

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_required_field_returns_error(self):
        user_data = generate_user_data()

        del user_data["password"]

        response = requests.post(
            f"{BASE_URL}{REGISTER_USER_ENDPOINT}",
            json=user_data
        )

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == (
            "Email, password and name are required fields"
        )