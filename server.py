import BaseHTTPServer
import json
import urlparse
import sys
from call_func import call_func
  
class MyServer(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(s):
        """Respond to a POST request."""
        length = int(s.headers['Content-Length'])
        post_data = urlparse.parse_qs(s.rfile.read(length).decode('utf-8'))
        data = json.dumps(json.loads(post_data['json'][0]))
        print "Server call to DB..."
        s.send_response(200)
        s.send_header('Content-type','application/json')        
        try:
            s.send_header('Content',call_func(data))
        except:
            s.send_header('Content',404)
        s.end_headers()
        return

if __name__ == '__main__':
    BaseHTTPServer.HTTPServer(('localhost',8000), MyServer).serve_forever()
