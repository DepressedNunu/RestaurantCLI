import json
from datetime import datetime

from Methods.dataManagement import extJson
from Models.Meal import Meal
from Models.Path import Path


class Order(extJson):
    total_price = 0
    orderId = 0
    orderList = []  # keep track of all orders instances

    def __init__(self, customer, *args):
        Order.orderId += 1
        self.id = Order.orderId
        self.customerId = customer.id
        for meal in args:
            if meal is None:
                continue
            self.meals = []
            if not isinstance(meal, Meal):
                print("Meal: " + meal + "is not valid !")
                continue
            self.meals.append(meal)
            self.total_price += meal.price
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def create(self, model, **kwargs):
        super().create(Path.Order, model)

    def update(self, model, **kwargs):
        super().update(Path.Order, model)

    def delete(self, model, **kwargs):
        super().delete(Path.Order, model)

    def to_json(self):
        return {
            'id': self.id,
            'customerId': self.customerId,
            'meals': [meal.id for meal in self.meals],
            'total_price': self.total_price,
            'date': self.date
        }