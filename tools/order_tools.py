import requests

BASE_URL = "http://localhost:8000"


def get_order(order_id):
    r = requests.get(f"{BASE_URL}/order/{order_id}")
    return r.json()