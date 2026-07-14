import ui.messages  

def add_account(data):
    site, login, passwd = (

        ui.messages.ask_site(),
        ui.messages.ask_login(), 
        ui.messages.ask_password()
    )
    data.append({

        'site': site,
        'login': login,
        'password': passwd
    })

def delete_account(data):
    site = ui.messages.ask_site()
    for account in data:
        if site in account['site']:
            if ui.messages.ask_to_delete(account['site']):
                data.remove(account) 
            else: pass

def get_all_accounts(data):
    data.sort(key=lambda x: x['site'])
    return data

def edit_account(data):
    site = ui.messages.ask_site()
    info, new_info = ui.messages.ask_what_to_change()
    for item in data:
        if item['site'] == site:
            item[info] = new_info
            break

def find_account(data):
    res = []
    site = ui.messages.ask_site()
    for item in data:
        if site in item['site']:
            res.append(item)
    return res


