from .interface import *
from .calc import *

def converter ():
    # valores iniciais para comecar o while
    return_menu = True
    new_convert = True
    new_value = True

    welcome()
    # cotacão digitada pelo usuário
    price = return_cot()

    while return_menu == True:
        if new_convert == True :
            convert = option_convert()
            new_convert = False
        if new_value == True:
            value = select_value()
        match convert:
            case 1:
                doll_to_real(value,price)
            case 2:
                real_to_doll(value, price)
        menu = select_menu()
        match menu:
            case 1:
                new_value = True
            case 2:
                new_convert = True
                new_value = True
            case 3:
                return_menu = False
                thanks()



