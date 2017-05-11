import psycopg2
from get_parametra import config
 
def connect():    
    conn = None
    try:      
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(
        """        
        CREATE TABLE account
        (
          id serial NOT NULL,
          "login" character varying(50) NOT NULL,
          "password" character varying(50) NOT NULL,
          email character varying(50) NOT NULL,
          money integer DEFAULT 0,
          CONSTRAINT account_pkey PRIMARY KEY (id),
          CONSTRAINT account_login_key UNIQUE (login)
        )
        WITH (
          OIDS=FALSE
        );
        ALTER TABLE account OWNER TO postgres;
        """)
        conn.commit() 
        cur.close()
    except (Exception, psycopg2.Error) as error:
        print(error)        
    finally:
        if conn is not None:
            conn.close()
             
if __name__ == '__main__':
    connect()
