from storage.json_storage import load_data, save_data
from manager.password_manager import (
    add_account,
    delete_account,
    get_all_accounts,
    find_account,
    edit_account
)
import ui.messages, ui.menu


def main():
    data = load_data()
    ui.menu.display_menu()
    while True:
        user = ui.messages.ask_action().lower()
        ui.menu.clear_display()
        ui.menu.display_menu()
        if user == '1':
            add_account(data)
            save_data(data)

        if user == '2':
            edit_account(data)
            save_data(data)

        if user == '3':
            ui.messages.show_account(find_account(data))

        if user == '4':
            ui.messages.display_accounts(get_all_accounts(data))

        if user == '5':
            delete_account(data)
            save_data(data)
   
        if user in ['x','exit']:
            ui.menu.clear_display()
            break   

if __name__ == '__main__':
    main()


