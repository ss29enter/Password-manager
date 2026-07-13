import json
from config import PASSWORDS_FILE

def load_data():
    try: 
        with open(PASSWORDS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data(data):
    with open(PASSWORDS_FILE, 'w', encoding='utf-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=0)
