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
def customer(log,p, email):
    try:
        params = config()
        connect = psycopg2.connect(**params)
        cursor = connect.cursor()
    except:
        print("no db")
        
    try:              
        cursor.execute(
        """SELECT id, login, password, email, money
        FROM account
        where login = %s;
        """,(log,) )
        row = cursor.fetchone()
        if row[1] != log:
            print "Wrong login"
        elif row[2]!= p:
            print "Wrong password"
        elif row[3]!= email:
            print "Wrong email"
        else:
            print "Welcome ",log            
        connect.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)        
    finally:
        if connect is not None:
            connect.close()
customer(get_login(),get_password(),get_email())
