import utils.encryption
from getpass import getpass
from utils.password_generator import generate_password
from ui.menu import display_menu, display_name


def ask_site():
    user = input('Site: ')
    display_menu()
    if user == '':
        print(display_error('empty'))
        return ask_site()
    return user

def ask_login():
    user = input('Login: ')
    display_menu()
    if user == '':
        print(display_error('empty'))
        return ask_login()
    return user

def ask_password():
    if input('Generate a password? [Y/N] ').lower() in ['no','n']:
        display_menu()
        user = getpass('Password: ')
        if user == '':
            print(display_error('empty'))
            return ask_password()
        display_menu()
        return user
    else:
        return ask_options()
        
def display_accounts(data):
    if data == []:
        return print(display_error('no_accounts'))
    print(display_name('acc').format(len(data)))
    for item in data:
        site, _, _ = item.values()
        print(f'- {site}')

def ask_what_to_change():
    user = input('Edit login or password? [L/P] ').lower()
    display_menu()
    while True:
        if user == 'l':
            login = input('New login: ')
            display_menu()
            if login == '': return print(display_error('empty'))
            return 'login', login
        elif user == 'p':
            if input('Generate a password? [Y/N] ').lower() in ['no','n']:
                display_menu()
                passwd = getpass('New password: ')
                display_menu()
                if passwd == '': return print(display_error('empty'))
                return 'password', passwd
            else: 
                return 'password', ask_options()
        elif user == '':
            print(display_error('empty'))
            return ask_what_to_change()
        else:
            print(display_error('incorrect'))
            return ask_what_to_change()

def show_account(data):
    print(display_name('res').format(len(data)))
    if data:
        for item in data:
            print(f'> {item["site"]}')
            print(f'{"Login: ":<15}{item["login"]}')
            print(f'{"Password: ":<15}{'*'*len(item["password"])}\n')
    else:
        return print(display_error('not_found'))
    ask = input('Show passwords? [Y/N] ').lower()
    if not ask in ['n','no']:
        if utils.encryption.check_hash(ask_master()):
            display_menu()
            print(display_name('res').format(len(data)))
            for item in data:
                print(f'> {item["site"]}')
                print(f'{"Login: ":<15}{item["login"]}')
                print(f'{"Password: ":<15}{item["password"]}\n')
        else: 
            display_menu()
            return print(display_error('wrong_pas'))
    else: display_menu()
    
def ask_to_delete(site):
    user = input(f'Delete {site} account? [Y/N] ').lower()
    display_menu()
    return 0 if user in ['n','no'] else 1

def ask_action():
    return input(': ')

def display_error(opt):
    errors = {

        'exist': '> Account is already exist',
        'empty': '> Empty line',
        'no_accounts': '> No added accounts yet',
        'incorrect': '> No account',
        'deletion': '> There are no accounts to delete',
        'not_found': '> No coincidences',
        'wrong_pas': '> Wrong password'
    }
    return errors[opt]

def display_allow(opt):
    allows = {

        'decrypt': '> File is successfully decrypted! [enter]',
        'encrypt': '> File is successfully encrypted!',
        'deletion': '> {} accounts is deleted',
        'editing': '> {} ({}) is edited',
        'add': '> {} account is added'
    }
    return allows[opt]

def set_password():
    return getpass('Set the master-key: ')
   
def ask_master():
    return getpass('Enter password: ')

def ask_options():
    display_menu()
    length = input('Length: ')
    if length == '' or not length.isdigit() : length = 8
    upper = input('Include uppercase? [Y/N] ').lower()
    lower = input('Include lowercase? [Y/N] ').lower()
    dig = input('Include digits? [Y/N] ').lower()
    symbols = input('Include symbols? [Y/N] ').lower()
    display_menu()
    return generate_password(int(length), upper, lower, dig, symbols)
