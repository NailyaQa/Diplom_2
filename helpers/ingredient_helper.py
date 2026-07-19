import requests

from data.data import BASE_URL


def get_ingredient_ids():
    response = requests.get(
        f"{BASE_URL}/api/ingredients"
    )

    return [
        response.json()["data"][0]["_id"],
        response.json()["data"][1]["_id"]
    ]