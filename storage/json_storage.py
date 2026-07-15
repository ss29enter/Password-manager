import json
from config import PASSWORDS_FILE, MASTER_PASSWORD_FILE, SALT_FILE


def load_data():
    try: 
        with open(PASSWORDS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(PASSWORDS_FILE, 'w', encoding='utf-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=0)

def load_master():
    try:
        with open(MASTER_PASSWORD_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_master(hash):
    with open(MASTER_PASSWORD_FILE, 'w', encoding='utf-8') as file:
        return json.dump(hash,file,indent=4,ensure_ascii=0)
    
def load_salt():
    with open(SALT_FILE,'rb') as file:
        return file.read()

def save_salt(salt):
    with open(SALT_FILE, 'wb') as file:
        return file.write(salt)
