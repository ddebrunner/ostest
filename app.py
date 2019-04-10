import os

for k in os.environ:
    print(k, os.environ[k])
    
import http.server

addr = (os.environ['DAN_PYTHON_TEST_SERVICE_HOST'], int(os.environ['DAN_PYTHON_TEST_SERVICE_PORT']))

print('Address', addr)

httpd = http.server.HTTPServer(addr, http.server.BaseHTTPRequestHandler)
httpd.serve_forever()
