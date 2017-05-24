import psycopg2
import hashlib
from connection import connection
from stub import send_err,send_ok
import json

def select(id_t,log):
    try:
        connect = connection()
        cursor = connect.cursor()
    except:
        send_err(1)        
    try:              
        cursor.execute(
        """SELECT login, password, email, money, game_config
        FROM account
        where login = %s;
        """,(log,))
        row = cursor.fetchone()
        data = {
            "id": id_t,            
            "fields": 
                [
                    {
                     "password": row[1],
                     "email": row[2],
                     "money": row[3],
					 "game_config":row[4]
                    }
                ]
            }              
        connect.commit()
        t= json.dumps(data)
        return t
    except (Exception, psycopg2.Error) as err:
        send_err(err)