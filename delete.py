import psycopg2
from connection import connection
from stub import send_err,send_ok,do_condition
import json

def delete_from_db(conditions):
    try:
        connect = connection()
        cursor = connect.cursor()
    except:
        send_err(1)        
    try:
        cursor.execute(
        """
        DELETE FROM  account        
        WHERE """+do_condition(conditions)+""";            
        """)
        connect.commit()
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)
