from enum import Enum


def listCategory():
    for category in Category:
        print(category.name + ': ' + str(category.value))
    return len(Category)


class Category(Enum):
    STARTER = "starter"
    MAIN = "main"
    DESSERT = "dessert"
