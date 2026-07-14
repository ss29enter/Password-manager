from storage.json_storage import load_data, save_data
from manager.password_manager import (
    add_account,
    delete_account,
    get_all_accounts,
    find_account,
    edit_account
)
from ui.messages import (
    display_accounts, 
    show_account,
    ask_action
)
from ui.menu import display_menu, clear_display


def main():
    data = load_data()
    display_menu()
    while True:
        user = ask_action().lower()
        clear_display()
        display_menu()
        if user == '1':
            add_account(data)
            save_data(data)

        if user == '2':
            edit_account(data)
            save_data(data)

        if user == '3':
            show_account(find_account(data))

        if user == '4':
            display_accounts(get_all_accounts(data))

        if user == '5':
            delete_account(data)
            save_data(data)
   
        if user in ['x','exit']:
            break   

if __name__ == '__main__':
    main()


