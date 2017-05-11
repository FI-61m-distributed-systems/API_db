import psycopg2
import hashlib
from get_parametra import config
from stub import get_login,get_password,get_email, WARNING

def reg(login, password, email):
    try:
        params = config()
        connect = psycopg2.connect(**params)    
        cursor = connect.cursor()
    except:
        WARNING()
    try:    
        cursor.execute(
        """INSERT INTO account  ( id,login, password, email, money) VALUES(default, %s , %s, %s,default );""",
        (login, password, email))
        connect.commit()
    except (Exception, psycopg2.Error):
        WARNING()        
    finally:
        if connect is not None:
            connect.close()
   
reg(get_login(),get_password(),get_email())
