import psycopg2
from get_parametra import config
from stub import get_login, money,WARNING

def send_money(loginFROM,loginTO, money):
    try:
        params = config()
        connect = psycopg2.connect(**params)            
        cursor = connect.cursor()
    except:
        WARNING()
    try:
        cursor.execute(
        """
        BEGIN;
        UPDATE account
        SET  money=money-%s
        WHERE login=%s;
        UPDATE account
        SET  money=money+%s
        WHERE login=%s;
        """,
        (money,loginFROM,money,loginTO))
        connect.commit()
    except (Exception, psycopg2.Error):
        WARNING()       
    finally:
        if connect is not None:
            connect.close()
   
        
send_money(get_login(),get_login(),money())
