import json
import Models
from Models.Path import Path


class extJson:

    def to_json(self):
        raise NotImplementedError("Should have implemented this")

    def create(self, path, model):
        try:
            open(path.value, 'r')
        except FileNotFoundError:
            file = open(path.value, 'w')
            file.write("[]")
            file.close()
        with open(path.value, 'r') as file:
            data = json.load(file)
            data.append(model.to_json())
            with open(path.value, 'w') as wfile:
                json.dump(data, wfile, indent=4)
        file.close()

    @staticmethod
    def display(path):
        with open(path.value, 'r') as file:
            data = json.load(file)
            if path == Path.Customer:
                if len(data) == 0:
                    print('\nNo Customer Found\n')
                    return False
                for customer in data:
                    print(str(customer['id']) + ": " + customer['name'] + " " + customer['surname'] + ", Number: " +
                          customer['phone'])
                file.close()
                return True
            elif path == Path.Meal:
                if len(data) == 0:
                    print('\nNo Meal Found\n')
                    return False
                for meal in data:
                    print(str(meal['id']) + ": " + meal['name'] + "\n Price: " + str(meal['price']) + ", Description: " +
                          meal['description'])
                file.close()
                return True
            elif path == Path.Order:
                if len(data) == 0:
                    print('\nNo Order Found\n')
                    return False
                for order in data:
                    print(str(order['id']) + ": " + order['customer'] + " " + order['meal'] + ", Price: " +
                          str(order['price']) + ", Date: " + order['date'])
                file.close()
                return True

    def update(self, path, model):
        # --------- To Avoid Circular Import ---------
        from Models.Customer import Customer
        from Models.Meal import Meal
        from Models.Order import Order
        # --------------------------------------------

        if not (isinstance(model, (Customer, Meal, Order))):
            print("Model is not valid !")
            return None
        with open(path.value, 'r') as file:
            if isinstance(model, Customer):
                data = json.load(file)
                for item in data:
                    if item['id'] == model.id - 1:
                        item['name'] = model.name
                        item['surname'] = model.surname
                        item['phone'] = model.phone
                        break
                with open(path.value, 'w') as wfile:
                    json.dump(data, wfile, indent=4)
            elif isinstance(model, Meal):
                data = json.load(file)
                for item in data:
                    print(item['id'], model.id)
                    if item['id'] == model.id - 1: # -1 because we create a new item to update
                        item['name'] = model.name
                        item['price'] = model.price
                        item['description'] = model.description
                        item['category'] = model.category.value
                        break
                with open(path.value, 'w') as wfile:
                    json.dump(data, wfile, indent=4)
            elif isinstance(model, Order):
                data = json.load(file)
                for item in data:
                    if item['id'] == model.id - 1:
                        item['customerId'] = model.customerId
                        item['meals'] = [meal.id for meal in model.meals]
                        item['total_price'] = model.total_price
                        item['date'] = model.date
                        break
                with open(path.value, 'w') as wfile:
                    json.dump(data, wfile, indent=4)
            else:
                print("Model is not valid !")
                return None
        file.close()
    @staticmethod
    def delete(path, model):
        with open(path.value, 'r') as file:
            data = json.load(file)
            for item in data:
                if item['id'] == model.id - 1:
                    data.remove(item)
                    break
            with open(path.value, 'w') as writefile:
                json.dump(data, writefile, indent=4)
        file.close()

    @staticmethod
    def availableId(path):
        #check if the file exists
        try:
            file = open(path.value, 'r')
        except FileNotFoundError:
            file = open(path.value, 'w')
            file.write("[]")
            file.close()
        with open(path.value, 'r') as file:
            data = json.load(file)
            if len(data) == 0:
                return 1
            file.close()

            for i in range(len(data)):
                if data[i]['id'] != i + 1:
                    return i + 1
            return len(data) + 1
