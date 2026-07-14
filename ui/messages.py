def ask_site():
    return input('Site: ')

def ask_login():
    return input('Login: ')

def ask_password():
    return input('Password: ')

def display_accounts(data):
    for num, account in enumerate(data,start=1):
        site, _, _ = account.values()
        print(f'{num}. {site}')

def ask_what_to_change():
    user = input('Edit login or password? [L/P] ').lower()
    while True:
        if user == 'l':
            return 'login', input('New login: ')
        elif user == 'p':
            return 'password', input('New password: ')
        else:
            user = input('Incorrect data. Enter [L/P] ').lower()

def show_account(data):
    print()
    print('Site:'); print(data['site'])
    print('Login:'); print(data['login'])
    print('Password:'); print(data['password'])