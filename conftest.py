import pytest
import requests

from data.data import BASE_URL, REGISTER_USER_ENDPOINT
from helpers.user_generator import generate_user_data



@pytest.fixture
def delete_user_after_test():
    user_data = {}

    yield user_data

    if "access_token" in user_data:
        requests.delete(
            f"{BASE_URL}/api/auth/user",
            headers={
                "Authorization": user_data["access_token"]
            }
        )

@pytest.fixture
def registered_user():
    user_data = generate_user_data()

    response = requests.post(
        f"{BASE_URL}{REGISTER_USER_ENDPOINT}",
        json=user_data
    )

    access_token = response.json()["accessToken"]

    yield user_data

    requests.delete(
        f"{BASE_URL}/api/auth/user",
        headers={
            "Authorization": access_token
        }
    )