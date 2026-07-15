import cryptography
import hashlib
from config import PASSWORDS_FILE
from storage.json_storage import (
    save_master,
    load_master,
    load_salt,
    save_salt                           
)
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import base64 
import secrets
import ui.messages


def hash_password(password):
    h = hashlib.sha256()
    h.update(password.encode())
    return h.hexdigest()

def set_master():
    user = ui.messages.set_password()
    master = hash_password(user)
    salt = generate_salt()
    save_master({'master-key': master})  
    encryption(user)
    print(ui.messages.display_allow('encrypt'))
    
def generate_salt():
    salt = secrets.token_bytes(16)
    save_salt(salt)

def generate_key(password):
    salt = load_salt()
    kdf = Scrypt(salt, length=32, n=2**14, r=8, p=1)
    derived_key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(derived_key)

def encryption(user,filename=PASSWORDS_FILE):
    key = generate_key(user)
    cipher = Fernet(key)
    with open(filename, 'rb') as file:
        data = file.read()

    encrypted_data = cipher.encrypt(data)
    with open(filename,'wb') as file:
        file.write(encrypted_data)

def decryption(key,filename=PASSWORDS_FILE):
    cipher = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except cryptography.fernet.InvalidToken:
        print(ui.messages.display_error('wrong_pas'))
        return False
    
    with open(filename,'wb') as file:
        file.write(decrypted_data)

    print(ui.messages.display_allow('decrypt'))
    return True

def check_password(user):
    key = generate_key(user)
    if check_hash(user):
        return decryption(key)
    decryption(key)

def check_hash(user):
    master = load_master()['master-key']
    return hash_password(user) == master






