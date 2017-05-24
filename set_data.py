import psycopg2
from connection import connection
from stub import send_err,send_ok

def set_data(login, password, email):
    try:
        connect = connection()    
        cursor = connect.cursor()
    except:
        return send_err(1)
    try:    
        cursor.execute(
        """INSERT INTO account  (id,login, password, email, money,game_config)
        VALUES(default, %s , %s, %s,default,default);""",
        (login, password, email))
        connect.commit()
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)