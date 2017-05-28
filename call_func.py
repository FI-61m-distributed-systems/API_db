import json
from stub import send_err,send_ok
from set_data import set_data
from selection import select
from update import update_data
from delete import delete_from_db
from connection import connection

def set_json(js):
    connect = connection()	           
    cursor = connect.cursor()
    data=json.loads(js)
    i=0
    answer=0
    if data["type"]=="get":
        return select(data["fields"],data["conditions"])
    elif data["type"]=="update":
        for i in range(0,len(data["transaction"]),1):
            if data["transaction"][i]["action"]=="insert":
                s=set_data(data["transaction"][i]["user"],
                           data["transaction"][i]["password"],data["transaction"][i]["email"],cursor)
                if s==200:
                    answer=answer+1
            elif data["transaction"][i]["action"]=="update":
               u=update_data(data["transaction"][i]["conditions"],data["transaction"][i]["field"],
                               data["transaction"][i]["value"],cursor)
               if u==200:
                    answer=answer+1
            elif data["transaction"][i]["action"]=="delete":
               d=delete_from_db(data["transaction"][i]["conditions"],cursor)
               if d==200:
                    answer=answer+1
        print "Correct transaction: ",answer, " of ",len(data["transaction"])
        if answer==len(data["transaction"]):
            connect.commit()
            return send_ok(answer)
        else:
            connect.rollback()
            return send_err("no transaction")        
    else:
        return send_err("no data")
