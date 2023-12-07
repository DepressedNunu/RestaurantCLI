# style Import
import json

import colorama
from colorama import Fore as fo, Back as bo

# Category Import
from Models.Category import listCategory, Category
from Models.Meal import Meal

# Methods Import
from Methods.dataManagement import extJson
from Models.Path import Path


def mealAction():
    while True:
        action = input(
            fo.BLACK + bo.LIGHTGREEN_EX + '1: Create Meal' + bo.RESET + '\n\n' + bo.YELLOW + '2: Update Meal' + bo.RESET + '\n\n' + bo.LIGHTMAGENTA_EX + '3: Delete Meal' + bo.RESET + '\n\n' + bo.RED + fo.BLACK + '4: Exit' + bo.RESET + '\n\n' + bo.RESET + fo.YELLOW + 'Choose an action: ' + fo.RESET)
        match action:
            case '1':
                name, price, description, category = mealInfo()
                if checkInfo(name, price, description, category):
                    meal = Meal(name, price, description, category)
                    meal.create(meal)
            case '2':
                meal = selectMeal()
                if checkInfo(meal):
                    name, price, description, category = mealInfo()
                    if checkInfo(name, price, description, category, meal):
                        meal = Meal(name, price, description, category)
                        meal.update(meal)
            case '3':
                meal = selectMeal()
                if checkInfo(meal):
                    meal = Meal(meal['name'], meal['price'], meal['description'], meal['category'])
                    meal.delete(meal)
            case '4':
                break


def selectMeal():
    # List the meals
    if not extJson.display(Path.Meal):
        print(fo.RED + '\nNo Meal Found\n' + fo.RESET)
        return None
    # Select a meal
    action = input(fo.LIGHTGREEN_EX + 'Select the meal: ' + fo.RESET)
    if action <= '0' or action > str(len(mealList())):
        return None
    meal = mealList()[int(action) - 1]
    return meal


def mealList():
    try:
        file = open('Data/Json/Meal.json', 'r')
    except FileNotFoundError:
        file = open('Data/Json/Meal.json', 'w')
        file.write("[]")
        file.close()
    with open('Data/Json/Meal.json', 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            print(fo.RED + '\nNo Meal Found\n' + fo.RESET)
            return []
        return data


def mealInfo():
    category = None
    action = input(fo.LIGHTGREEN_EX + 'Enter name: ' + fo.RESET)
    name = action
    action = input(fo.LIGHTGREEN_EX + 'Enter price: ' + fo.RESET)
    price = action
    try:
        price = float(action)
    except ValueError:
        return None, None, None, None
    action = input(fo.LIGHTGREEN_EX + 'Enter description: ' + fo.RESET)
    description = action
    print(listCategory())
    action = input(fo.LIGHTGREEN_EX + 'Enter category: ' + fo.RESET)
    try:
        action = int(action)
    except ValueError:
        return None, None, None, None

    if action <= 0 or action > listCategory():
        return None, None, None, None
    if action == 1:
        category = Category.STARTER
    elif action == 2:
        category = Category.MAIN
    elif action == 3:
        category = Category.DESSERT
    return name, float(price), description, category


def checkInfo(*args):
    for arg in args:
        if arg is None:
            print(fo.RED + '\n Invalid Type' + str(arg) + "\n" + fo.RESET)
            return False
    return True
