import secrets
import random
from string import (
    ascii_uppercase as up, 
    ascii_lowercase as low,
    digits as dig,
    punctuation as sym
)


def generate_password(length, upper, lower, digits, symbols):
    chars, password = '', []
    if upper not in ['n','no']:
        chars += up
        password.append(secrets.choice(up))
    if lower not in ['n','no']:
        chars += low
        password.append(secrets.choice(low))
    if digits not in ['n','no']:
        chars += dig
        password.append(secrets.choice(dig))
    if symbols not in ['n','no']:
        chars += sym
        password.append(secrets.choice(sym))
    
    password += [secrets.choice(chars) for _ in range(length-len(password))]
    random.shuffle(password)
    return ''.join(password)






        
        
