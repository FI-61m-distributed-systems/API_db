import BaseHTTPServer
import json
import urlparse
import sys, getopt
from call_func import set_json

def main(argv):
    host = ''
    port= ''
    try:
        opts, args = getopt.getopt(argv,"hs:p:",["host=","port="])
    except getopt.GetoptError:
        print 'python server.py -s <host> -p <port>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'python server.py -s <host> -p <port>'
            sys.exit()
        elif opt in ("-s", "--host"):
            host = arg      
        elif opt in ("-p", "--port"):
            port = arg
    try:
        BaseHTTPServer.HTTPServer((host,int(port)), MyServer).serve_forever()
    except:
        print 'python server.py -s <host> -p <port>'
        sys.exit(2)
class MyServer(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(self):
        """Respond to a POST request."""
        length = int(self.headers['Content-Length'])
        post_data = urlparse.parse_qs(self.rfile.read(length).decode('utf-8'))
        data = json.dumps(json.loads(post_data['json'][0]))
        print "Server call to DB..."
        self.send_response(200)
        self.send_header('Content-type','application/json')        
        try:
            self.send_header('Content',set_json(data))
        except:
            self.send_header('Content',500)
        self.end_headers()
        return

if __name__ == '__main__':
    main(sys.argv[1:])
