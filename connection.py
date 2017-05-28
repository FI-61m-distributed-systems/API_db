import ConfigParser
import psycopg2 
 
def config(filename='conf.ini', section='postgresql'):    
    parser = ConfigParser.ConfigParser()    
    parser.read(filename) 
    db = {}   
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return db
	
def connection ():
    try:
        par = config()
        connect = psycopg2.connect(**par)
    except:
        print "ERR"
    return connect