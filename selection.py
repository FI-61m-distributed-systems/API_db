import psycopg2
from connection import connection
from stub import send_err,send_ok,do_condition,set_fields
import json

def select(fields,conditions):
    try:
        connect = connection()
        cursor = connect.cursor()
    except:
        send_err(1)        
    try:              
        cursor.execute(
        """SELECT """+set_fields(fields) +
        """ FROM account
        where """ +do_condition(conditions)+""";
        """)
        rows = cursor.fetchall()       
        value=[]
        for row in range(0,len(rows),1):
            dictt={}
            for i in range(0,len(rows[row]),1):                
                dictt[fields[i]]=rows[row][i]
            value.append(dictt)        
        data = {"values":value}
        connect.commit()
        t= json.dumps(data)
        return t
    except (Exception, psycopg2.Error) as err:
        return send_err(err)
