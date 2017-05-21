import urllib
import urllib2
import json

url = 'http://localhost:8000'

data = {
      "id": "id",
      "request": "update",
      "transaction":
      [
         {
            "action": "update",
            "user": "vika",
            "field": "password",
	    "value": "vv"
            
         }
      ]
   }

p=urllib.urlencode({'json': json.dumps(data)})
response = urllib2.urlopen(url,p)
print response.getcode()
s=response.headers['Content']
print s
response.close()
