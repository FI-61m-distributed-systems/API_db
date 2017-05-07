import psycopg2
def get_login():
    login= raw_input("login ")
    return login
def money():
    money= raw_input("money ")
    return money

def money_in_pocket(login, money):
    try:
        
        connect = psycopg2.connect(database='Game_Webmoney', user='postgres', host='localhost', password='medvedka123',port = '5433')
        cursor = connect.cursor()

    except:
        print("no db")

    try:
            cursor.execute(
                """
            
            UPDATE account
            SET  money=money+%s
            WHERE login=%s;""",
                (money,login,)    )
            connect.commit()
    except psycopg2.Error:
        try: 
            
            connect.rollback()
            print ("Your data is not correct")
            connect.close()

        except:
            connect.close()        
            print ("Your data is not written")
            
    connect.close()
money_in_pocket(get_login(), money())
