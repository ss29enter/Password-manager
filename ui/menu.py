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