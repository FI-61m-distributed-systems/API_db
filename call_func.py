import json
from stub import send_err,send_ok
from set_data import set_data
from selection import select
from update import update_data
from delete import delete_from_db

def set_json(js):
    data=json.loads(js)
    i=0
    answer=0
    if data["type"]=="get":
        return select(data["fields"],data["conditions"])
    elif data["type"]=="update":
        for i in range(0,len(data["transaction"]),1):
            if data["transaction"][i]["action"]=="insert":
                s=set_data(data["transaction"][i]["user"],
                           data["transaction"][i]["password"],data["transaction"][i]["email"])
                if s==200:
                    answer=answer+1
            elif data["transaction"][i]["action"]=="update":
               u=update_data(data["transaction"][i]["conditions"],data["transaction"][i]["field"],
                               data["transaction"][i]["value"])
               if u==200:
                    answer=answer+1
            elif data["transaction"][i]["action"]=="delete":
               d=delete_from_db(data["transaction"][i]["conditions"])
               if d==200:
                    answer=answer+1
        print "Correct transaction: ",answer
        if answer==len(data["transaction"]):
            return send_ok(answer)
        else:
            return send_err("no data")        
    else:
        return send_err("no data")
