


from random import randint

def generate_user_data():
    return {
        "email": f"test{randint(100000, 999999)}@yandex.ru",
        "password": "password123",
        "name": "Naiке"
}
