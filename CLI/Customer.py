import json

from Data.Customer import customerList, customerSelect
from colorama import Fore as fo, Back as bo
from Data.DataVerification import dataVerification, dataInput
from Methods.dataManagement import extJson
from Models.Customer import Customer
from Models.ModelList import ModelList
from Models.Path import Path


def customerAction():
    while True:
        action = input(
                    fo.BLACK + bo.LIGHTGREEN_EX + '1: Create Customer' + bo.RESET + '\n\n' + bo.YELLOW + '2: Update Customer' + bo.RESET + '\n\n' + bo.LIGHTMAGENTA_EX + '3: Delete Customer' + bo.RESET + '\n\n' + bo.RED + fo.BLACK + '4: Exit' + bo.RESET + '\n\n' + bo.RESET + fo.YELLOW + 'Choose an action: ' + fo.RESET)
        if action == '1':
            name, surname, phone = dataInput()
            if dataVerification(name, surname, phone):
                customer = Customer(name, surname, phone)
                customer.create(customer)

        elif action == '2':
            customer = customerList()
            if not customer:
                return
            customer = customerSelect()
            if not dataVerification(customer):
                print(fo.RED + 'Invalid Customer' + fo.RESET)
                return
            name, surname, phone = dataInput()
            if dataVerification(name, surname, phone, customer):
                customer = Customer(name, surname, phone)
                customer.update(customer)

        elif action == '3':
            customerList()
            customer = json.dumps(customerSelect())
            if dataVerification(customer):
                customer = json.loads(customer)
                customer = Customer(customer['name'], customer['surname'], customer['phone'])
                customer.delete(customer)




        elif action == '4':
            break