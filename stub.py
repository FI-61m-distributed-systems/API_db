def get_login(data):
    login= raw_input("login ")
    return login

def money(data):
    money= raw_input("money ")
    return money

def send_ok(data):
    return 200

def send_err(data):
    return 500

def get_password(data):
    password = raw_input("password ")
    return password

def get_email(data):
    email= raw_input("email ")
    return email
def do_condition(conditions):
    dictionary={"user": "login", "password": "password", "email": "email",
                "money":"money","game":"game_config"}
    i=0
    j=0
    srt=''
    for i in range(0,len(conditions),1):
        if conditions[i][0]== "money":
            srt = dictionary[conditions[i][0]]+" "+conditions[i][1]+" "+conditions[i][2]+" "
        else:
            srt = dictionary[conditions[i][0]]+" "+conditions[i][1]+" '"+conditions[i][2]+"' "
        if i<len(conditions)-1:
            srt=srt+ "AND "    
    return srt
def set_fields(fields):
    dictionary={"user": "login", "password": "password", "email": "email",
                    "money":"money","game":"game_config"}
    i=0
    srt=''
    for i in range(0,len(fields),1):        
        if i<len(fields)-1:
            srt = srt+dictionary[fields[i]]+","
        else:
            srt = srt+dictionary[fields[i]]
    return srt
