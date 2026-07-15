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
        key = ui.messages.ask_password()
        if not security.check_password(key):
            return
        
    data = load_data()
    ui.menu.display_menu()
    while True:
        user = ui.messages.ask_action().lower()
        ui.menu.clear_display()
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
            if security.check_hash(ui.messages.ask_password()):
                security.set_master()
                return

        if user in ['x','exit']:
            ui.menu.clear_display()
            security.encryption(key)
            break   


if __name__ == '__main__':
    main()


