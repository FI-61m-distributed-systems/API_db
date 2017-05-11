def get_login():
    login= raw_input("login ")
    return login

def money():
    money= raw_input("money ")
    return money

def OK():
    return 1

def WARNING():
    return 0

def get_password():
    password = raw_input("password ")
    h = hashlib.md5(password)
    p = h.hexdigest()
    return p

def get_email():
    email= raw_input("email ")
    return email 



