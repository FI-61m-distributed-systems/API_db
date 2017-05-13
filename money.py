import psycopg2
from connection import connection
from stub import send_err

def send_money(loginFROM,loginTO, money):
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
        """,(loginFROM,) )
        row = cursor.fetchone()       
        if row[0] != loginFROM:
            send_err(loginFROM)
        else:
            cursor.execute(
            """SELECT  login
            FROM account
            where login = %s;
            """,(loginTO,) )
            row2 = cursor.fetchone()
            if row2[0] != loginTO:
                send_err(loginTO)
            else:                    
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
    except (Exception, psycopg2.Error) as err:
        send_err(err)