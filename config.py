import pathlib


BASE_DIR = pathlib.Path(__file__).parent
DATA_DIR = BASE_DIR / 'data'
PASSWORDS_FILE = DATA_DIR / 'passwords.json'
MASTER_PASSWORD_FILE = DATA_DIR / 'master_password.json'

WIDHT = 45