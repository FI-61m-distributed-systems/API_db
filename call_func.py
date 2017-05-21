import json
from stub import send_err
from set_data import set_data
from selection import select
from update import update_data

def call_func(d):
    data=json.loads(d)
    if data["request"]=="get":
        return select(data["id"],data["user"])
    elif data["request"]=="set":
        return set_data(data["transaction"][0]["user"], data["transaction"][0]["password"],
                        data["transaction"][0]["email"])
    elif data["request"]=="update":
        return update_data(data["transaction"][0]["user"],data["transaction"][0]["field"],
                           data["transaction"][0]["value"])
    else:
        send_err("no data")