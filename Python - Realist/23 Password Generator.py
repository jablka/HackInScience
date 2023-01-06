import random
import string

def pwgen(length, with_digits, with_uppercase):

    letters = string.ascii_lowercase
    password = random.choices(letters, k=length)
    
    if with_digits:
        password.pop()
        digits = string.digits
        password.append(random.choice(digits))
        
    if with_uppercase:
        password[0] = password[0].upper()

    random.shuffle(password)

    p = ''.join(password)

    return p