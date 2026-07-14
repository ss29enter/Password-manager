from ui.menu import print_sep

def ask_site():
    return input('Site: ')

def ask_login():
    return input('Login: ')

def ask_password():
    return input('Password: ')

def display_accounts(data):
    for id, account in enumerate(data,start=1):
        site, _, _ = account.values()
        print(f'{id}. {site}')

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
    if len(data) == 0:
        print('No added account yet.')
    else:
        print(f'{"Login: ":<15}{data["login"]}')
        print(f'{"Password: ":<15}{data["password"]}')

def ask_to_delete(site):
    user = input(f'Delete {site} account? [Y/N] ').lower()
    return 0 if user in ['n','no'] else 1

def ask_action():
    return input(': ')