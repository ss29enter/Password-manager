from config import WIDHT
import os

def print_title():
    print()
    print(f'{"PASSWORD-MANAGER":^{WIDHT}}')
    print('-'*WIDHT,'\n')

def print_actions():
    print(' 1. Add account')
    print(' 2. Edit account')
    print(' 3. Find account')
    print(' 4. Show all accounts')
    print(' 5. Delete account')
    print(' X. EXIT')

def print_sep():
    print()
    print('-'*WIDHT)
    print()

def clear_display():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print_title()
    print_actions()
    print_sep()