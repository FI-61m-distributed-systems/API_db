import psycopg2
import hashlib
from connection import connection
from stub import send_err,send_ok 

def authorization_customer(log,p, email):
    try:
        connect = connection()
        cursor = connect.cursor()
    except:
        send_err(1)        
    try:              
        cursor.execute(
        """SELECT id, login, password, email, money
        FROM account
        where login = %s;
        """,(log,) )
        row = cursor.fetchone()
        if row[1] != log:
            send_err("login")
        elif row[2]!= p:
            send_err("password")
        elif row[3]!= email:
            send_err("email")
        else:
            send_ok(log)           
        connect.commit()		
    except (Exception, psycopg2.Error) as err:
        send_err(err)