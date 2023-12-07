from colorama import Fore as fo


def dataVerification(*args):
    for arg in args:
        if arg is None or arg == '':
            print(fo.RED + '\n Invalid Type' + str(arg) + "\n" + fo.RESET)
            return False
    return True


def dataInput():
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    phone = input("Enter phone: ")
    if dataVerification(name, surname, phone):
        return name, surname, phone
    return None, None, None
