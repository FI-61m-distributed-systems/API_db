import psycopg2
from connection import connection
from stub import send_err, send_ok,do_condition

def update_data(condits,field,value):
    dictionary={"user": "login", "password": "password", "email": "email",
                "money":"money","game":"game_config"}
    try:
        connect = connection()	           
        cursor = connect.cursor()
    except:
        send_err(1)
    try:
        cursor.execute(
        """
        UPDATE account
        SET """+ dictionary[field]+"""=%s
        WHERE """+do_condition(condits)+""";            
        """,
        (value,))
        connect.commit()
        return send_ok(1)
    except (Exception, psycopg2.Error) as err:
        return send_err(err)
##data={
##    "type": "update",
##    "transaction":
##    [
##       {
##          "action": "insert",
##          "login": "bbb",
##          "password": "vvv",
##          "email": "x@w"         
##       },
####      {
####          "action": "delete",
####          "conditions": [["user", "=", "c"]]
####       },
##       {
##          "action": "update",
##          "field": "money",
##          "value": 105,
##          "conditions": [["user", "=", "vika"]]
##       }
##    ]
## }
##print   do_condition(data["transaction"][1]["conditions"])
##print update_data(data["transaction"][1]["conditions"],data["transaction"][1]["field"],
##                              data["transaction"][1]["value"])
