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
    show_account
)


def main():
    data = load_data()
    show_account(find_account(data))
    save_data(data)

if __name__ == '__main__':
    main()


