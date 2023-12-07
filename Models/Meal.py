from datetime import datetime
import json

from Methods.dataManagement import extJson
from Models.Category import Category
from Models.Path import Path


class Meal(extJson):

    def __init__(self, name, price, description, category):
        self.id = extJson.availableId(Path.Meal)
        self.name = name
        self.price = price
        self.description = description
        if category is None:
            raise TypeError("Category : starter, main or dessert")
        self.category = category
        self.creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'category': self.category.value,
            'creation_date': self.creation_date
        }

    def create(self, model, **kwargs):
        if len(kwargs) > 2:
            return None
        super().create(Path.Meal, model)

    def update(self, model, **kwargs):
        if len(kwargs) > 2:
            return None
        super().update(Path.Meal, model)

    def delete(self, model, **kwargs):
        if len(kwargs) > 2:
            return None
        super().delete(Path.Meal, model)

    def display(self, **kwargs):
        if len(kwargs) > 0:
            return None
        super().display(Path.Meal)
