import psycopg2
from connection import connection
from stub import send_err

def reg(login, password, email):
    try:
        connect = connection()    
        cursor = connect.cursor()
    except:
        send_err(1)
    try:    
        cursor.execute(
        """INSERT INTO account  ( id,login, password, email, money) VALUES(default, %s , %s, %s,default );""",
        (login, password, email))
        connect.commit()		
    except (Exception, psycopg2.Error) as err:
        send_err(err) 