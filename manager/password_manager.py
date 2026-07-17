import ui.messages  


def add_account(data):
    site = ui.messages.ask_site()
    for item in data:
        if site == item['site']:
            return print(ui.messages.display_error('exist'))
    login, passwd = (

        ui.messages.ask_login(), 
        ui.messages.ask_password()
    )
    data.append({

        'site': site,
        'login': login,
        'password': passwd
    })
    print(ui.messages.display_allow('add').format(site))

def delete_account(data):
    site = ui.messages.ask_site()
    res = []
    for item in data:
        if site in item['site']:
            if ui.messages.ask_to_delete(item['site']):
                res.append(item)
    if res == []: 
        return print(ui.messages.display_error('deletion'))
    print(ui.messages.display_allow('deletion').format(len(res)))
    for el in res: data.remove(el)

def get_all_accounts(data):
    data.sort(key=lambda x: x['site'])
    return data

def edit_account(data):
    site = ui.messages.ask_site()
    flag = True
    for item in data:
        if site == item['site']:
            flag = False
    if flag: 
        return print(ui.messages.display_error('incorrect'))
    
    info, new_info = ui.messages.ask_what_to_change()
    for item in data:
        if item['site'] == site:
            item[info] = new_info
            print(ui.messages.display_allow('editing').format(info.title(),site))
            break

def find_account(data):
    res = []
    site = ui.messages.ask_site()
    for item in data:
        if site in item['site']:
            res.append(item)
    return res   