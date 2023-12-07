
# style Import
from colorama import Fore as fo


def orderAction():
    while True:
        action = input(
            fo.LIGHTGREEN_EX + '1: Create Order \n\n' + fo.YELLOW + '2: Update Order\n\n' + fo.BLACK + '3: Delete Order \n\n' + fo.RED + '4: Exit\n\n' + fo.YELLOW + 'Choose an action: ' + fo.RESET)
        if action == '1':
            createOrder()
        elif action == '2':
            updateOrder()
        elif action == '3':
            deleteOrder()
        elif action == '4':
            break
