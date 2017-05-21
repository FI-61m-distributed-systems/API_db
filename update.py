import psycopg2
from connection import connection
from stub import send_err, send_ok

def update_data(login,field, value):
	
    try:
        connect = connection()	           
        cursor = connect.cursor()
    except:
        send_err(1)
    try:
        cursor.execute(
        """SELECT  login
        FROM account
        where login = %s;
        """,(login,))
        if field=="money":
            cursor.execute(
            """
            UPDATE account
            SET money=%s
            WHERE login=%s;            
            """,
            (value,login))
            connect.commit()
        elif field=="password":
            cursor.execute(
            """
            UPDATE account
            SET password=%s
            WHERE login=%s;            
            """,
            (value,login))
            connect.commit()
        elif field=="email":
            cursor.execute(
            """
            UPDATE account
            SET email=%s
            WHERE login=%s;            
            """,
            (value,login))
            connect.commit()
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)