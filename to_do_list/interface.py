def welcome():
    print("Welcome to the to-do list")

def thanks():
    print("Thank you for using our to-do list system!")

def select_menu():
    option_menu = int(input("""=== MENU ===
1- Add task                            
2- Show list
3- Withdraw task
4- Reset list                            
5- Finalize program
Select: """))
    return option_menu

def add_task ():
    task = str(input("Enter the task you want to add to your list: "))
    return task

def show_list(list):
    print("--- LIST ---")
    if list == []:
        print ('You didnt add an item to your LIST !!!')
    else:
        for i in range (len(list)):
            print(f"{i+1}- {list[i]}")

def remove_task():
    remove = int(input("Enter the number of the task you want to withdraw: "))
    return remove