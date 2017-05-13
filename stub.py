import hashlib

def get_login():
    login= raw_input("login ")
    return login

def money():
    money= raw_input("money ")
    return money

def send_ok(data):
    print "Welcom ", data

def send_err(data):
    print "ERROR ", data

def get_password():
    password = raw_input("password ")
    h = hashlib.md5(password)
    p = h.hexdigest()
    return p

def get_email():
    email= raw_input("email ")
    return email 