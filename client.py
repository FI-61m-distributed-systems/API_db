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
            "user": "vika",
            "field": "password",
	    "value": "xfjkv"            
         }
      ]
   }

p=urllib.urlencode({'json': json.dumps(data)})
response = urllib2.urlopen(url,p)
print response.getcode()
print response.headers['Content']
response.close()
