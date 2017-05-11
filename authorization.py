import psycopg2
import hashlib
from get_parametra import config
from stub import get_login,get_password,get_email,WARNING,OK 

def add_customer(log,p, email):
    try:
        params = config()
        connect = psycopg2.connect(**params)
        cursor = connect.cursor()
    except:
        WARNING()        
    try:              
        cursor.execute(
        """SELECT id, login, password, email, money
        FROM account
        where login = %s;
        """,(log,) )
        row = cursor.fetchone()
        if row[1] != log:
            WARNING()
        elif row[2]!= p:
            WARNING()
        elif row[3]!= email:
            WARNING()
        else:
            OK()           
        connect.commit()
    except (Exception, psycopg2.Error):
        WARNING()       
    finally:
        if connect is not None:
            connect.close()
            
add_customer(get_login(),get_password(),get_email())
