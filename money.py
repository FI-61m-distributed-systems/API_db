import psycopg2
from get_parametra import config
def get_login():
    login= raw_input("login ")
    return login

def money():
    money= raw_input("money ")
    return money

def money_in_pocket(loginFROM, moneyFROM,loginTO, moneyTO):
    if moneyFROM == moneyTO:
        try:
            params = config()
            connect = psycopg2.connect(**params)            
            cursor = connect.cursor()
        except:
            print "no db"
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
                (moneyFROM,loginFROM,moneyTO,loginTO))
                connect.commit()
        except (Exception, psycopg2.Error) as error:
            print(error)        
        finally:
            if connect is not None:
                connect.close()
    else:
        print "Wrong money"
        
money_in_pocket(get_login(), money(),get_login(), money())
