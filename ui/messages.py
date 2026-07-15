from config import WIDHT


def ask_site():
    user = input('Site: ')
    if user == '':
        print(display_error('empty'))
        return ask_site()
    return user

def ask_login():
    user = input('Login: ')
    if user == '':
        print(display_error('empty'))
        return ask_login()
    return user

def ask_password():
    user = input('Password: ')
    if user == '':
        print(display_error('empty'))
        return ask_password()
    return user

def display_accounts(data):
    if data == []:
        return print('\n' + display_error('no_accounts'))
    print(f'{"ACCOUNTS":^{WIDHT}}\n')
    print(f'> {len(data)} accounts found:')
    for item in data:
        site, _, _ = item.values()
        print(f'- {site}')
    print()

def ask_what_to_change():
    user = input('> Edit login or password? [L/P] ').lower()
    print()
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
    print()
    if data:
        for item in data:
            print(f'> {item["site"]}')
            print(f'{"Login: ":<15}{item["login"]}')
            print(f'{"Password: ":<15}{item["password"]}\n')
    else:
        return print(display_error('not_found'))
    
def ask_to_delete(site):
    print()
    user = input(f'> Delete {site} account? [Y/N] ').lower()
    return 0 if user in ['n','no'] else 1

def ask_action():
    return input(': ')

def display_error(opt):
    errors = {

        'exist': '> Account is already exist',
        'empty': '> Empty line',
        'no_accounts': '> No added accounts yet',
        'incorrect': '> No account',
        'not_found': '> No coincidences',
        'wrong_pas': '> Wrong password'
    }
    return errors[opt]

def set_password():
    return input('Set the master-key: ')

def ask_password():
    return input('Enter password: ')
