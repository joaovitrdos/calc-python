def welcome():
    print("Welcome to converter Real/Dollar")

def thanks():
    print("Thank you for using our value converter")

def return_cot():
    cot = float(input("Enter the current Dollar rate: "))
    return cot

def option_convert():
    print("""==== Conversion ====
1- Dollar to Real
2- Real to Dollar""")
    convert= int(input("Conversion (1 or 2):"))
    return convert

def select_value():
    value = float(input("Enter the amount: "))
    return value

def select_menu():
    menu = int(input("""
=== MENU CONVERTER ===
1- Convert another value
2- Change the type of conversion
3- Finish the program                    

Select an option from the menu: """))
    return menu

if __name__ == "__main__":
    welcome()
    return_cot()
    option_convert()
    select_value()
    select_menu()