from enum import Enum
from Models.Customer import Customer
from Models.Meal import Meal
from Models.Order import Order


class ModelList(Enum):
    Customer = Customer
    Meal = Meal
    Order = Order
