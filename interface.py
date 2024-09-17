def welcome():
    print("Welcome to program Systems")

def menu ():
    menu_option = int(input("""=== MAIN MENU ===
1- Calculator
2- Dollar/Real Converter
3- Secret number game
4- To-do list
5- Finalize general program
                             
Select a program: """))
    return menu_option

def thanks():
    print("Thank you for using our programs !")