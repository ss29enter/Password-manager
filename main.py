from storage.json_storage import (
    load_data, 
    save_data, 
    load_master
)
import utils.encryption as security
import manager.password_manager as manager
import ui.messages, ui.menu


def main():
    if not load_master():
        save_data(load_data())
        security.set_master()
        return
    else: 
        key = ui.messages.ask_master()
        if not security.check_password(key):
            return
        
    data = load_data()
    while True:
        user = ui.messages.ask_action().lower()
        ui.menu.display_menu()

        if user == '1':
            manager.add_account(data)
            save_data(data)

        if user == '2':
            manager.edit_account(data)
            save_data(data)

        if user == '3':
            ui.messages.show_account(manager.find_account(data))

        if user == '4':
            ui.messages.display_accounts(manager.get_all_accounts(data))

        if user == '5':
            manager.delete_account(data)
            save_data(data)
   
        if user == 'r':
            if security.check_hash(ui.messages.ask_master()):
                ui.menu.display_menu()
                security.set_master()
                return
            ui.menu.display_menu()
            print(ui.messages.display_error('wrong_pas'))

        if user in ['x','exit']:
            ui.menu.clear_display()
            security.encryption(key)
            print(ui.messages.display_allow('encrypt'))
            break   


if __name__ == '__main__':
    main()


