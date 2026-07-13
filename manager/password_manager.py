import ui.menu

def add_account(data):
    site, name, passwd = ui.menu.ask_site(), ui.menu.ask_login(), ui.menu.ask_password()
    data.append({
        'site': site,
        'username': name,
        'password': passwd
    })

def delete_account(data):
    site = ui.menu.ask_site()
    for account in data:
        if account['site'] == site:
            data.remove(account)

def get_all_accounts(data):
    data.sort(key=lambda x: x['site'])
    return data

