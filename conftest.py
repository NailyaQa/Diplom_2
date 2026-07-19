import pytest
import requests

from data.data import BASE_URL


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