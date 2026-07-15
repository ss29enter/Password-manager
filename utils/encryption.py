import hashlib
from config import MASTER_PASSWORD_FILE
from storage.json_storage import save_master, load_master
import ui.messages


def hash_password(password):
    h = hashlib.sha256()
    h.update(password.encode())
    return h.hexdigest()

def set_master():
    master = hash_password(ui.messages.set_password())
    save_master({'master-key': master})

def check_password():
    user = hash_password(ui.messages.ask_password())
    master = load_master()['master-key']
    return user == master




