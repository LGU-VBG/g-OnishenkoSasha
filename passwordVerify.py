import re



def passwordVerify():
    password = input() 
    if (re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[0-9]', password) and re.search(r'[^a-z^A-Z^0-9]', password)):
        print('формат пароля верный')
    else:
        print('неверный формат пароляы')


print('введите пароль')
passwordVerify()