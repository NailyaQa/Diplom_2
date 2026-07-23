import requests
import allure

from data.data import BASE_URL, CREATE_ORDER_ENDPOINT


@allure.step("Создать заказ")
def create_order(ingredient_ids, access_token=None):
    headers = {}

    if access_token:
        headers["Authorization"] = access_token

    return requests.post(
        f"{BASE_URL}{CREATE_ORDER_ENDPOINT}",
        headers=headers,
        json={
            "ingredients": ingredient_ids
        }
    )