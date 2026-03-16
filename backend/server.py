from fastapi import FastAPI
from models.order import Order
from models.product import Product

app = FastAPI()

products = {
    "iphone": {"name": "iPhone 15", "price": 999},
    "ipad": {"name": "iPad Air", "price": 799}
}

orders = {
    "1001": {"product": "iphone", "status": "shipped"},
    "1002": {"product": "ipad", "status": "processing"}
}


@app.get("/products")
def get_products():
    return products


@app.get("/order/{order_id}")
def get_order(order_id: str):
    return orders.get(order_id, {"error": "order not found"})