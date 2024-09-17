def welcome():
    print("=== Welcome to the secret number game ===")

def thanks():
    print("Thank you for using our secret number game !")

def introduction():
    print("In this game the computer will generate a random number between 0 and 100. You have to guess what value was generated:")

def first_attempt ():
    attempt = int(input("Take your first kick: "))
    return attempt

def number_bigger():
    attempt = int(input("""His shot was high. Try again
Enter another value: """))
    return attempt

def number_small():
    attempt = int(input("""His shot was low. Try again
Enter another value: """))
    return attempt

def congratulations(number, attempts):
    print (f"Congratulations, you got the number {number} right in {attempts} attempts")

def play_again ():
    again = str(input("Want to play again ? (s/n)")).upper()
    match again:
        case 'S':
            return True
        case 'N':
            return False
