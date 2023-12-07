from Methods.dataManagement import extJson
from Models.Path import Path


class Customer(extJson):
    customerId = 0

    def __init__(self, name, surname, phone):
        self.id = extJson.availableId(Path.Customer)
        self.name = name
        self.surname = surname
        self.phone = phone

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'phone': self.phone
        }

    def create(self, model, **kwargs):
        super().create(Path.Customer, model)

    def update(self, model, **kwargs):
        super().update(Path.Customer, model)

    def delete(self, model, **kwargs):
        super().delete(Path.Customer, model)

