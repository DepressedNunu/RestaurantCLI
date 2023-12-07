# Import Models

# import Methods

# import CLI
from CLI.Customer import customerAction
from CLI.Meal import mealAction
from CLI.Order import orderAction

# import Styles
from colorama import Fore as fo, Back as bo


def main():
    while True:
        action = input(
            #based on this snippet from CLI/Meal.py:  fo.BLACK + bo.LIGHTGREEN_EX + '1: Create Meal' + bo.RESET + '\n\n' + bo.YELLOW + '2: Update Meal' + bo.RESET + '\n\n' + bo.LIGHTMAGENTA_EX + '3: Delete Meal' + bo.RESET +  '\n\n' + bo.RED + fo.BLACK + '4: Exit' + bo.RESET + '\n\n' + bo.RESET + fo.YELLOW + 'Choose an action: ' + fo.RESET)
            fo.BLACK + bo.LIGHTGREEN_EX + '1: Customer' + bo.RESET + '\n\n' + bo.YELLOW + '2: Meal' + bo.RESET + '\n\n' + bo.LIGHTMAGENTA_EX + '3: Order' + bo.RESET + '\n\n' + bo.RED + fo.BLACK + '4: Exit' + bo.RESET + '\n\n' + bo.RESET + fo.YELLOW + 'Choose an action: ' + fo.RESET)
        if action == '1':
            customerAction()
        elif action == '2':
            mealAction()
        elif action == '3':
            orderAction()
        elif action == '4':
            break


if __name__ == '__main__':
    print(bo.WHITE + fo.BLACK + '*****************' + fo.BLACK + ' WELCOME TO THE RESTAURANT ' + fo.BLACK + '***************' + bo.RESET + "\n")
    main()
