def ask_password():
    string = 'password'
    tries = 3 
    while tries != 0:
        passworld = input('enter passworld')
        if passworld == string:
            print('пароль принят')
            break
        else:
            print("неправильно")
            tries -= 1
    if tries == 0:
        print('незя')
ask_password()


x = int(input('x: '))
y = int(input('y: '))

def check_part(x, y):
    if x > 0 and y > 0:
        print('I')
    elif x < 0 and y > 0:
        print('II')
    elif x < 0 and y < 0:
        print('III')
    else:
        print('IV')
check_part(x, y)