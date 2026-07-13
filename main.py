from storage.json_storage import load_data, save_data
from manager.password_manager import (
    add_account,
    delete_account,
    get_all_accounts
)
from ui.menu import display_accounts



def main():
    data = load_data()

if __name__ == '__main__':
    main()


