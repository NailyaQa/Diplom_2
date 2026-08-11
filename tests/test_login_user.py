import requests
import allure

from data.data import BASE_URL
from helpers.user_generator import generate_user_data

class TestLoginUser:


    @allure.title("Авторизация под существующим пользователем")
    def test_login_existing_user_success(self):
        user_data = generate_user_data()

        requests.post(
            f"{BASE_URL}/api/auth/register",
            json=user_data
    )

        response = requests.post(
            f"{BASE_URL}/api/auth/login",
            json={
            "email": user_data["email"],
            "password": user_data["password"]
        }
    )

        assert response.status_code == 200
        assert response.json()["success"] is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Авторизация с неверными логином и паролем")
    def test_login_with_invalid_credentials_returns_error(self):
        response = requests.post(
            f"{BASE_URL}/api/auth/login",
            json={
                "email": "wrong_user@yandex.ru",
                "password": "wrong_password"
            }
        )

        assert response.status_code == 401
        assert response.json()["success"] is False
        assert response.json()["message"] == (
            "email or password are incorrect"
        )

