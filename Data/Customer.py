import json
from colorama import Fore as fo


def selectCustomer():
    with open('Data/Json/Customers.json', 'r') as file:
        customers = json.load(file)
    for customer in customers:
        print(customer['id'], customer['name'], customer['surname'], customer['phone'])


def customerList():
    #check if file exists
    try:
        file = open('Data/Json/Customers.json', 'r')
    except FileNotFoundError:
        file = open('Data/Json/Customers.json', 'w')
        file.write("[]")
        file.close()
    with open('Data/Json/Customers.json', 'r') as file:
        data = json.load(file)
        if len(data) == 0:
            print(fo.RED + '\nNo Customer Found\n' + fo.RESET)
            return False
        for customer in data:
            print(fo.RED + str(customer['id']) + ": " + fo.RESET + fo.GREEN + customer['name'] + " " + fo.YELLOW +
                  customer['surname'] + fo.RESET + ", Number: " + fo.CYAN + customer['phone'] + fo.RESET)
        file.close()
        return True


def customerSelect():
    with open('Data/Json/Customers.json', 'r') as file:
        data = json.load(file)
        file.close()
        customer = input('Select Customer: ')
        try:
            selection = int(customer)
        except ValueError:
            return None
        for customer in data:
            if customer['id'] == int(selection):
                return customer
        return None


def getJsonLength():
    with open('Data/Json/Customers.json', 'r') as file:
        data = json.load(file)
        file.close()
        return len(data)
