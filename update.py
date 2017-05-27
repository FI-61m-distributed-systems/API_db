import psycopg2
from connection import connection
from stub import send_err, send_ok

def update_data(login,field,value):
    dictionary={"login": "login", "password": "password", "email": "email",
                "money":"money","game":"game_config"}
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
        cursor.execute(
        """
        UPDATE account
        SET """+ dictionary[field]+"""=%s
        WHERE login=%s;            
        """,
        (value,login))
        connect.commit()
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)
