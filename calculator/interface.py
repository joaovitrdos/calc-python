def welcome ():
    print("""Welcome to Calculator""")

def thanks():
    print("Thank you for using our calculator!")

def value1():
    value1 = float(input("Enter the first value: "))
    return value1

def value2():
    value2 = float(input("Enter the second value: "))
    return value2

def operator ():
    option = (input("""==== Operation ====
Addition: +
Subtraction:-
Multiplication: X
Division:/ 

    Choose your operation:                                                                                                                 
"""))
    return option

def menu ():
    select_menu = int(input("""=== MENU CALCULATOR === 
1- Make another account
2- Change the operation
3- End program
"""))
    return select_menu

if __name__ == "__main__" :
    menu()