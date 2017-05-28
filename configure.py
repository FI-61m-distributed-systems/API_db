import psycopg2
from connection import connection
from stub import send_err
import sys, getopt

def main(argv):
   host = ''
   password = ''
   port= ''
   f = open('conf.ini', 'w')
   f.write('[postgresql]' + '\n'+'user=postgres'+ '\n'+'database=postgres'+'\n')
   try:
      opts, args = getopt.getopt(argv,"hs:p:l:",["host=","password=","port="])
   except getopt.GetoptError:
      print 'python configure.py -s <host> -p <password> -l <port>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'python configure.py -s <host> -p <password> -l <port>'
         sys.exit()
      elif opt in ("-s", "--host"):
         host = arg
      elif opt in ("-p", "--password"):
         password = arg
      elif opt in ("-l", "--port"):
         port = arg
   f.write('host='+host+'\n'+'password='+ password+ '\n'+'port ='+port)
   f.close()
   print "Create ini"

def changeDB_ini():   
   try:
      fi = open('conf.ini', 'r') 
      text = fi.read()
      fi.close()
      f = open('conf.ini', 'w')
      f.write(text.replace('database=postgres', 'database=Game_Webmoney'))
      f.close()
      print "change ini"
   except:
      print "ERROR ini didn't change"
      
def create_db():        
        conn = None
        try:
                connect = connection()
                connect.autocommit = True
                cur = connect.cursor()
                cur.execute(
                """        
                CREATE DATABASE "Game_Webmoney"
                WITH OWNER = postgres
                ENCODING = 'UTF8'
                TABLESPACE = pg_default
                LC_COLLATE = 'Russian_Russia.1251'
                LC_CTYPE = 'Russian_Russia.1251'
                CONNECTION LIMIT = -1;
                """) 
                cur.close()
                connect.close()
                print "Create DB"
        except (Exception, psycopg2.Error) as error:
                send_err(error)

def create_table():    
        conn = None
        try:
                connect = connection()
                cur = connect.cursor()
                cur.execute(
                """        
                CREATE TABLE account
                (
                  id serial NOT NULL,
                  "login" character varying(50) NOT NULL,
                  "password" character varying(50) NOT NULL,
                  email character varying(50) NOT NULL,
                  money integer DEFAULT 0,
                  game_config text ,
                  CONSTRAINT account_pkey PRIMARY KEY (id),
                  CONSTRAINT account_login_key UNIQUE (login),
                  CONSTRAINT CHK_money CHECK (money>=0)
                )
                WITH (
                  OIDS=FALSE
                );
                ALTER TABLE account OWNER TO postgres;
                """)
                connect.commit() 
                cur.close()
                connect.close()
                print "Create table"
        except (Exception, psycopg2.Error) as error:
                send_err(error)        
   
if __name__ == "__main__":
   main(sys.argv[1:])
   create_db()
   changeDB_ini()
   create_table()
