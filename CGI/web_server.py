import os,sys
from http.server import HTTPServer, CGIHTTPRequestHandler
srvraddr=('',80)
srvrobj=HTTPServer(srvraddr,CGIHTTPRequestHandler)
srvrobj.serve_forever()
