from stub import get_login,get_password,get_email,money
from money import send_money
from registration import reg
from authorization import authorization_customer

m = raw_input("Input mode, which you want (s-send momey, a-authorization, r-registration): ")
if m == 's':
    print "test for send money"
    send_money(get_login(),get_login(),money())
elif m == 'a':
    print "test for authorization"
    authorization_customer(get_login(),get_password(),get_email())
elif m == 'r':
    print "test for add user"
    reg(get_login(),get_password(),get_email())
else:
    print "No mode"
