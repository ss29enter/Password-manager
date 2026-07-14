from ui.menu import print_sep

def ask_site():
    user = input('Site:\n> ')
    if user == '':
        print(display_error('empty'))
        return ask_site()
    return user

def ask_login():
    user = input('Login:\n> ')
    if user == '':
        print(display_error('empty'))
        return ask_login()
    return user

def ask_password():
    user = input('Password:\n> ')
    if user == '':
        print(display_error('empty'))
        return ask_password()
    return user

def display_accounts(data):
    if data == []:
        return print(display_error('no_accounts'))
    for id, account in enumerate(data,start=1):
        site, _, _ = account.values()
        print(f'{id}. {site}')

def ask_what_to_change():
    user = input('Edit login or password? [L/P] \n> ').lower()
    while True:
        if user == 'l':
            return 'login', input('New login: ')
        elif user == 'p':
            return 'password', input('New password: ')
        elif user == '':
            print(display_error('empty'))
            return ask_what_to_change()
        else:
            print(display_error('incorrect'))
            return ask_what_to_change()

def show_account(data):
    if data:
        for item in data:
            print(f'> {item["site"]}')
            print(f'{"Login: ":<15}{item["login"]}')
            print(f'{"Password: ":<15}{item["password"]}\n')

def ask_to_delete(site):
    user = input(f'Delete {site} account? [Y/N] ').lower()
    return 0 if user in ['n','no'] else 1

def ask_action():
    return input(': ')

def display_error(opt):
    errors = {

        'exist': 'Account is already exist.',
        'empty': 'Empty line.',
        'no_accounts': 'No added accounts yet.',
        'incorrect': 'Incorrect output.',
        'not_found': 'No coincidences.'
    }
    return errors[opt]