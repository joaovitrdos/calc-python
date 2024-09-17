def calc (v1, v2, option):
    match option:
        case '-' | 'subtrction':
            print(f"the subtraction of {v1} - {v2} = {v1-v2} ")
        case '+' | 'addition':
            print(f"The addition of {v1} + {v2} = {v1+v2} ")
        case 'X' | 'x' | 'multiplication':
            print(f"The multiplication of {v1} - {v2} = {v1*v2} ")
        case '/' | 'division':
            print(f"The division of {v1} / {v2} = {v1/v2} ")