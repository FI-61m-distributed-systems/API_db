import psycopg2
from stub import send_err, send_ok,do_condition

def update_data(condits,field,value,cursor):
    dictionary={"user": "login", "password": "password", "email": "email",
                "money":"money","game":"game_config"}
    try:
        cursor.execute(
        """
        UPDATE account
        SET """+ dictionary[field]+"""=%s
        WHERE """+do_condition(condits)+""";            
        """,
        (value,))
        #connect.commit()
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)