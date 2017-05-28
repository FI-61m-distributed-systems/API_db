import psycopg2
from stub import send_err,send_ok,do_condition

def delete_from_db(conditions,cursor):
       
    try:
        cursor.execute(
        """
        DELETE FROM  account        
        WHERE """+do_condition(conditions)+""";            
        """)        
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)