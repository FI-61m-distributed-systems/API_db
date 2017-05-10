import psycopg2
import hashlib
from get_parametra import config

def get_login():
    login= raw_input("login ")
    return login
def get_password():
    password = raw_input("password ")
    h = hashlib.md5(password)
    p = h.hexdigest()
    return p
def get_email():
    email= raw_input("email ")
    return email 
def reg(login, p, email):
    try:
        params = config()
        connect = psycopg2.connect(**params)    
        cursor = connect.cursor()

    except:
        print("no db")

    try:
    
        cursor.execute(
        """INSERT INTO account  ( id,login, password, email, money) VALUES(default, %s , %s, %s,default );""",
        (login, p, email))
        connect.commit()

    except (Exception, psycopg2.Error) as error:
        print(error)        
    finally:
        if connect is not None:
            connect.close()
   
reg(get_login(),get_password(),get_email())
